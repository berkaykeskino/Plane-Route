<h1 align = "center"> <img src= "https://clipart-library.com/images/AcbjRexdi.png" width= 300px height=auto> </h1>

<h1 align = "center"> ✈️Welcome to Plane Router! </h1> 
⚡⚡What does this code do?
When you choose two points on the earth's surface, what is the shortest path between them? The program finds it on 3D and reflects the path on 2D map to alleviate understanding the path.
<br><br>
💥How?
When you choose two points on 2D map, it translates those coordinates into 3D. Draws a line between the two points in 3D coordinates (blue line). Then splits that line into n many points. After that behaves like those points are vectors from the center of the sphere and makes their length equal to the radius, which is equal to making them touch the surface(dotted line).
<p align = "center"><img src= "https://github.com/berkaykeskino/Plane-Route/blob/main/Photos/sphere-line.png?raw=true" width= 300px height=auto></p>
Finally, translates those n points' locations on the surface into 2D map locations.

<hr>
👀See an example:
<p align = "center"><img src= "https://github.com/berkaykeskino/Plane-Route/blob/main/Photos/example.PNG?raw=true" width= 300px height=auto></p>

🔗Note that you should install Pygame to run the code.
