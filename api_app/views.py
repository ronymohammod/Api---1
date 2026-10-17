from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from api_app.models import *
from api_app.serializers import *

from rest_framework import status


@api_view(['GET'])
def product_view(request):
    if request.method == 'GET':
       product_data = ProductModel.objects.all()
       serializers=productSerializers(product_data,many = True)
       return Response({
           'success':True,
           'message':'Data Get successfully',
           'data':serializers.data
       })



    if request.method == 'POST':
       serializers=productSerializers(data=request.data)
       if serializers.is_valid():
           serializers.save()
           return Response({
           'success':True,
           'message':'Product Created successfully',
           'data':serializers.data
       })



@api_view(['GET','PUT','DELETE'])    

def product_detail(request,p_id):
    try:
       data = ProductModel.objects.get(id=p_id)
    except:
        return Response({
            'success':False,
            'message':'Product data Not Found',
            'data':[]
        }, status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
     


        serializers_data=productSerializers(data)
        return Response({
            'success':True,
            'message':'Product Get successfully',
            'data':serializers_data.data
        }, status=status.HTTP_200_OK)




    if request.method == 'DELETE':
        try:
            data = ProductModel.objects.get(id=p_id)
        except:
            return Response({
                'success':False,
                'message':'Product data Not Found',
                'data':[]
            }, status=status.HTTP_404_NOT_FOUND)
        data.delete()
        return Response({
                'success':True,
                'message':'Product Delete successfully',
                'data':serializers_data.data
            }, status=status.HTTP_200_OK)



    if request.method == 'PUT':
        serializers_data=productSerializers(data,data = request.data)
        if serializers_data.is_valid():
            serializers_data.save()
            return Response({
                'success':True,
                'message':'Product Updates successfully',
                'data':serializers_data.data
            }, status=status.HTTP_201_CREATED)

        else:
            return Response({
                'success':False,
                'message':serializers_data.errors
                
            }, status=status.HTTP_400_BAD_REQUEST)






        