function press(num){
    var button = document.querySelector("#display");
    // console.log(button)
    if(button.innerText === "0"){
        button.innerText = num; 
    }
 else {
    button.innerText = button.innerText+num;
}
}
function setOP(op){
    // console.log(op)
    var operator= op
    // console.log(operator)

    var number1 = document.querySelector ("#display").innerText
    console.log(number1)
    
}