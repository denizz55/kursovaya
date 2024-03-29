from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView

from .models import Clock

def news(request):
    
    return render(request, 'myapp/news.html', )

def registration(request):
    return render(request, 'myapp/registration.html')

def katalog(request):
    clock = Clock.objects.all()
    return render(request, 'myapp/katalog.html', {'clock': clock})

def authorization(request):
    return render(request, 'myapp/authorization.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('news') 
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Замени 'login' на имя URL-адреса страницы входа
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def post_detail(request, pk):
    Ck = get_object_or_404(Clock, id=pk)
    return render(request, 'myapp/product.html', {
        "Ck":Ck,
 })

