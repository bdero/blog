Title: Prototype: "Just the Basics" v0.2
Date: 2013-11-12 00:43
Category: Games
Tags: 2.5d, browser, canvas, gridwars, html5, interactive, ivank.js, javascript, jsdoc, just the basics, particles, pointer lock controls, prototype, shooter, space, top down, vector graphics, webgl
Slug: just-the-basics-2
Authors: Brandon DeRosier
Summary: It's week two with this thing and I met the goals I set at the last minute as usual. It's now got bullets firing, aiming with or without pointer lock controls, and simple enemies to kill called "Spin Stars". The delta time multiplier is being properly distributed and used with most everything (even with asymptotic functions like camera easing), so if you're running it fullscreen on legacy hardware and you're experiencing significant frame lag, it should still sort of <em>feel</em> like things are the correct speed.

It's week two with this thing and I met the goals I set at the last minute as usual. It's now got bullets firing, aiming with or without pointer lock controls, and simple enemies to kill called "Spin Stars". The delta time multiplier is being properly distributed and used with most everything (even with asymptotic functions like camera easing), so if you're running it fullscreen on legacy hardware and you're experiencing significant frame lag, it should still sort of <em>feel</em> like things are the correct speed.

I also modularized the code a bit and added JsDoc/Doxygen compatible comments for each file, class, and function. I haven't tried to generate any docs for it yet, but why not? I'd love to see this code get hacked on and reused. <!--more-->

<iframe src="http://bdero.me/jtb-releases/v0.2/" height="400" width="100%" frameborder="no"></iframe>
<h5><strong>If you don't see anything in the frame above, then either <a title="Check if your browser supports WebGL" href="http://get.webgl.org/" target="_blank">your browser doesn't support WebGL</a>, or your graphics driver is not sufficient for initializing a WebGL context.</strong></h5>
The source code is available on <a title="Just the Basics v0.2 source code" href="https://github.com/bdero/just-the-basics/tree/v0.2" target="_blank">GitHub</a>.

To take control of the canvas, click on it. Like my <a href="{filename}/8-just-the-basics-1.md" title="Prototype: “Just the Basics” v0.1">previous post</a>, you can use the classic <strong>W, S, A, and D keys</strong> (or the arrow keys) to navigate the ship around the field, but now you can control the direction of a cannon attached to the ship by <strong>moving the mouse</strong> around over the canvas.

You can also control the cannon by accepting the pointer lock request which fires every time the canvas is clicked, given that your browser supports it. This hides the mouse so you don't have to worry about accidentally moving the mouse out of the canvas and losing control.

Lastly, <strong>holding the mouse down</strong> causes the ship's cannon to continuously fire.

I'd never done anything with a collision detection grid before, but I figured that's what this would need if I want to stuff hundreds of enemies into the playing field and expect it to still run smoothly.

<figure style="width: 300px">
  <a href="{filename}/images/collision_plans.jpeg" target="_blank">
    <img class="size-medium wp-image-166" alt="Quick plans for the collision detection" src="{filename}/images/collision_plans.jpeg" width="300" height="191" />
  </a>
  <figcaption>
    Quick plans for the collision detection
  </figcaption>
</figure>

The whole "ActiveObject" thing for entities that do collision checking didn't end up happening since the player and the bullets will need to do different things upon collision. Instead, there's a general method in World that takes an entity and figures out if any enemies are colliding with it using the world's collision grid. Besides, why would I want to go overkill worrying about how everything involving entities needs to be stuffed somewhere within the entity hierarchy? Last time I checked, this isn't Java.

The resulting collision grid seems to be fast for bullet-to-entity collision detection so far, though I've yet to test it to its limit!

<img src="{filename}/images/lots_of_spin_stars.png" alt="Lots of Spin Stars" />

For the next time around, I'd like to have a couple more enemies, a timeline system, and maybe player death along with a way to start over.

More to come!

Graphics provided by WebGL via <a href="http://lib.ivank.net/" target="_blank">IvanK.js</a>.
