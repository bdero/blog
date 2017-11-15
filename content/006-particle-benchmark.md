Title: Mini game: Particle Benchmark
Date: 2013-10-24 00:50
Category: Games
Tags: 2.5d, browser, canvas, circles, html5, interactive, javascript, mini game, monkey, oldie, particles, vector graphics
Slug: particle-benchmark
Authors: bdero
Summary: This is another oldie - and it's sort of a mini game because, even though there's no real way to win (I just played it by ear without any real planning or direction), it's still interactive in a very game-like way.

<figure>
  <img width="100%" src="{filename}/images/particles0.png" />
  <figcaption>
    Splash screen with dynamic particle text.
  </figcaption>
</figure>

This is another oldie - and it's sort of a mini game because, even though there's no real way to win (I just played it by ear without any real planning or direction), it's still interactive in a very game-like way.

I wrote most of it during the two weeks prior to attending college primarily to have something to show off to professors. The plan was to use it in my conquest to skip out of as many basic comp-sci classes as possible. Didn't work so well - but I did get into a pretty neat class working mostly with the Android SDK and OpenGL ES early on. Unfortunately, given that it was OpenGL ES <em>1.1</em>, the other students and I ended up only working with the highly outdated fixed pipeline.


The content isn't embedded into the post this time because, as much as it pains me to say, it doesn't handle resizing very well and I've lost the original source code (though I haven't given up looking for it in my backups). There was a version down the line that resized just fine, but maybe I can just add this one to my "properly remake into an actual game" list.

<h2 style="text-align: center;"><a title="&quot;Particles benchmark&quot; mini game" href="http://bdero.me/particle-roll/" target="_blank">Click here to play the mini game.</a></h2>

You can use the classic W, A, S, and D keys, or the arrow keys, to roll around. That's pretty much all you need to know. When compiling it as an Android application, it would rely on the gyroscope for movement to give it the "rolling a marble around on a surface" feel.

<figure>
  <img width="100%" src="{filename}/images/particles1.png" />
  <figcaption>
    The "mini game" in action.
  </figcaption>
</figure>

The sphere rotation effect is faked in a 2.5D-like way, where the attached 2D particles are being modified by a 3D rotation matrix and a Z-value based radii. Their draw order is also Z-indexed. The particle text was fun stuff - I designed a very low-res (3px by 5px characters) monospace typeface on a piece of graph paper, including both lowercase and uppercase letters as well as decimal numbers and various symbols. I then decided to compress it by row (so each character's data could be represented by a string of length 5, one for each row) and manually added each character to an array that corresponds to ASCII.

There are a couple of fun features, like how colliding with a red particle results in an opposing force and 1/5 total particle loss consisting of the particles that were closest to the point of impact. The yellow debris flying all over the place when colliding with blue-green particles at high speeds also makes a decent effect, and the delta clock in the background doesn't really do much, but its intent was to be an actual timer for the game.

The experimental part was to make everything.. a particle. All display objects share common ancestry because they're all just circles of various colors and sizes.

I wrote it in a proprietary BASIC-like language called Monkey and used its JavaScript translator. This isn't an endorsement. I do <em>not</em> recommend Monkey due to both its proprietary nature and the fact that this could have been more effectively and easily written directly in JavaScript.

The benefit of Monkey at the time was that it translates code for use with a handful of different platforms and frameworks almost seamlessly. Why didn't I just use <a title="Haxe official website" href="http://haxe.org/" target="_blank">Haxe</a>? Because I didn't do any research.
