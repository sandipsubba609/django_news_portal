from django.shortcuts import render
from django.views import View
from accounts.forms import UserSignUpForm
# Create your views here.

class UserSignUpView(View):
    def get(self, request):
        form = UserSignUpForm
        print(request)
        pass
    
    def post(self, request):
        pass