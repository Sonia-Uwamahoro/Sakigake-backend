# from rest_framework import generics, permissions
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response
# from rest_framework import serializers
# from rest_framework.views import APIView
# from rest_framework import status
# from django.contrib.auth import authenticate, login
# from .models import School, Teacher, Parent
# from .serializers import   ParentRegistrationSerializer, ParentSerializer, SchoolSerializer, TeacherRegistrationSerializer
# # TeacherRegistrationSerializer

# # TeacherSerializer
# from rest_framework.views import APIView

# class SignupView(APIView):
#     def post(self, request):
#         serializer = SchoolSerializer(data=request.data)
#         if serializer.is_valid():
#             school = serializer.save()
#             return Response("School registered successfully.", status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginView(APIView):
#     def post(self, request):
#         school_name = request.data.get('school_name')
#         password = request.data.get('password')

#         try:
#             school = School.objects.get(school_name=school_name)
#         except School.DoesNotExist:
#             return Response("Invalid school name.", status=status.HTTP_400_BAD_REQUEST)

#         if school.create_password != password:
#             return Response("Invalid password.", status=status.HTTP_400_BAD_REQUEST)

       
#         return Response("Successfully logged in.", status=status.HTTP_200_OK)

# class SignoutView(APIView):
#     def post(self, request):
      
#         return Response("Successfully signed out.", status=status.HTTP_200_OK)

# class SchoolListView(APIView):
#     def get(self, request):
#         schools = School.objects.all()
#         serializer = SchoolSerializer(schools, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# class SchoolDetailView(APIView):
#     def get(self, request, pk):
#         try:
#             school = School.objects.get(pk=pk)
#         except School.DoesNotExist:
#             return Response("School not found.", status=status.HTTP_404_NOT_FOUND)

#         serializer = SchoolSerializer(school)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         try:
#             school = School.objects.get(pk=pk)
#         except School.DoesNotExist:
#             return Response("School not found.", status=status.HTTP_404_NOT_FOUND)

#         serializer = SchoolSerializer(school, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response("School updated successfully.", status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         try:
#             school = School.objects.get(pk=pk)
#         except School.DoesNotExist:
#             return Response("School not found.", status=status.HTTP_404_NOT_FOUND)

#         school.delete()
#         return Response("School deleted successfully.", status=status.HTTP_204_NO_CONTENT)

# class ParentRegistrationView(APIView):
#     def post(self, request, school_id):
#         try:
#             school = School.objects.get(id=school_id)
#         except School.DoesNotExist:
#             return Response("Invalid school ID.", status=status.HTTP_400_BAD_REQUEST)
        
#         serializer = ParentSerializer(data=request.data)
#         if serializer.is_valid():
#             parent = serializer.save(school=school)
#             response_data = {
#                 "message": "Parent  registered successfully.",
#                 "school_name": school.school_name,
#                 "parent_email": parent.email_address
#             }
#             return Response(response_data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ParentLoginSerializer(serializers.Serializer):
#     phone_number = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, attrs):
#         phone_number = attrs.get('phone_number')
#         password = attrs.get('password')

#         if phone_number and password:
#             parent = Parent.objects.filter(phone_number=phone_number).first()

#             if not parent:
#                 raise serializers.ValidationError("Invalid phone number or password.")

#             if not parent.check_password(password):
#                 raise serializers.ValidationError("Invalid phone number or password.")
#         else:
#             raise serializers.ValidationError("Phone number and password are required.")

#         return attrs



# class ParentRegistrationView(APIView):
#     def post(self, request, school_id):
#         try:
#             school = School.objects.get(id=school_id)
#         except School.DoesNotExist:
#             return Response("Invalid school ID.", status=status.HTTP_400_BAD_REQUEST)
        
#         serializer = ParentRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             parent = serializer.save(school=school)
#             response_data = {
#                 "message": "Parent registered successfully.",
#                 "school_name": school.school_name,
#                 "parent_email": parent.email_address
#             }
#             return Response(response_data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class TeacherRegistrationView(APIView):
#     def post(self, request, school_id):
#         try:
#             school = School.objects.get(id=school_id)
#         except School.DoesNotExist:
#             return Response("Invalid school ID.", status=status.HTTP_400_BAD_REQUEST)
        
#         serializer = TeacherRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             teacher = serializer.save(school=school)
#             response_data = {
#                 "message": "Teacher registered successfully.",
#                 "school_name": school.school_name,
#                 "teacher_email": teacher.email_address
#             }
#             return Response(response_data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ParentLoginView(APIView):
#     def post(self, request):
#         serializer = ParentLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             phone_number = serializer.validated_data['phone_number']
#             password = serializer.validated_data['password']
#             parent = authenticate(request, phone_number=phone_number, password=password)
#             if parent is not None:
#                 login(request, parent)
#                 return Response("Parent logged in successfully.", status=status.HTTP_200_OK)
#             else:
#                 return Response("Invalid phone number or password.", status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     



