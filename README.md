# chaos-game
Implementation of chaos game in python.

### Paramenters configuration
Parameters description:
- **height, width**: size of the canvas (it is recommended to use a square)
-  **num**: number of sides of the polygon
-  **lam**: distance (between 0 and 1) from the selected vertex of the polygon (the higher the more the new point will be distant)
-  **delta_space**: restriction on points of the vertex of the polygon that can be selected each time ([0] means that the same vertex cannot be selected, [1, -1] means that both adjacent anticlockwise and adjacent clockwise verteces cannot be selected)
-  **delta_time**: restriction on points of the vertex of the polygon that can be selected each time (0 means that no restrictions are applied, 2 means that **delta_space** restriction is applied regard to the vertex chosen 2 turns ago)
-  **iterations**: number of points drawn
-  **inner_color, outer_color**: RGB color respectively of near and far points from the center of the polygon
-  **points_at_once**: number of points drawn each ms
