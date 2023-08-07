from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import Snippet  
from .serializers import SnippetSerializer  
from django.contrib.auth import authenticate,login as lg, logout
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required



class UserLogin(APIView):
    def post(self,request):
        username=request.data.get("username")
        password=request.data.get("password")
        is_valid=authenticate(username=username,password=password)
        
        if is_valid:
            lg(request, is_valid)
            token="12345"
            name=is_valid.first_name+" "+is_valid.last_name
            return Response({"status":'success',"message":"Login successfull","data":{"token":token,"name":name}})

               
        
        return Response({"status":'fail',"message":"Login failed","data":{}})


# @login_required(login_url="login")
class SnippetDetails(APIView): 
  
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:          
            result = Snippet.objects.all()  
            serializers = SnippetSerializer(result, many=True)  
            return Response({'status': 'success', "snippets":serializers.data}, status=200) 
        return Response({'status': 'fail', "message":"Please login"}, status=200) 
         
    
    
  
    def post(self, request):  
        if request.user.is_authenticated:
            serializer = SnippetSerializer(data=request.data)  
            if serializer.is_valid():  
                serializer.save()  
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
            else:  
                return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
            
        return Response({'status': 'fail', "message":"Please login"}, status=200) 
        
    
        
    def put(self, request, pk, format=None):
        if request.user.is_authenticated:
            snippet = Snippet.objects.get(id=pk) 
            serializer = SnippetSerializer(snippet, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "successfully updated the details", "data": serializer.data}, status=status.HTTP_200_OK)  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
        return Response({'status': 'fail', "message":"Please login"}, status=200)  
    
    def delete(self, request, pk, format=None):
        if request.user.is_authenticated:
            snippet = Snippet.objects.get(id=pk) 
            snippet.delete()
            return Response({"status": "successfully deleted the details", "data": {}}, status=status.HTTP_200_OK) 
        return Response({'status': 'fail', "message":"Please login"}, status=200)  

