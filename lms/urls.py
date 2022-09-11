from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from lms import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='library API Documentation')


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user-list/<str:username>', views.getUserList, name='User List'),
    path('overview/',views.apioverview, name='apiOverView'),
    path('book-list/', views.showList, name='Book-list'),
    path('book-details/<int:pk>/', views.ViewBook, name='BookDetails'),
    path('book-add/',views.AddBook, name="AddBook"),
    path('book-update/<int:pk>', views.updateBookDetails, name='UpdateBookDetails'),
    path('book-delete/<int:pk>', views.deleteBook, name='DeleteBook'),
    path('', schema_view)

]