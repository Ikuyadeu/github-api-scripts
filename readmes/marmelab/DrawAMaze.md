# Draw a maze

Draw a maze is a game exploring HTML5 canvas element. To test it, you need a webcam, a sheet of paper and a pen (choose a black one for better result).

## How to play?

To play to "Draw a maze", you first have to configure a virtual host on a Web server. Indeed, canvas element has some security restrictions which prevent you from executing the index.html file directly into your browser.

* Draw a maze on your paper: do not hesitate to create thick black walls for better recognizing. 
* Open the website and allow it to use your webcam. 
* Take a picture of your maze, thanks to the Snap button. 
* Adjust the wall threshold to reduce number of wall artifacts.

Now that your maze is ready, simply move the player (the red dot) from entrance to exit with arrow keys.

## Todos

* Improve collision detection (it really works only with a radius of 1 and a speed of 1)
* Add a little bit more design
* Add an AI trying to catch you
