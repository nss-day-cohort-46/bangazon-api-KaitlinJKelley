from django.core.checks.messages import Error
from rest_framework import serializers, status
from rest_framework.response import Response
from bangazonapi.models import Product, ProductRating, Customer
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ProductRatings(ViewSet):    
    def create(self, request):
        
        try:
            product_rating = ProductRating()
            product_rating.customer = Customer.objects.get(pk=request.data["customer_id"])
            product_rating.product = Product.objects.get(pk=request.data["product_id"])
            product_rating.rating = request.data["rating"]

            product_rating.save()

            serializer = ProductRatingSerializer(product_rating, context={'request': request})

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as ex:
            return Response({ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

class ProductRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductRating
        fields = '__all__'
    
    

