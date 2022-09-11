from django.urls import path
from . import views
from knox import views as knox_views

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='library API')


urlpatterns=[
    path('login/', views.login_api),
    path('user/', views.get_user_data),
    path('register/', views.register_api),
    path('logout/', knox_views.LoginView.as_view()),
    path('overview/',views.apioverview, name='apiOverView'),
    path('book-list/', views.showList, name='Book-list'),
    path('book-details/<int:pk>/', views.ViewBook, name='BookDetails'),
    path('book-add/',views.AddBook, name="AddBook"),
    path('book-update/<int:pk>', views.updateBookDetails, name='UpdateBookDetails'),
    path('book-delete/<int:pk>', views.deleteBook, name='DeleteBook'),
    path('doc/', schema_view)
]