from django.shortcuts import render
from .forms import UserMessageForm
from .models import UserMessage

def home(request):
    form = UserMessageForm()
    if request.method == "POST":
        UserMessage.objects.create(
            user_name = request.POST.get('user_name'),
            user_email = request.POST.get('user_email'),
            text = request.POST.get('text'),
        )
    context = {}
    return render(request, 'index.html', context)

def services(request):
    if request.method == "POST":
        UserMessage.objects.create(
            user_name = request.POST.get('user_name'),
            user_email = request.POST.get('user_email'),
            text = request.POST.get('text'),
        )
    context = {}
    return render(request, 'services.html', context)

def about(request):
    if request.method == "POST":
        UserMessage.objects.create(
            user_name = request.POST.get('user_name'),
            user_email = request.POST.get('user_email'),
            text = request.POST.get('text'),
        )
    context = {}
    return render(request, 'about.html', context)