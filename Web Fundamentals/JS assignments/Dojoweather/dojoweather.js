function alertCity(){
    alert("You are now seeing the temperatures in Burbank!");
}

function hideCookie(){
    var cookie=document.getElementById("cookie-popup")
    cookie.remove();
}

function changeTemperature() {
    var toFahrenheit = document.getElementById("temperature").value === "°F";

    document.querySelectorAll(".temperature-red, .temperature-blue").forEach(temp => {
        let num = parseInt(temp.innerText); 
        
        if (toFahrenheit) {
            temp.innerText = Math.round(num * 9/5 + 32) + "°"; 
        } else {
            temp.innerText = Math.round((num - 32) * 5/9) + "°"; 
        }
    });
}