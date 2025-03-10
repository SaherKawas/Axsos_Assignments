function acceptFriend(){
    var friend = document.getElementById("class-list1");
    friend.remove();
    var request = document.getElementById("request-number");
    request.innerText --;
    var friend= document.getElementById("connection-number");
    friend.innerText ++ ;

}

function declineFriend(){
    var friend = document.getElementById ("class-list1");
    friend.remove();
    var request = document.getElementById ("request-number");
    request.innerText --;
}
function changeName(){
    var name = document.getElementById("name");
    name.innerText = "Anna Sofia";
}


