function press(7){
    var button = document.querySelector("#display");
    if(button.innerText === "0" && 7 !=="."){
        button.innerText = 7; 
    }
 else {
    button.innerText += 7;
}
}