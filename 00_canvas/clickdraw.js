// Tim Marder
// SoftDev2 pd06
// K#00 -- I See a Red Door...
// 2019-01-30

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var clear = document.getElementById("clear");
var toggle = document.getElementById("toggle");
var state = "rectangle";


function getPos(c, e) {
    var rectangle = c.getBoundingClientRect();
    return {
        x: e.clientX - rectangle.left,
        y: e.clientY - rectangle.top
    };
}


c.addEventListener('click', function(e) {
    const height = 40;
    const width = 40;
    const horiz_rad = 5;
    const vert_rad = 5;
    var pos = getPos(c, e);

    if (state == "rectangle") {
        ctx.fillRect(pos.x - (width / 2), pos.y - (height / 2), width, height);
    }
    else {
        ctx.beginPath();
        ctx.ellipse(pos.x - (horiz_rad / 4), pos.y - (vert_rad / 4), horiz_rad, vert_rad, 0, 0, 2 * Math.PI);
        ctx.fill();
    }
});


clear.addEventListener('click', function(e) {
    ctx.clearRect(0, 0, c.height, c.width);
});


toggle.addEventListener('click', function(e) {
    if (state == "rectangle") {
        state = "dot";
        toggle.innerHTML = "Dot";
    }
    else {
        state = "rectangle";
        toggle.innerHTML = "Rectangle";
    }
});
