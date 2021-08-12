from django.db.models import fields
from django.db.models.query import QuerySet
from pkg_resources import require
from rest_framework import serializers
from django.contrib.auth.models import User
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from customer.models import Customer
#for adding the country field ,, casues it pop error sometime  thats why i added it
from django_countries.serializers import CountryFieldMixin


#Validator Rest Framework, phone_number validate on Account Serializer
from rest_framework.validators import UniqueValidator


class CustomerSerializer(CountryFieldMixin,serializers.ModelSerializer):
    password = serializers.CharField(required=False,style={'input_type': 'password'},
                                      write_only=True)
    confirm_password = serializers.CharField(required=False,style={'input_type': 'password'},
                                      write_only=True)

    # image = serializers.ImageField(require=False)
    class Meta:
        ordering = ['id']
        model = Customer
        fields=['id','name','email','password','confirm_password','address','is_customer','is_vendor','country','image']
     

    def create(self, validated_data,*args, **kwargs):
        
        password = validated_data.get("password")
        confirm_password = validated_data.get("confirm_password")

        if password != confirm_password:
            data= {"password":"Not match"}
            raise serializers.ValidationError(data)

        username = validated_data.get('name')
        email = validated_data.get('email')
        password = validated_data.get('password')
        address = validated_data.get('address')
        country = validated_data.get('country')
        image = validated_data.get('image')
        country = validated_data.get('country')
        is_customer = validated_data.get('is_customer')
        if is_customer == "true":
            is_customer = True
        else:
            is_customer=False


        is_vendor = validated_data.get('is_vendor')

        if is_vendor == "true":
            is_vendor = True
        else:
            is_vendor=False
        user = User.objects.get_or_create(username=username,email=email,password=password)
        user[0].set_password(password)
        user[0].save()
        customer= Customer.objects.get(user=user[0])
        customer.user = user[0]
        customer.save()
        
        customer.name = username
        customer.address = address
        customer.country=country
        customer.image = image
        customer.email = email
        customer.is_customer = is_customer
        customer.is_vendor = is_vendor
        customer.save()

        return customer
     
    

    def update(self, instance, validated_data):
        print("Call the update method")
        instance.name = validated_data.get('name',instance.name)
        instance.email = validated_data.get('email',instance.email)
        instance.address = validated_data.get('address',instance.address)
        instance.is_customer = validated_data.get('is_customer',instance.is_customer)
        instance.is_vendor = validated_data.get('is_vendor',instance.is_vendor)
        instance.country = validated_data.get('country',instance.country)
        instance.image = validated_data.get('image',instance.image)


        user =  User.objects.get(id=instance.user.id)
        user.email = instance.email
        user.username = instance.name
        user.save()
        instance.save()
        return instance
       