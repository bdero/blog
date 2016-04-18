Title: Tower of Hanoi
Date: 2013-09-22 05:53
Category: Algorithms
Tags: 2d, algorithm, browser, canvas, classic, html5, ivank.js, javascript, minimal, puzzle, recursion, tower of hanoi, tweener, vector graphics, visualization, webgl
Slug: tower-of-hanoi
Authors: Brandon DeRosier
Summary: I figured I'd start with something classic.

I figured I'd start with something classic. <!--more-->

<iframe src="http://bdero.me/ivank-tests/hanoi/" width="100%" height="465" frameborder="no"></iframe>
<h5><strong>If you don't see anything in the frame above, then either <a title="Check if your browser supports WebGL" href="http://get.webgl.org/" target="_blank">your browser doesn't support WebGL</a>, or your graphics driver is not sufficient for initializing a WebGL context.</strong></h5>
The source code is available on <a title="Tower of Hanoi Solver source code" href="http://git.cheesekeg.com/?p=ivank-tests.git;a=history;f=hanoi;hb=HEAD" target="_blank">git.cheesekeg.com</a>.

It works by generating the optimal solution using the common <a title="Tower of Hanoi recursive solution" href="https://en.wikipedia.org/wiki/Tower_of_Hanoi#Recursive_solution" target="_blank">recursive algorithm</a>. It then walks through each step in the solution sequence, shifting disks from peg to peg in order to give a human-friendly visual. It can generate the solution and display it for any number of starting disks. The number of disks to use is passed as an argument to the <strong>Hanoi()</strong> constructor.

The generated solution for three disks looks like this:
[prettify class="javascript"][[0, 2], [0, 1], [2, 1], [0, 2], [1, 0], [1, 2], [0, 2]][/prettify]

It's organized into steps, where each array element consists of a source peg and destination peg. So the first step says to move the top-most disk of <strong>peg 0</strong> to <strong>peg 2</strong>, and the second step says to move the top disk of <strong>peg 0</strong> to <strong>peg 1</strong>, etc.. If all of the steps in the sequence were completed, then the disks would be left correctly stacked on top of <strong>peg 2</strong>.

If you run your browser's JavaScript console (<strong>Ctrl+Shift+K</strong> in Firefox, <strong>Ctrl+Shift+J</strong> in Chromium) and then refresh this page, you can inspect the generated solution array, which is logged after the algorithm completes and before the disks start visually shifting from peg to peg.

The graphics are provided by WebGL via <a href="http://lib.ivank.net/" target="_blank">IvanK.js</a> and <a href="http://tweener.ivank.net/" target="_blank">Tweener</a>. IvanK.js is really nice because it abstracts a lot of entity management out of the way, providing lots of conveniences that the Flash API makes available without any of the proprietary garbage attached. Very fun and suitable for fast WebGL games and interactive prototypes!
