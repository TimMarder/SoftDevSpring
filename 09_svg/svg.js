// Tim Marder
// SoftDev2 pd06
// K09 -- Connect the dots
// 2019-03-13

var pic = document.getElementById("vimage");

function clear(){
    while(pic.firstChild){
        pic.removeChild(pic.firstChild);
    }
}

prevx = []
prevy = []

pic.addEventListener("click", function(e){
    if(pic.firstChild){
        var l = line(e.clientX, e.clientY, pic.lastElementChild.getAttribute("cx"), pic.lastElementChild.getAttribute("cy"));
        pic.appendChild(l);
    }
    pic.appendChild(dot(e.clientX, e.clientY));

    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute("cx", e.offsetX);
    c.setAttribute("cy", e.offsetY);
    c.setAttribute("r", 10);
    c.setAttribute("fill", "red");
    c.setAttribute("stroke", "red");
    return c;

    prevx.push(e.offsetX);
    prevy.push(e.offsetY);

    var l = document.createElementNS("http://www.w3.org/2000/svg", "line");
    l.setAttribute("x1", prevx[prevx.length - 1]);
    l.setAttribute("x2", e.offsetX);
    l.setAttribute("y1", prevy[prevy.length - 1]);
    l.setAttribute("y2", e.offsetY);
    l.setAttribute("stroke", "black");
    return l;
});
