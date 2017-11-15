Title: (Not-so) infinite simplex noise map in 3D
Date: 2013-10-14 23:20
Category: Algorithms
Tags: 3d, algorithm, browser, canvas, html5, interactive, javascript, minimal, perlin noise, pointer lock controls, quake controls, simplex noise, terrain, three.js, visualization, webgl
Slug: infinite-simplex-noise-map-3d
Authors: bdero
Summary: I thought this might be a good start for something 3D. It's not-so infinite because the terrain doesn't keep regenerating in front of the camera as you move around (which wouldn't even really take that much refactoring), but the camera's height should keep changing according to the noise even after moving far away from the terrain.

I thought this might be a good start for something 3D. It's not-so infinite because the terrain doesn't keep regenerating in front of the camera as you move around (which wouldn't even really take that much refactoring), but the camera's height should keep changing according to the noise even after moving far away from the terrain.
<!--more-->


<iframe src="http://bdero.me/threejs-tests/simplexmap/" height="465" width="100%" frameborder="no"></iframe><h5><strong>If you don't see anything in the frame above, then either <a title="Check if your browser supports WebGL" href="http://get.webgl.org/" target="_blank">your browser doesn't support WebGL</a>, or your graphics driver is not sufficient for initializing a WebGL context.</strong></h5>
The source code is available on <a title="Simplex terrain map source code" href="https://github.com/bdero/threejs-tests/blob/gh-pages/simplexmap/simplexmap.js" target="_blank">GitHub</a>.

To use it, just click on it to receive a pointer lock request through your browser. If you're using a flavor of Firefox, the request will display in the form of a balloon popup. When the request is accepted, you'll be able to pan the camera around Quake style. You can also move about the scene using the classic W, S, A, and D keys.

As the title implies, the shape of the terrain and the Y-position of the camera is determined by a similar simplex noise function (provided by <a title="simplex-noise.js Github repository" href="https://github.com/jwagner/simplex-noise.js" target="_blank">simplex-noise.js</a>) to that of which I used in my <a title="Some simplex noise" href="{filename}/003-some-simplex-noise.md">previous post</a>. The only real difference is the fact that I used 2D simplex noise here instead of 3D since I had no interest in making the terrain morph.
That type of thing would totally be useful for morphing a water surface. Though, in that case, one might just consider using a <a title="webgl-noise Github repository" href="https://github.com/ashima/webgl-noise" target="_blank">vertex shader implementation of simplex noise</a>.

Graphics provided by WebGL via the wonderful <a title="three.js Github repository" href="https://github.com/mrdoob/three.js" target="_blank">three.js</a>.
