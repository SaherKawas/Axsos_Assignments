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

        if number > randomnumber:
            message = "Too high"
        elif number < randomnumber:
            message = "Too low"
        else:
            message = "Correct!"  

        request.session["message"] = message

        return redirect("/")

    return redirect("/")

def play(request):
    request.session.flush()

    return redirect("/")