from django.shortcuts import render

# Create your views here.
def index(request):
    """index page"""
    return render(request, "learning_logs/index.html")