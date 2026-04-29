""" from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pos_app.models import TableResto
from api.serializers import TableRestoSerializer

class TableRestoListApiView(APIView):

    def get(self, request):
        data = TableResto.objects.all()
        serializer = TableRestoSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TableRestoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
class TableRestoDetailApiView(APIView):

    def get_object(self, id):
        try:
            return TableResto.objects.get(id=id)
        except TableResto.DoesNotExist:
            return None

    def get(self, request, id, *args, **kwargs):
        table_resto = self.get_object(id)
        if not table_resto:
            return Response({
                'status': 400,
                'message': 'Data does not exists...',
                'data': {}
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = TableRestoSerializer(table_resto)
        return Response({
            'status': 200,
            'message': 'Data retrieve successfully...',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def put(self, request, id, *args, **kwargs):
        table_resto = self.get_object(id)
        if not table_resto:
            return Response({
                'status': 400,
                'message': 'Data does not exists...',
                'data': {}
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = TableRestoSerializer(
            instance=table_resto,
            data=request.data,
            partial=True
        )
        #disini ak ubah supaya pas put/update, hanya field yg dimasuin di body json aja yg di edit
        #jadi g perlu masuin semua field, cukup field yg mau di edit aja yg dimasuin di body jsonnya
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 200,
                'message': 'Data updated successfully...',
                'data': serializer.data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        table_resto = self.get_object(id)
        if not table_resto:
            return Response({
                'status': 400,
                'message': 'Data does not exists...',
                'data': {}
            }, status=status.HTTP_400_BAD_REQUEST)

        table_resto.delete()
        return Response({
            'status': 200,
            'message': 'Data deleted successfully...'
        }, status=status.HTTP_200_OK) """

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from api.serializers import RegisterSerializer
from api.serializers import LoginSerializer
from pos_app.models import MenuResto
from api.serializers import MenuRestoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from api.paginators import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

#untuk buat endpoint register, buat bikin akun admin
class RegisterUserAPIView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'status': status.HTTP_201_CREATED,
                'message': 'Selamat anda telah terdaftar...',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
#untuk buat endpoint login, buat login admin, dan dikasi token auth
class LoginUserAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Login berhasil',
                'data': {
                    'token': serializer.validated_data['token']
                }
            }, status=status.HTTP_200_OK)

        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    

#untuk buat endpoint menu resto, buat nampilin data menu resto, endpoint ini butuh authentication, jadi harus login dulu baru bisa akses endpoint ini, dan pas login berhasil bakal ngasih token, terus token itu yang dipake buat akses endpoint ini, cukup masukin tokennya aja di header authorizationnya, dengan format "Token <tokennya>"
class MenuRestoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = MenuResto.objects.all()
        serializer = MenuRestoSerializer(data, many=True)
        return Response({
            'status': 200,
            'data': serializer.data
        })

#pagination    
class MenuRestoFilterApi(generics.ListAPIView):
    queryset = MenuResto.objects.all()
    serializer_class = MenuRestoSerializer
    pagination_class = CustomPagination
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['category__name'] #Django pakai double underscore (__) untuk “menyebrang relasi”
    #in case u asking, y double underscore
    ordering_fields = ['created_on']