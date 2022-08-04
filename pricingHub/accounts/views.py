from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# from django.http import HttpResponse   for testing


def home(request):
    return render(request, "index.html")


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('/login')

        else:
            messages.info(request, 'password does not match')
            return redirect('signup')
        return redirect('login')
    else:

        return render(request, 'register.html')






#For Testing
# def home_view(request):


#     name = "Justin"
#     HTML_STRING = f"""
# <h1> Hello {name}</h1>
# <p>My first django page</p>
# """
#     return HttpResponse(HTML_STRING)




# def login(request):

#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']

#         user = auth.authenticate(email=email, password=password)

#         if user is not None:
#             auth.login(request, user)
#             return redirect('/')
#         else:
#             messages.info(request, 'Invalid Credentials')
#             return redirect('login')

#     else:
#         return render(request, 'login.html')

# def logout(request):
#     auth.logout(request)
#     return redirect('login')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
