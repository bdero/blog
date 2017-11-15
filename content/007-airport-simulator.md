Title: Airport "simulator"
Date: 2013-10-27 19:37
Category: Simulations
Tags: 2d, bitmap graphics, browser, canvas, html5, ivank.js, minimal, mobile, oldie, simulation, visualization
Slug: airport-simulator
Authors: bdero
Summary: During my sophomore year at college, I was on the lookout to insert graphics into whatever I could to loosen up some monotony. I decided that I would hack on displays to the labs I was doing for one of my classes by using Slick2D (it was basically a Java collections course). I presented in front of the class to show how easy it is to throw a little visual in front of something like this - I even found the I recorded for students explaining how grab the source!

During my sophomore year at college, I was on the lookout to insert graphics into whatever I could to loosen up some monotony. I decided that I would hack on displays to the labs I was doing for one of my classes by using Slick2D (it was basically a Java collections course). I presented in front of the class to show how easy it is to throw a little visual in front of something like this - I even found the I recorded for students explaining how grab the source!

Unfortunately, I hopped on the procrastination train after only one lab, so the resulting repository with the one modified lab, "airport simulation", might still be sitting on <a href="https://github.com/bdero/slick2d-structures-labs" title='Original "airport simulation" repository' target="_blank">GitHub</a>, but it was never committed to again.

I was reminded of this recently and quickly rewrote it yesterday for browser use.
<!--more-->


<iframe src="http://bdero.me/ivank-tests/airport/" height="371" width="100%" frameborder="no"></iframe><h5><strong>If you don't see anything in the frame above, then either <a title="Check if your browser supports WebGL" href="http://get.webgl.org/" target="_blank">your browser doesn't support WebGL</a>, or your graphics driver is not sufficient for initializing a WebGL context.</strong></h5>
The source code is available on <a title="Airport simulator test source code" href="https://github.com/bdero/ivank-tests/blob/gh-pages/airport/airport.js" target="_blank">GitHub</a>.

Non-interactive, all it really does is display two queues of airplanes sharing a runway - ones that are waiting to land, and ones that are waiting to take off. There is only one runway, so they share it based on priority, where the queue of planes waiting to land takes precedence. Each action occupies the strip for one second, while there are five 15% chances per second for a new airplane to arrive at the scene.

The graphics were made with <a href="http://inkscape.org/" title="Inkscape website" target="_blank">Inkscape</a>. The XCF file can be found in the <a href="https://github.com/bdero/slick2d-structures-labs/tree/master/src/lab4_AirportSimulation/images" title='Original "airport simulation" repository images' target="_blank">old repository</a>. And the graphics were rendered with WebGL via <a href="http://lib.ivank.net/" target="_blank">IvanK.js</a>.
