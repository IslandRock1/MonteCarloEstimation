# MonteCarloEstimation
Rendering Monte Carlo simulation to estimate the mathematical constant pi.

## How it works

### Estimation
This piece of (quite terrible code) is using the ratio of random points in a circle vs in a square to estimate pi. You start by making a square with an inscribed circle, then create random points within that square. A lot of the points created will not only be inside the square, but also the circle. If you take the ratio, and multiply it by 4 you can estimate the value of pi given that you have enought points.

### Rendering
The rendering is done with pygame. It draws up the square with the inscribed circle, as well as some usefull stats. Then starts drawing in points. After 10 million points it will stop rendering, and only do the computation.

## Saving as video
To create a video out of this you will have save screenshots of each frame, then later combine them to a single video using the `renderer.py` script. This is ofcourse a terrible way to do this, but a simple one that works for me. Saving the images does take a lot of time because of using slow storage such as ssd/hdd so if you want to watch the simulation live i reccommend commenting out line 317 to not take screenshots.

## Dependencies
For this to run you need pygame (installed with `pip install pygame`), as well as the Fraction and Vec2 library in the library folder.
