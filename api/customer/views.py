from django.db.models.query import InstanceCheckMeta
from api.views import *
from customer.models import Customer
from .serializers import CustomerSerializer

def custom_view(request):
    return HttpResponse("Customer API Called")



class CustomerViewSet(viewsets.ModelViewSet):
    """
    List all books, or create a new book.
    """
    
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


    # def perform_create(self, serializer):

    #     password = self.request.data.get("password")
    #     confirm_password = self.request.data.get("confirm_password")

    #     if password != confirm_password:
    #         data= {"password":"Not match"}
    #         raise serializers.ValidationError(data)

    #     username = self.request.data.get('name')
    #     email = self.request.data.get('email')
    #     password = self.request.data.get('password')
    #     address = self.request.data.get('address')
    #     country = self.request.data.get('country')
    #     image = self.request.data.get('image')
    #     country = self.request.data.get('country')
    #     is_customer = self.request.data.get('is_customer')
    #     if is_customer == "true":
    #         is_customer = True
    #     else:
    #         is_customer=False


    #     is_vendor = self.request.data.get('is_vendor')

    #     if is_vendor == "true":
    #         is_vendor = True
    #     else:
    #         is_vendor=False
    #     user = User.objects.get_or_create(username=username,email=email,password=password)
    #     user[0].set_password(password)
    #     user[0].save()
    #     customer= Customer.objects.get(user=user[0])
        
    #     customer.name = username
    #     customer.address = address
    #     customer.country=country
    #     customer.image = image
    #     customer.email = email
    #     customer.is_customer = is_customer
    #     customer.is_vendor = is_vendor
    #     customer.save()

    # def perform_update(self, serializer):
    #     import pdb;pdb.set_trace()
    #     instance = serializer.save()
    #     customer = Customer.objects.get(pk=instance.id)
       
    #     user = User.objects.get(id=customer.user.id)
    #     user.username = self.request.data.get['name']
    #     user.email =  self.request.data.get['email']
    #     user.save()
    #     instance.save()
    #     return instance