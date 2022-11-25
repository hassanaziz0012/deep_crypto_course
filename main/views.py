from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.views import View
from main.models import Video


# Create your views here.
@method_decorator(login_required, name="dispatch")
class HomeView(View):
    def get(self, request):
        videos = Video.objects.all().order_by('-creation_date')
        return render(request, 'home.html', context={"videos": videos, "title": "Course Videos"})


@method_decorator(csrf_exempt, name="dispatch")
class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'login.html', context={"title": "Login"})

    def post(self, request):
        memberid = request.POST.get('memberid')
        password = request.POST.get('password')
        user = authenticate(request, username=memberid, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, message="Logged in successfully.", extra_tags="alert-success")
            return redirect('home')

        messages.error(request, "Invalid memberid or password.", extra_tags="alert-danger")
        return redirect('login')


@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, 'Logged out successfully', extra_tags="alert-info")
        return redirect('login')


@method_decorator(login_required, name='dispatch')
class VideoView(View):
    def get(self, request, id):
        video = Video.objects.get(pk=id)
        return render(request, "video.html", context={"video": video, "title": video.title})