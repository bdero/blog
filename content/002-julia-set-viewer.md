Title: Julia set viewer
Date: 2013-09-28 23:16
Category: Algorithms
Tags: 2d, algorithm, browser, canvas, classic, fractal, html5, interactive, iteration, ivank.js, javascript, julia set, mobile, vector graphics, visualization, webgl
Slug: julia-set-viewer
Authors: Brandon DeRosier
Summary: A little bit of fun with fractals!

A little bit of fun with fractals! <!--more-->

<iframe src="http://bdero.me/ivank-tests/julia/" width="100%" height="465" frameborder="no"></iframe><h5><strong>If you don't see anything in the frame above, then either <a title="Check if your browser supports WebGL" href="http://get.webgl.org/" target="_blank">your browser doesn't support WebGL</a>, or your graphics driver is not sufficient for initializing a WebGL context.</strong></h5>
The source code is available on <a title="Julia Set viewer source code" href="https://github.com/bdero/ivank-tests/blob/gh-pages/julia/julia.js" target="_blank">GitHub</a>.

There's nothing special about the way each pixel's color is determined. It's colored based on the number of iterations it takes a point to escape the given distance bound (in this case, <em>sqrt(10)</em>) in the Julia set function, just like <a title="How Julia set images are generated" href="http://www.youtube.com/watch?v=2AZYZ-L8m9Q#t=358" target="_blank">any other typical fractal viewer</a>.

I decided to have it precompute the color pallet like this:

```javascript
function generateColors() {
	colors = new Uint32Array(MAX_ITERATIONS);

	var escapeTime, red, green, blue;
	for (var i = 0; i < colors.length; i++) {
		escapeTime = i/MAX_ITERATIONS;

		red = (-Math.cos(escapeTime*Math.PI) + 1)/2*0xff;
		green = Math.sin(escapeTime*Math.PI)*0xff;
		blue = (Math.cos(escapeTime*Math.PI) + 1)/2*0xff;

		colors[i] = (0xff000000 | red | green << 8 | blue << 16);
	}
}
```

...and here's what the color functions look like on a graph, where blue starts off strong and dies off, green peaks in the middle, and red ends up strong:

<iframe src="http://graph.tk/" id="julia-set-viewer_colorgraph" width="100%" height="200" frameborder="no"> </iframe><script>
var graph=document.getElementById("julia-set-viewer_colorgraph");
graph.onload=function() { function g(m){ graph.contentWindow.postMessage(m,"http://graph.tk") };
g("add:(cos(x*pi)+1)/2"); // Blue
g("add:(-cos(x*pi)+1)/2"); // Red
g("add:sin(x*pi)"); // Green
g("scale:9,3");
g("center:0.5,0.5");
}</script>

The viewer is made up of a few small components:
<ul>
	<li>A <strong>viewport</strong>, which finds the rectangle on the complex plane to render based on given <em>translation coordinates</em>, a <em>zoom multiplier</em>, and the current <em>window resolution</em>.</li>
	<li>A <strong>bitmap</strong>, which holds the most up-to-date <em>image buffer</em> to display via WebGL. Sections of it are continuously overwritten by the <strong>renderer</strong>.</li>
	<li>A <strong>renderer</strong>, which calls the Julia set function continuously, limiting each execution time a maximum of <em>20ms</em> and keeping track of where it left off in the <strong>bitmap</strong> between each call. It also keeps track of the <em>offset</em> (a complex number to add to a point each time it's squared in the Julia set function).</li>
	<li>A <strong>controller</strong>, which sets up the head-up display <em>buttons</em>, <em>text</em>, and user input <em>listeners</em> to modify the <em>zoom</em> and <em>center</em> of the <strong>viewport</strong> and randomly select new <em>offsets</em> for the Julia set function.</li>
</ul>

Everytime you hit <strong>+</strong> to zoom in, the <em>zoom</em> of the <strong>viewport</strong> is multiplied by <em>1.5</em>. The <strong>viewport</strong> generates a rectangle every frame by essentially dividing a given starting rectangle's width and height by the <em>zoom</em>.

Because of this setup, if you zoom in far enough, you'll crash into a pixelated mess:
<img class="aligncenter" alt="julia_zoom" src="{filename}/images/julia_zoom.gif" />

This is due to the floating point numbers having limited precision - in the case of JavaScript, floating point numbers are 64-bit. You may also notice that the <strong>viewport</strong>'s <em>center</em> snaps while panning when you're zoomed in that far.

The graphics are provided by WebGL via the wonderful <a href="http://lib.ivank.net/" title="IvanK Lib" target="_blank">IvanK.js</a>. The Julia set itself is, however, ironically software rendered - mainly because IvanK.js isn't intended for use alongside low level access to WebGL.. and I wanted to see how fast I could get it to work in pure JavaScript. c:

No fragment shaders were <del>butchered</del> written in the making of this demo.
