function increaseLike(){
   var inner = document.getElementById("numberoflikes")
    inner.innerText ++;
    var button= document.getElementById("like")
    button.style.backgroundColor="Green"
    if(button.innerText === "Like"){
        button.innerText = "Liked";
    }
}



function increaseLikes(){
    var x = document.getElementById("numberoflikes2")
    x.innerText ++;
}

function increaseLike2(){
    var y = document.getElementById("numberoflikes3")
    y.innerText ++;
}