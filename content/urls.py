from django.urls import path
from .views import UploadFeed,Profile,UploadReply,Main,ToggleLike,ToggleBookmark,Follow

urlpatterns = [
    path('upload',UploadFeed.as_view()),
    path('reply', UploadReply.as_view()),
    path('profile',Profile.as_view()),
    path('bookmark',ToggleBookmark.as_view()),
    path('main',Main.as_view()),
    path('like',ToggleLike.as_view()),
    path('follow',Follow.as_view())
]