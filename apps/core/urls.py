from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.asset_list, name='asset_list'),
    path('<int:pk>/', views.asset_detail, name='asset_detail'),
    path('create/', views.asset_create, name='asset_create'),
    path('<int:pk>/edit/', views.asset_edit, name='asset_edit'),
    path('<int:pk>/delete/', views.asset_delete, name='asset_delete'),
    path('export/', views.asset_export, name='asset_export'),
    path('template/', views.asset_template, name='asset_template'),
    path('import/', views.asset_import, name='asset_import'),

    # Excel import detail views
    path('physical/<int:pk>/', views.physicalasset_detail, name='physicalasset_detail'),
    path('physical/<int:pk>/edit/', views.physicalasset_edit, name='physicalasset_edit'),
    path('license/<int:pk>/', views.softwarelicense_detail, name='softwarelicense_detail'),
    path('license/<int:pk>/edit/', views.softwarelicense_edit, name='softwarelicense_edit'),
    path('notebook/<int:pk>/', views.notebooklease_detail, name='notebooklease_detail'),
    path('notebook/<int:pk>/edit/', views.notebooklease_edit, name='notebooklease_edit'),
    path('application/<int:pk>/', views.softwareapplication_detail, name='softwareapplication_detail'),
    path('application/<int:pk>/edit/', views.softwareapplication_edit, name='softwareapplication_edit'),

    # Category
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),

    # Location
    path('locations/', views.location_list, name='location_list'),
    path('locations/create/', views.location_create, name='location_create'),
    path('locations/<int:pk>/edit/', views.location_edit, name='location_edit'),
    path('locations/<int:pk>/delete/', views.location_delete, name='location_delete'),

    # Real-time Activity API
    path('activity/json/', views.asset_activity_json, name='asset_activity_json'),
]
