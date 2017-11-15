Title: Some simplex noise
Date: 2013-10-06 05:53
Category: Algorithms
Tags: 2d, algorithm, browser, canvas, html5, iteration, ivank.js, javascript, minimal, perlin noise, plasma, simplex noise, visualization, webgl
Slug: some-simplex-noise
Authors: bdero
Summary: Just a tiny simplex noise test with retro colors. c:

Just a tiny simplex noise test with retro colors. c: <!--more-->

<iframe src="http://bdero.me/ivank-tests/simplexnoise/" height="200" width="100%" frameborder="no"></iframe><h5><strong>If you don't see anything in the frame above, then either <a title="Check if your browser supports WebGL" href="http://get.webgl.org/" target="_blank">your browser doesn't support WebGL</a>, or your graphics driver is not sufficient for initializing a WebGL context.</strong></h5>
The source code is available on <a title="Simplex noise test source code" href="https://github.com/bdero/ivank-tests/blob/gh-pages/simplexnoise/simplexnoise.js" target="_blank">GitHub</a>.

Nothing too too interesting - it just pans around and renders out a 3D simplex noise function, passing through the third dimension over time. You can manually control the pan direction and speed by clicking and dragging the mouse around. I wanted to write a bunch of simplex noise combinations to make different kinds of textures, but I quickly lost interest and figured that moving on to some 3D things might be more fun.

The colors are precomputed using the same method explained in my previous <a href="{filename}/002-julia-set-viewer.md" title="Julia set viewer">Julia set viewer</a> post. Since I wasn't too interested in writing an implementation myself, the actual simplex noise code was taken from a <a href="https://gist.github.com/banksean/304522#file-perlin-noise-simplex-js" title="banksean's simplex noise implementation" target="_blank">gist by banksean</a>.

Graphics provided by WebGL via <a href="http://lib.ivank.net/" title="IvanK Lib" target="_blank">IvanK.js</a>, though the simplex noise is just being software rendered!
