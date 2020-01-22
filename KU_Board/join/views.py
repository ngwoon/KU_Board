from django.shortcuts import render
from .models import UserInfo
# Create your views here.

def test(request):
    return render(request, 'join/signin.html')

def check(request):
    id = request.POST['id']
    pw = request.POST['pw']

    idpw_list = UserInfo.objects.all()

    for pair in idpw_list:
        if pair.identifier == id:
            if pair.password == pw:
                return render(request, 'join/message.html', {'msg' : 'success'})
            else:
                return render(request, 'join/message.html', {'msg' : 'password error'})

    return render(request, 'join/message.html', {'msg' : 'fail'})

def signup(request):
    return render(request, 'join/signup.html')





