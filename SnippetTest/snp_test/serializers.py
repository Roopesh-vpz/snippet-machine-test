from rest_framework import serializers  
from .models import Snippet 
from django.contrib.auth.models import User,Group,Permission


  
class SnippetSerializer(serializers.ModelSerializer):  
    title = serializers.CharField(max_length=200, required=True)  
    created_on = serializers.DateField() 
    name=serializers.SerializerMethodField()
    tag_name=serializers.SerializerMethodField()
    
    
    
    
    def get_name(self, obj):

            try:                              
                name = obj.created_by_id.first_name+" "+obj.created_by_id.last_name
                
                return name
            except:
                return "NA"
            
    def get_tag_name(self, obj):

            try:                              
                name = obj.tag.title
                
                return name
            except:
                return "NA"
     
    
    class Meta:  
        model = Snippet  
        # fields = ('created_on','name','title','tag_name')  
        fields=('__all__')
        
        
  
    def create(self, validated_data):  
        """ 
        Create and return a new `Snippet` instance, given the validated data. 
        """  
        return Snippet.objects.create(**validated_data)  
  
    def update(self, instance, validated_data):  
        """ 
        Update and return an existing `Snippet` instance, given the validated data. 
        """  
        
        instance.title = validated_data.get('title', instance.title)  
        
        instance.created_on = validated_data.get('created_on', instance.created_on)  
        instance.created_by_id = validated_data.get('created_by_id', instance.created_by_id)  
        instance.tag = validated_data.get('tag', instance.tag)  
  
        instance.save()  
        return instance  