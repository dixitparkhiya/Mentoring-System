from django.shortcuts import render ,redirect
from django.contrib.auth import logout , login
from  django.contrib.auth.forms import AuthenticationForm

# def signup_view(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request,user)
#             return redirect('home')
#     else:
#         form = SignupForm()
#     return render(request,'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('student:home')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form': form})


def logout_view(request):
    logout(request)
    return redirect('student:home')


