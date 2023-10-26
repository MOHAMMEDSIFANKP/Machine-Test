from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views import View
from .models import *


# User Login

class UserAuth(View):
    template_name = 'login.html'

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email.strip() or not password.strip():
            messages.error(request, "Fields can't be blank")
            return redirect('UserAuth')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Your email or password is incorrect")
            return redirect('UserAuth')

    def get(self, request):
        if not request.user.is_anonymous:
            return redirect('home')
        return render(request, self.template_name)


class home(View):
    template_name = 'index.html'

    @method_decorator(login_required(login_url='UserAuth'))
    def get(self, request):
        return render(request, self.template_name)
# Logout
class signout(View):
    @method_decorator(login_required(login_url='UserAuth'))
    def get(self, request):
        logout(request)
        return redirect('UserAuth')
# Profile view
class Profile(View):
    template_name = 'profile.html'
    @method_decorator(login_required(login_url='UserAuth'))
    def get(self, request):
        return render(request, self.template_name)
        
# Password Reset
class Resetpassword(View):
    template_name = 'profile.html'

    @method_decorator(login_required(login_url='UserAuth'))
    def post(self, request):
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        password = request.POST.get('password')

        if not current_password.strip() or not new_password.strip() or not password.strip():
            messages.error(request, "Fields can't be blank")
            return redirect('Profile')

        user = User.objects.get(email=request.user)

        if check_password(current_password, user.password):
            if new_password == password:
                user.set_password(new_password)
                user.save()

                user = authenticate(request, email=user.email, password=new_password)

                if user is not None:
                    login(request, user)
                    messages.success(request, "Password reset successfully")
                    return redirect('Profile')
                else:
                    messages.error(request, "Something went wrong")
                    return redirect('UserAuth')
            else:
                messages.error(request, "Password did not match")
                return redirect('Profile')
        else:
            messages.error(request, "Wrong old password")
            return redirect('Profile')

    def get(self, request):
        return render(request, self.template_name)


# Short Course View and paginations
class short_course_view(View):
    template_name = 'short-course-view.html'
    paginate_by = 2

    @method_decorator(login_required(login_url='UserAuth'))
    def get(self, request):
        query = request.GET.get('q')
        courses = ShortTermCourse.objects.all().order_by('id')
        if query:
            courses = courses.filter(Q(title__icontains=query) |  Q(subtitle__icontains=query) |   Q(description__icontains=query) )
        paginator = Paginator(courses, self.paginate_by)
        page = request.GET.get('page')
        paged_variation = paginator.get_page(page)
        context = {
            'courses': paged_variation,
        }
        return render(request, self.template_name, context)
    

# Short course Creations
class short_course_create(LoginRequiredMixin, CreateView):
    model = ShortTermCourse
    template_name = 'short-course-create.html'
    fields = '__all__'
    success_url = reverse_lazy('short_course_view')

    def form_valid(self, form):
        messages.success(self.request, 'Short Cource created successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Please fill in all required fields.')
        return super().form_invalid(form)
    
# Short Course Edit
class short_course_edit(LoginRequiredMixin,UpdateView):
    model = ShortTermCourse
    template_name = 'short-course-create.html'
    fields = '__all__'
    success_url = reverse_lazy('short_course_view')

    def form_valid(self, form):
        messages.success(self.request, 'Short Cource created successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Please fill in all required fields.')
        return super().form_invalid(form)

# Delete Short course
class short_course_delete(LoginRequiredMixin,DeleteView):
    model = ShortTermCourse
    template_name = 'short-course-create.html'
    fields = '__all__'
    success_url = reverse_lazy('short_course_view')