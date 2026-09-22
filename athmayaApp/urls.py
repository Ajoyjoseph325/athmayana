"""
URL configuration for athmayana project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/ hdghgd
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
  
    path('', views.home, name='home'),
    path('packages/all/<int:category_id>/',views.spiritual_packages,name='spiritual_packages'),
    path('packages/wellness/',  views.wellness_packages,   name='wellness_packages'),
    path('kailash/',            views.kailash_detail,      name='kailash_detail'),
    path('publications/',       views.publications,        name='publications'),
    # path('contact/',            views.contact,             name='contact'),
    path('category/', views.add_category, name='add_category'),
      
    path('books/', views.books, name='books'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    

        
    path('pacakgeadmin/', views.add_packages, name='view_packages'),
    path('add-packages/', views.add_packages, name='add_packages'),
    path('edit-package/<int:id>/',views.edit_package,name='edit_package'),
    path('update-package/<int:id>/',views.update_package,name='update_package'),
    path('delete-package/<int:id>/',views.delete_package,name='delete_package'),
    path('add-category/',                views.add_category,    name='add_category'),
    path('category/delete/<int:pk>/', views.delete_category, name='delete_category'),
    path('packagedetails/<int:id>/', views.kailash_detail, name='kailash_detail'),
    path('addpackagedetails/', views.add_package_details, name='add_package_details'),
    path('packagehighlights/', views.package_highlights, name='package_highlights'),

    # path('addtourhighlights/', views.add_package_highlights, name='add_package_highlights'),
    # path('edithighlight/<int:id>/', views.edit_highlight, name='edit_highlight'),
    # path('deletehighlight/<int:id>/', views.delete_highlight, name='delete_highlight'),
    path('addtourhighlights/', views.add_package_highlights, name='add_package_highlights'),
    path('addtourhighlights/edit/<int:edit_id>/', views.add_package_highlights, name='edit_highlight'),
    path('deletehighlight/<int:id>/', views.delete_highlight, name='delete_highlight'),

    # add package details urls

    path('addpackagedetails/', views.add_package_details, name='add_package_details'),
    path('addpackagedetails/edit/<int:edit_id>/', views.add_package_details, name='edit_package_detail'),
    path('addpackagedetails/delete/<int:id>/', views.delete_package_detail, name='delete_package_detail'),

    # add itneray
    path('addpackageitinerary/', views.add_package_itinerary, name='add_package_itinerary'),
    path('addpackageitinerary/edit/<int:edit_id>/', views.add_package_itinerary, name='edit_package_itinerary'),
    path('addpackageitinerary/delete/<int:id>/', views.delete_package_itinerary, name='delete_package_itinerary'),


    path('backoffice/',views.backoffice,name='backoffice'),
    path('backoffice/logout/', views.admin_logout, name='admin_logout'),


    
  

]
