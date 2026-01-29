from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm

def home(request):
    return render(request, 'core/home.html')

def guestbook(request):
    messages = Message.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guestbook')
    else:
        form = MessageForm()
    
    return render(request, 'core/guestbook.html', {
        'messages': messages,
        'form': form
    })

