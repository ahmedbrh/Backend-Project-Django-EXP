from django.shortcuts import render
from django.views import View
import json
from  django.http import JsonResponse
# Create your views here.


class usernameValidationView(View):
    # post request
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        if str(username).isalnum():
            return JsonResponse({"username_error" : "le nom d'utilisateur ne doit pas contenir des caracteres "}, status=400)
            return JsonResponse({"username_valid": True})



class RegistrationView(View):
    # get request
    def get(self, request):
        return render(request, 'authentification/register.html')