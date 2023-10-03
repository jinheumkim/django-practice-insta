from django.urls import path
from .views import Join,login,logOut,UploadProfile

urlpatterns = [
    path('join',Join.as_view()),
    path('login',login.as_view()),
    path('logout',logOut.as_view()),
    path('profile/upload',UploadProfile.as_view())
]