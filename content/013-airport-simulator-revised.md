Title: Airport "simulator" revised
Date: 2014-03-10 19:37
Category: Simulations
Tags: 2d, bitmap graphics, browser, canvas, html5, ivank.js, minimal, mobile, oldie, simulation, visualization
Slug: airport-simulator-revised
Authors: bdero
Summary: I was recently asked by my previous professor to make a revision to the "airport simulator" port that I posted earlier here. The difference is that there's now a small overlay on the top left corner with slider controls for arrival and departure probabilities.

I was recently asked by my previous professor to make a revision to the "airport simulator" port that I posted earlier here.

The difference is that there's now a small overlay on the top left corner with slider controls as follows:

- **Arrival probability**: The probability that an airplane will be added to the "landing" queue per second
- **Departure probability**: The probability that an airplane will be added to the "takeoff" queue per second
- **Duration**: The amount of time that the simulation will run before pausing in seconds

<iframe src="http://bdero.me/ivank-tests/airport-sliders/" height="450" width="100%" frameborder="no"></iframe><h5><strong>If you don't see anything in the frame above, then either <a title="Check if your browser supports WebGL" href="http://get.webgl.org/" target="_blank">your browser doesn't support WebGL</a>, or your graphics driver is not sufficient for initializing a WebGL context.</strong></h5>

The source code is available on <a title="Airport simulator test source code" href="https://github.com/bdero/ivank-tests/blob/gh-pages/airport-sliders/airport.js" target="_blank">GitHub</a>.

The new overlay is just an "absolute" positioned DIV, while the sliders and buttons use <a href="http://jqueryui.com/slider/" target="_blank">jQuery-UI</a> along with <a href="http://jquery.com/" target="_blank">jQuery</a> for control code.

See my <a href="/airport-simulator.html" title="Airport “simulator”">older post</a> for more information.
