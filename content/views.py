from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed


# Create your views here.
class Main(APIView):
    def get(self, request):
        Feed_list = Feed.objects.all()
        
        print(Feed_list)
        return render(request, "insta/main.html")