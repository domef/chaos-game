import random
import math
import collections
import itertools
import tkinter as tk

# delta_time: only in n-th (current) or all n or only choosen?

# parameters
height = 800
width = 800
num = 5
lam = 1 / 2
delta_time = 1
delta_space = [1, -1]
iterations = 10 ** 5
inner_color = (191, 74, 168)
outer_color = (81, 208, 222)
points_at_once = 50

def draw_points():
    global current_iteration
    global last_point

    for _ in itertools.repeat(None, points_at_once):
        current_iteration += 1

        v = random.randint(0, num - 1)        

        if delta_time != 0:
            while any(v == (last_vertexes[0] + s) % num for s in delta_space):
                v = random.randint(0, num - 1)

            last_vertexes.append(v)
            last_vertexes.popleft()

        point = points[v]

        h = int(lam * last_point[0] + (1 - lam) * point[0])
        w = int(lam * last_point[1] + (1 - lam) * point[1])
        last_point = (h, w)

        distance = math.sqrt((h - center[0]) ** 2 + (w - center[1]) ** 2)
        c = distance / r

        c1 = int((1 - c) * inner_color[0] + c * outer_color[0])
        c2 = int((1 - c) * inner_color[1] + c * outer_color[1])
        c3 = int((1 - c) * inner_color[2] + c * outer_color[2])

        canvas.create_line(h, w, h+1, w, fill='#%02x%02x%02x' % (c1, c2, c3))

    if current_iteration < iterations:
        root.after(1, draw_points)

if __name__ == '__main__':
    root = tk.Tk()
    canvas = tk.Canvas(root, height=height, width=width, bg='black')
    canvas.pack()

    last_vertexes = collections.deque([-1] * delta_time)
    center = (int(height / 2), int(width / 2))    
    r = min(height, width) / 2 - 1
    theta = 2 * math.pi / num
    points = []

    for i in range(num):
        h = r * math.cos(theta * i) + height / 2
        w = r * math.sin(theta * i) + width / 2
        inth = int(h)
        intw = int(w)
        points.append((inth, intw))
        canvas.create_line(inth, intw, inth+1, intw, fill='#%02x%02x%02x' % outer_color)

    last_point = (random.randint(0, height - 1), random.randint(0, width - 1))
    current_iteration = 0

    draw_points()
    root.mainloop()