function changeText(el){
    if(el.innerText=="Login"){
        el.innerText="Logout"
    }
    else{
        el.innerText="Login"
    }
}

function getNotification(){
    alert("Ninja was liked")
}

function hideButton(element){
    element.remove();
}