from os import name
from django.db.models import fields
from rest_framework import serializers
from rest_framework.decorators import parser_classes
from api.serializers import *
from product.models import Product,ProductCategory,ProductUOM

import base64

from django.core.files.base import ContentFile
from rest_framework import serializers




# class Base64ImageField(serializers.ImageField):
#     def from_native(self, data):
#         if isinstance(data, basestring) and data.startswith('data:image'):
#             # base64 encoded image - decode
#             format, imgstr = data.split(';base64,')  # format ~= data:image/X,
#             ext = format.split('/')[-1]  # guess file extension

#             data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

#         return super(Base64ImageField, self).from_native(data)


from rest_framework import serializers    

# class Base64ImageField(serializers.ImageField):
#     """
#     A Django REST framework field for handling image-uploads through raw post data.
#     It uses base64 for encoding and decoding the contents of the file.

#     Heavily based on
#     https://github.com/tomchristie/django-rest-framework/pull/1268

#     Updated for Django REST framework 3.
#     """

#     def to_internal_value(self, data):
#         from django.core.files.base import ContentFile
#         import base64
#         import six
#         import uuid

#         # Check if this is a base64 string
#         if isinstance(data, six.string_types):
#             import pdb;pdb.set_trace()
#             # Check if the base64 string is in the "data:" format
#             if 'data:' in data and ';base64,' in data:
#                 # Break out the header from the base64 content
#                 header, data = data.split(';base64,')

#             # Try to decode the file. Return validation error if it fails.
#             try:
#                 decoded_file = base64.b64decode(data)
#             except TypeError:
#                 self.fail('invalid_image')

#             # Generate file name:
#             file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
#             # Get the file name extension:
#             file_extension = self.get_file_extension(file_name, decoded_file)

#             complete_file_name = "%s.%s" % (file_name, file_extension, )

#             data = ContentFile(decoded_file, name=complete_file_name)

#         return super(Base64ImageField, self).to_internal_value(data)

#     def get_file_extension(self, file_name, decoded_file):
#         import imghdr

#         extension = imghdr.what(file_name, decoded_file)
#         extension = "jpg" if extension == "jpeg" else extension

#         return extension


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        ordering = ['id']
        model = ProductCategory
        fields = ['name']

class ProductUomSerializer(serializers.ModelSerializer):

    class Meta:
        ordering = ['id']
        model = ProductUOM
        fields = ['name']




class ProductSerializer(serializers.ModelSerializer):
   
    # category = serializers.SerializerMethodField('get_categoryname')
    # uom = serializers.SerializerMethodField('get_uomname')
    category =  ProductCategorySerializer()
    uom = ProductUomSerializer()
    # image = Base64ImageField(
    #     max_length=None, use_url=True,
    # )



   

    class Meta:
        ordering = ['id']
        model = Product
        fields = ['id','name','type','category','uom','slug','image','barcode','sale_price','purchase_price']
    
    # def get_categoryname(self, obj):
    #     name = obj.category.name
    #     return name

    # def get_uomname(self,obj):
    #     name = obj.uom.name
    #     return name

    def create(self, validated_data):
        category = validated_data.get("category")
        uom = validated_data.get("uom")


        try:
            category_obj =  ProductCategory.objects.get(name=category['name'])
        except:
            data = {"category":"There is no category"}
            raise serializers.ValidationError(data)

        
        try:
            uom_obj =  ProductUOM.objects.get(name=uom['name'])
        except:
            data = {"uom":"There is no uom"}
            raise serializers.ValidationError(data)
        

        validated_data["category"] = category_obj
        validated_data["uom"] = uom_obj
       

        return super().create(validated_data)

    def update(self, instance, validated_data):
        category =  validated_data.get("category")
        uom =  validated_data.get("uom")

        try:
            category_obj =  ProductCategory.objects.get(name=category['name'])
        except:
            data = {"category":"There is no category"}
            raise serializers.ValidationError(data)

        
        try:
            uom_obj =  ProductUOM.objects.get(name=uom['name'])
        except:
            data = {"uom":"There is no uom"}
            raise serializers.ValidationError(data)


        instance.name = validated_data.get('name',instance.name)
        instance.type = validated_data.get('type',instance.type)
        instance.slug = validated_data.get('slug',instance.slug)
        instance.image = validated_data.get('image',instance.image)
        instance.barcode = validated_data.get('barcode',instance.barcode)
        instance.sale_price = validated_data.get('sale_price',instance.sale_price)
        instance.purchase_price = validated_data.get('purchase_price',instance.purchase_price)
        instance.category =category_obj
        instance.uom = uom_obj
        instance.save()
        return instance
       
