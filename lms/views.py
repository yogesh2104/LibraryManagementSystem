
# Create your views here.
from rest_framework import viewsets,serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .serializers import BookSerializer
from .models import Books


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    class Meta:
        model= User
        fields=['id','username','email','password','is_staff']


        def create(self,validated_data):
            user=User.objects.create(
                username=validated_data["username"],
                email=validated_data["email"]
                )
            user.set_password(validated_data["password"])
            user.save()
            return user

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer


class UserViewViewSet(viewsets.ModelViewSet):
    """
    UserModel View.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


@api_view(['GET'])
def getUserList(request, username):
    user=User.objects.get(username=username)
    serializer=UserSerializer(user, many=False)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def apioverview(request):
    # permission_classes=(IsAuthenticated,)
    api_url={
        'List':'/book-list',
        'Details View':'/book-details/<int:id>',
        'Add Book':'/book-add/',
        'Update':'/book-update/<int:id>',
        'Dalete':'/book-detete/<int:id>',
        'Documantation':'/doc'
    }
    return Response(api_url)

@api_view(['GET'])
@permission_classes((IsAuthenticated,IsAdminUser))
def showList(request):
    bookList=Books.objects.all()
    serializers=BookSerializer(bookList, many=True)
    return Response(serializers.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated,IsAdminUser))
def ViewBook(request, pk):
    book=Books.objects.get(id=pk)
    serializers=BookSerializer(book,many=False)
    return Response(serializers.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated,IsAdminUser))
def AddBook(request):
    serializer=BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser))
def updateBookDetails(request, pk):
    book=Books.objects.get(id=pk)
    serializer=BookSerializer(instance=book, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated, IsAdminUser))
def deleteBook(request, pk):
    book=Books.objects.get(id=pk)
    book.delete()
    return Response('Book Deleted successfully!')
