from rest_framework import serializers
from .models import Product,Category,Book
from django.contrib.auth.models import User






class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password',]
        
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user   

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password',]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        #fields = ['name','price']
        #exclude = ['id']
        
    def validate(self, data):
        
        if data['name']:
            for i in data['name']:
                if i.isdigit():
                    raise serializers.ValidationError({'error':'name cant not be a number'})
        
        if data['price']<=100:
            raise serializers.ValidationError({'error':'price must be between 100 and 10000'})
                    
        
        return data
    
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']
            
  
class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'       
        depth = 1     