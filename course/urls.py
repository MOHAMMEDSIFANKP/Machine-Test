from django.urls import path
from .import views
from course.views import *
urlpatterns = [
    path('', UserAuth.as_view(), name='UserAuth'),
    path('home/', home.as_view(), name='home'),
    path('signout/', signout.as_view(), name='signout'),
    path('profile/', Profile.as_view(), name='Profile'),
    path('resetpassword/', Resetpassword.as_view(), name='Resetpassword'),
    path('short_course_view/', short_course_view.as_view(), name='short_course_view'),
    path('short_course_create/', views.short_course_create, name='short_course_create'),
    path('short_course_edit/<int:id>', views.short_course_edit, name='short_course_edit'),
    path('short_course_delete/<int:id>', views.short_course_delete, name='short_course_delete'),

]
