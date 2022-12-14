from rest_framework.views import APIView
from rest_framework import status,generics
from rest_framework.response import Response
from .models import *
from .serializer import *
from django.http import Http404
from django.shortcuts import get_object_or_404
from datetime import datetime

class ExcelDataViews(APIView):
    def get(self, request):
        adminobj=ExcelUpload.objects.all()
        serializer = ExcelUploadSerializer(adminobj, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExcelUploadSerializer(data = request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            print('Excel_data is saving')
            return Response({"msg":"Data uploaded Successful"},status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response({"msg":"Enter the Required Fields"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, format=None):
        try:
            ExcelUpload.objects.all().delete()
            return Response({"msg":"Database cleaned Successful"},status=status.HTTP_204_NO_CONTENT)
        except :
            return Response({"msg":"Data not found"},status=status.HTTP_400_BAD_REQUEST)

class FrontDeskViews(APIView):
    def get_object(self, pk):
        try:
            return FrontDeskModel.objects.get(pk=pk)
        except FrontDeskModel.DoesNotExist:
            raise Http404

    def get(self, request):
        adminobj=FrontDeskModel.objects.all()
        serializer = FrontDeskSerializer(adminobj, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FrontDeskSerializer(data = request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            print('Frontdesk_data is saving')
            return Response({"msg":"Data updated Successful"},status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request,pk, format=None):
        try:
            FrontDeskModel.objects.get(id=pk).delete()
            return Response({"msg":"Data deleted Successful"},status=status.HTTP_204_NO_CONTENT)
        except :
            return Response({"msg":"Data not found"},status=status.HTTP_400_BAD_REQUEST)

    
class FrontDeskUpdateStatus(generics.RetrieveUpdateDestroyAPIView):
    queryset = FrontDeskModel.objects.all()
    serializer_class = FrontDeskSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)
    
class FrontDeskPatientStatus(generics.RetrieveUpdateAPIView):
    queryset = FrontDeskModel.objects.all()
    serializer_class = FrontDeskActiveSerializer


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DoctorDataViews(APIView):
    def get(self, request):
        adminobj=DoctorData.objects.all()
        serializer = DoctorDataSerializer(adminobj, many=True)
        return Response(serializer.data)

class CalenderApiViews(APIView):
    def get(self, request):
        adminobj=FrontDeskModel.objects.all()
        serializer = CalenderSerializer(adminobj, many=True)
        return Response(serializer.data)

# class CustomCalenderApiViews1(generics.ListAPIView):
#     serializer_class = CalenderDetailSerializer
#     def get_queryset(self):
#         doctor_name = self.kwargs['pk']
#         dos = self.kwargs['lk']
#         date_dos= datetime.strptime(dos,'%d/%m/%Y')
#         print(date_dos)
#         print(date_dos,doctor_name)
#         return FrontDeskModel.objects.filter(Doctor_name = doctor_name,DOS = date_dos)

class TestingEditCalender(generics.ListAPIView):
    serializer_class = CalenderDetailSerializer
    def get_queryset(self):
        dos = self.kwargs['lk']
        return FrontDeskModel.objects.filter(DOS = dos)
        
class CalenderApiViews12(APIView):
    def get(self, request,lk):
        # doctor_name = self.kwargs['pk']
        date_dos = lk
        query=FrontDeskModel.objects.filter(DOS = date_dos)
        total_patient = FrontDeskModel.objects.filter(DOS = date_dos).count()
        patient_not_present = FrontDeskModel.objects.filter(DOS = date_dos).filter(active =False).count()
        patient_present = total_patient - patient_not_present
        Response_data = {}
        k=1
        for dat in query:
            Response_data[k] = {
                'id':k, 'title': f'{dat.Location}-{dat.Doctor_name}-{patient_present}/{total_patient}',
                'date':dat.DOS
                }
            k+=1
        return Response(Response_data)

# from rest_framework import generics
# from rest_framework.views import APIView
# from blog.models import Post
# from .serializers import PostSerializer
# from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
# from rest_framework import viewsets
# from rest_framework import filters
# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
# from rest_framework import filters


# class PostUserWritePermission(BasePermission):
#     message = 'Editing posts is restricted to the author only.'

#     def has_object_permission(self, request, view, obj):

#         if request.method in SAFE_METHODS:
#             return True

#         return obj.author == request.user

# # User Filter
# # class PostList(generics.ListAPIView):
# #     permission_classes = [IsAuthenticated]
# #     serializer_class = PostSerializer
 
# #     def get_queryset(self):
# #         user = self.request.user
# #         return Post.objects.filter(author=user)

# class PostList(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer

#     def get_queryset(self):
#         user = self.request.user
#         return Post.objects.filter(author=user)

# class PostDetail(generics.RetrieveAPIView):
#     serializer_class = PostSerializer

#     def get_queryset(self):
#         slug = self.request.query_params.get('slug', None)
#         print(slug)
#         return Post.objects.filter(slug=slug)

# class PostListDetailfilter(generics.ListAPIView):

#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['^slug']

#     # '^' Starts-with search.
#     # '=' Exact matches.
#     # '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
#     # '$' Regex search.


# class PostSearch(generics.ListAPIView):
#     permission_classes = [AllowAny]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['^slug']

    # def get_object(self, queryset=None, **kwargs):
    #     item = self.kwargs.get('pk')
    #     return get_object_or_404(Post, slug=item)

    # Define Custom Queryset
    # def get_queryset(self):
    #     return Post.objects.all()


# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()

#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)

    # def list(self, request):
    #     pass

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass

    # class PostList(viewsets.ModelViewSet):
    #     permission_classes = [IsAuthenticated]
    #     queryset = Post.postobjects.all()
    #     serializer_class = PostSerializer



""" Concrete View Classes
# CreateAPIView
Used for create-only endpoints.
# ListAPIView
Used for read-only endpoints to represent a collection of model instances.
# RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
# DestroyAPIView
Used for delete-only endpoints for a single model instance.
# UpdateAPIView
Used for update-only endpoints for a single model instance.
# ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
# RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
# RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""