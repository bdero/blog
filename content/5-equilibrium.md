Title: Mini game: Equilibrium
Date: 2013-10-20 23:27
Category: Games
Tags: 2d, browser, canvas, circles, html5, interactive, javascript, jsgamesoup, mini game, minimal, oldie, vector graphics
Slug: equilibrium
Authors: Brandon DeRosier
Summary: Well, that streak quickly came to an end. I was hoping to write new experiments on time to post every week, but time has gotten very tight very fast. Instead, I have something old to share. I banged most of it out during a physics class one day last year right around the time I started feeling sour about my college.

Well, that streak quickly came to an end. I was hoping to write new experiments on time to post every week, but time has gotten very tight very fast. Instead, I have something old to share. I banged most of it out during a physics class one day last year right around the time I started feeling sour about my college. <!--more-->

<iframe src="http://bdero.me/html5fun/projects/equilibrium/" height="465" width="100%" frameborder="no"></iframe>
The source code is available on <a title="Equilibrium source code" href="https://github.com/bdero/html5fun/blob/gh-pages/projects/equilibrium/equilibrium.js" target="_blank">GitHub</a>.

Once the green or red point is absorbed, left clicking restarts the mini game.

You are a mouse controlled green point who is able to absorb both the red center point and the spiraling white points. The red point simply remains in the center, collecting the white points that you don't collect yourself. Absorption of a white point results in growth. When you (the green point) touch the red point, both points shrink.

There are two ways to lose, but no real way to win. In order to stay playing for as long as possible and progress, you must prevent the red and green points from absorbing each other. There's a sort of score/level bar at the top that collects as the sizes of the points are canceled out. Each time the "score" bar fills up, it resets and becomes more difficult to refill.

I figure this might be a fun little idea to expand later.

Graphics provided by the canvas 2D API via <a title="jsGameSoup" href="http://www.jsgamesoup.net/" target="_blank">jsGameSoup</a>.
