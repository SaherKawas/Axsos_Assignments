from django.shortcuts import render, redirect
import random

def root(request):
    if "randomnumber" not in request.session:
        request.session["randomnumber"] = random.randint(1, 100)

    if "attempts" not in request.session:
        request.session["attempts"] = 0

    message = request.session.get("message", "")

    context = {
        "message": message,
        "attempts": request.session["attempts"],
        "randomnumber": request.session["randomnumber"]
    }

    request.session.pop("message", None)

    return render(request, "index.html", context)

def guess(request):
    if request.method == "POST":
        number = int(request.POST['number'])
        randomnumber = request.session["randomnumber"]

        request.session["attempts"] += 1
        attempts=request.session["attempts"]

        if number > randomnumber: 
            message = "Too high"
        elif number < randomnumber:
            message = "Too low"
        else:
            message = "Correct!"  
        if attempts>=5:
            message="You lose"

        request.session["message"] = message

    return redirect("/")

def play(request):
    request.session.flush()

    return redirect("/")

def win(request):
    if request.method == "POST":
        winner={
            "firstname": request.POST["firstname"],
            "lastname": request.POST["lastname"],
            "attempts": request.session.get("attempts",0)
        }

        if "winners" not in request.session:
            request.session["winners"] = []

        winners = request.session["winners"]
        winners.append(winner)
        request.session["winners"] = winners  

    return render(request, "winners.html", {"winners": winners})
    