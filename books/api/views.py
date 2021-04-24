from rest_framework.response import Response
from rest_framework import status
from books.models import Book
from .serializers import BookSerializer , UserSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import api_view, permission_classes


class IsViewer(BasePermission):
    def has_permission(self , request , view):
        return request.user.has_perm("books.view_book")


@api_view(['POST'])
def api_signup(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(data={
            "success":True,
            "message":"User has been registered"
            },
            status=status.HTTP_201_CREATED
            )  
        
        return Response(data={

        "success":False,
        "errors":serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
        )   
     
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    books = Book.objects.all()
    serializer = BookSerializer(instance=books, many=True)

    return Response(data=serializer.data,status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show(request , id):
    book = Book.objects.get(pk=id)
    serializer = BookSerializer(instance=book)

    return Response(data=serializer.data,status=status.HTTP_200_OK)

    
@api_view(['POST',])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success":True,
            "message":"Book has been created"
        },
        status=status.HTTP_201_CREATED
        )
    return Response(data={

        "success":False,
        "errors":serializer.errors
    },
    status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['PUT',])
@permission_classes([IsAuthenticated])
def edit(request, id):
    book = Book.objects.get(pk=id)
    serializer = BookSerializer(data=request.data , instance=book)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success":True,
            "message":"Book has been updated"
        },
        status=status.HTTP_201_CREATED
        )
    return Response(data={

        "success":False,
        "errors":serializer.errors
    },
    status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request , id):
    book = Book.objects.get(pk=id)
    serializer = BookSerializer(instance=book)
    book.delete()

    return Response(data=serializer.data,status=status.HTTP_200_OK)

