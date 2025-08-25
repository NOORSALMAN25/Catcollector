from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('about/', views.about , name='about'),
    path('cats/', views.cats_index, name='index'),
    path('cats/<int:cat_id>/',views.cats_detail,name='detail'),


    #CBV's
    path('cats/create/' , views.CatCreate.as_view() , name='cats_create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view() , name='cats_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view() , name='cats_delete'),


    #Normal path
    path('cats/<int:cat_id>/add_feeding' , views.add_feeding, name='add_feeding'), #19

    #2-4  // CBV's for the Toys model
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),

    #2-16 Associate a Toy with a Cat (M:M)
    path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    # Unassociate a Toy from a Cat (M:M)
    path('cats/<int:cat_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),

    #3-8 // signup
    path('accounts/signup' , views.Signup , name='signup'),

]
