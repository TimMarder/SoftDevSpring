//Britni Canale & Jabir Chowdhury -- Paint2.0
//SoftDev2 pd6
//K01 -- And I want to paint it Better
//2019 - 01 - 31

var c = document.getElementById("slate");
var ctx = c.getContext("2d");

var b = document.getElementById("clear");
b.addEventListener('click',
  function(e){
    e.preventDefault();//in place to avoid default functionfrom event if there is a default
    ctx.clearRect(0,0,600,600);
    console.log(e);
  }
);

var shape = "dot";


c.addEventListener('click',
  function(e){
    e.preventDefault()
    if(shape == "dot"){
      ctx.beginPath(); //Resets stroke before each ellipse is drawn, prevents connected ellipses
      //Offset gives difference of pixels between event point and reference point, which is upper left corner of the element in question, the canvas
      ctx.ellipse(e.offsetX, e.offsetY, 3,3, 0, 0, 2*Math.PI, true);
      ctx.fill();
    }else{
      ctx.fillRect(e.offsetX, e.offsetY, 20,20);
    }
    console.log(e);
  }
);

var s = document.getElementById("shape");
s.addEventListener('click',
  function(e){
    e.preventDefault();
    if(shape == "box"){
      shape = "dot";
    }else{
      shape = "box";
    }
  }
);
