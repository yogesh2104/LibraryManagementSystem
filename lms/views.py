from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializers import RegisterSerializer
from rest_framework.decorators import api_view,permission_classes
from .serializers import BookSerializer
from .models import Books
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.


@api_view(['POST'])
def login_api(request):
    serializer=AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user=serializer.validated_data['user']
    _, token= AuthToken.objects.create(user)

    return Response({
        'user_info':{
            'id':user.id,
            'username':user.username,
            'email':user.email
        },
        'token':token
    })

@api_view(['GET'])
def get_user_data(request):
    user=request.user
    if user.is_authenticated:
        return Response({
            'user_info':{
                'id':user.id,
                'username':user.username,
                'email':user.email
            },
        })
    return Response({
        'error':'User not authorized'
    },status=400)



@api_view(['POST'])
def register_api(request):
    serializer=RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user=serializer.save()
    _, token=AuthToken.objects.create(user)

    return Response({
        'user_info':{
            'id':user.id,
            'username':user.username,
            'email':user.email
        },
        'token':token
    })

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
