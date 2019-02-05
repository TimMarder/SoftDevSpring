// Pegleg Pete's Posse - Tim Marder and Maggie Zhao
// SoftDev2 pd06
// K03-- They lock us in the tower whenever we get caught ...which is often
// 2019-02-04

//model for HTML5 canvas-based animation

//access canvas and butttons via DOM
var c = document.getElementById("playground"); //Canvas element
var ctx = c.getContext("2d"); //Get context of canvas
var stopButton = document.getElementById("stop");
var dotButton = document.getElementById("circle");
var requestID;
var radius = 0;
var growing = 1;
var shrinking = 0;
//var goPressed = 0;
//var stopPresed = 0;


//set fill color to cyan
ctx.fillStyle = "#00ffff";

var clear = function() {
  ctx.clearRect(0, 0, c.width, c.height);
};

var drawDot = function() {
  //...
  //draw the dot
  requestID = requestAnimationFrame(drawDot);
  clear();
  ctx.beginPath();
  ctx.arc(c.width / 2, c.height / 2, radius, 0, 2 * Math.PI );
  ctx.stroke();
  ctx.fill();

  if (growing) {
      radius++;
  }
  if (shrinking) {
      radius--;
  }


  if (radius >= c.width / 2) {
      growing = 0;
      shrinking = 1;
  }
  if (radius == 0 && shrinking == 1) {
      shrinking = 0;
      growing = 1;
  }

  console.log(requestID);
  console.log("growing = " + growing);
};

var stopIt = function() {
  cancelAnimationFrame(requestID);
};

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);

// Adds event listener to the canvas


/* EXPLANATIONS
ctx.clearRect();
 - erases the pixels in the canvas by making them transparent black
e.preventDefault();
 - prevents the default action of the user's interaction of the html element.
 - This can be used for error checking / data filtering
 - Does not work for buttons, but does work for checkboxes and inputs
ctx.beginPath();
 - begins a path, or any series of strokes (i.e. lines, arcs, ellipses) so that it can be drawn with different strokestyles
 - primes the canvas to draw the specified line (stroke) between the given coordinates
 - if not to begin the path, then beginPath() resets the current path
e.offsetX
 - upon clicking (the mouseEvent), reads the X-coordinate of the mouse pointer in local (DOM content) coordinates (aka the offset in the X coordinate between the event and the padding edge of the target node)
e.offsetY
 - upon clicking (the mouseEvent), reads the Y-coordinate of the mouse pointer in local (DOM content) coordinates (aka the offset in the Y coordinate between the event and the padding edge of the target node)
ctx.moveTo(x, y);
 - begins a new subpath at the point specified by the given (x, y) coordinates
ctx.lineTo(x, y);
 - creates a straight line linking the last point of the path to the points specified by the (x, y) coordinates
 - does not directly render anything
ctx.stroke();
 - strokes (or outlines) the current path with the current stroke style
*/
