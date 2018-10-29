from django.shortcuts import render

def base(request):
    if request.method == 'GET':
        return render(request, "heritage_register/card_pattern.html", {})
