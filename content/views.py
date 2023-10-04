import os
from uuid import uuid4
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from .models import Feed
from insta.settings import MEDIA_ROOT


# Create your views here.
class Main(APIView):
    def get(self, request):
        feed_object_list = Feed.objects.all().order_by('-id')
        feed_list = []
        
        for feed in feed_object_list:
            user = User.objects.filter(email = feed.email).first()
            feed_list.append(dict(image = feed.image,
                                  content = feed.content,
                                  like_count = feed.like_count))
        email = request.session.get('email',None)
        
        if email is None:
            return render(request, "user/login.html")
        
        user = User.objects.filter(email = email).first()
        
        
        if user is None:
            return render(request, "user/login.html")
        
        return render(request, "insta/main.html",context = dict(feeds = feed_list, user=user))
    

class UploadFeed(APIView):
    def post(self, request):
        
        file = request.FILES['file']
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT,uuid_name)
        
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        
        image = uuid_name
        content = request.data.get('content')
        email = request.session.get('email',None)
        
        Feed.objects.create(image = image, content = content, email = email, like_count = 0)
        
        return Response(status=200)
    
class Profile(APIView):
    def get(self, request):
        email = request.session.get('email',None)
        
        if email is None:
            return render(request, "user/login.html")
        
        user = User.objects.filter(email = email).first()
        
        if user is None:
            return render(request, "user/login.html")
        
        return render(request, "content/profile.html" , context = dict(user = user))
    
        