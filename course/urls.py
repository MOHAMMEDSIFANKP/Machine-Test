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
    path('short_course_create/', short_course_create.as_view(), name='short_course_create'),
    path('short_course_edit/<int:pk>', short_course_edit.as_view(), name='short_course_edit'),
    path('short_course_delete/<int:pk>', short_course_delete.as_view(), name='short_course_delete'),

]