from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from .models import School, Teacher, Parent
from .serializers import (
    # ParentLoginSerializer,
    # ParentRegistrationSerializer,
    # ParentSerializer,
    SchoolSerializer,
    TeacherLoginSerializer,
    # TeacherRegistrationSerializer,
   
)

class SignupView(APIView):
    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            school = serializer.save()
            return Response("School registered successfully.", status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        school_name = request.data.get('school_name')
        password = request.data.get('password')

        try:
            school = School.objects.get(school_name=school_name)
        except School.DoesNotExist:
            return Response("Invalid school name.", status=status.HTTP_400_BAD_REQUEST)

        if school.create_password != password:
            return Response("Invalid password.", status=status.HTTP_400_BAD_REQUEST)

        return Response("Successfully logged in.", status=status.HTTP_200_OK)

class SignoutView(APIView):
    def post(self, request):
        logout(request)
        return Response("Successfully signed out.", status=status.HTTP_200_OK)

class SchoolListView(APIView):
    def get(self, request):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SchoolDetailView(APIView):
    def get(self, request, pk):
        try:
            school = School.objects.get(pk=pk)
        except School.DoesNotExist:
            return Response("School not found.", status=status.HTTP_404_NOT_FOUND)

        serializer = SchoolSerializer(school)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            school = School.objects.get(pk=pk)
        except School.DoesNotExist:
            return Response("School not found.", status=status.HTTP_404_NOT_FOUND)

        serializer = SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("School updated successfully.", status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            school = School.objects.get(pk=pk)
        except School.DoesNotExist:
            return Response("School not found.", status=status.HTTP_404_NOT_FOUND)

        school.delete()
        return Response("School deleted successfully.", status=status.HTTP_204_NO_CONTENT)

# class ParentRegistrationView(APIView):
#     def post(self, request, school_id):
#         try:
#             school = School.objects.get(id=school_id)
#         except School.DoesNotExist:
#             return Response("Invalid school ID.", status=status.HTTP_400_BAD_REQUEST)

#         serializer = ParentRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             parent = serializer.save(school=school)
#             response_data = {
#                 "message": "Parent registered successfully.",
#                 "school_name": school.school_name,
#                 "parent_email": parent.email_address
#             }
#             return Response(response_data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TeacherRegistrationView(APIView):
#     def post(self, request, school_id):
#         try:
#             school = School.objects.get(id=school_id)
#         except School.DoesNotExist:
#             return Response("Invalid school ID.", status=status.HTTP_400_BAD_REQUEST)

#         serializer = TeacherRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             teacher = serializer.save(school=school)
#             response_data = {
#                 "message": "Teacher registered successfully.",
#                 "school_name": school.school_name,
#                 "teacher_email": teacher.email_address
#             }
#             return Response(response_data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    ParentRegistrationSerializer,
    TeacherRegistrationSerializer,
    ParentLoginSerializer,
    TeacherLoginSerializer,
)

# Parent registration API
class ParentRegistrationView(APIView):
    def post(self, request, school_id):
        try:
            school = School.objects.get(id=school_id)
        except School.DoesNotExist:
            return Response("Invalid school ID.", status=status.HTTP_400_BAD_REQUEST)

        serializer = ParentRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            parent = serializer.save(school=school)
            response_data = {
                "message": "Parent registered successfully.",
                "school_name": school.school_name,
                "parent_email": parent.email_address
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Teacher registration API
class TeacherRegistrationView(APIView):
    def post(self, request, school_id):
        try:
            school = School.objects.get(id=school_id)
        except School.DoesNotExist:
            return Response("Invalid school ID.", status=status.HTTP_400_BAD_REQUEST)

        serializer = TeacherRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            teacher = serializer.save(school=school)
            response_data = {
                "message": "Teacher registered successfully.",
                "school_name": school.school_name,
                "teacher_email": teacher.email_address
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ParentLoginView(APIView):
    def post(self, request):
        serializer = ParentLoginSerializer(data=request.data)
        if serializer.is_valid():
            response_data = {
                "message": "Parent logged in successfully."
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherLoginView(APIView):
    def post(self, request):
        serializer = TeacherLoginSerializer(data=request.data)
        if serializer.is_valid():
           
            response_data = {
                "message": "Teacher logged in successfully."
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

class ParentLogoutView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response("Parent logged out successfully.", status=status.HTTP_200_OK)
    
class TeacherLogoutView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response("Teacher logged out successfully.", status=status.HTTP_200_OK)