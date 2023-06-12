from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def app(request):
    context = {}
    return render(request,"schools/home.html",context=context)