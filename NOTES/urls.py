from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import download_file


urlpatterns = [
    path('', views.index,name='index' ),
    path('home', views.home,name='home' ),
    path('index', views.index,name='index' ),
    path('adminlogin', views.adminlogin,name='adminlogin' ),
    path('admin_nav', views.admin_nav,name='admin_nav' ),
    path('createaccount', views.createaccount,name='createaccount' ),
    path('userlogin', views.userlogin,name='userlogin' ),
    path('about', views.about,name='about' ),
    path('contact', views.contact,name='contact' ),
    path('profile', views.profile,name='profile' ),
    path('Logout', views.Logout,name='Logout'),
    path('adminHome', views.adminHome,name='adminHome'),
    path('profile', views.profile,name='profile'),
    path('changepassword', views.changepassword,name='changepassword'), 
    path('editprofile', views.editprofile,name='editprofile'),
    path('upload_notes', views.upload_notes,name='upload_notes'),
    path('adminuploadnotes', views.adminuploadnotes,name='adminuploadnotes'),
    path('view_mynotes', views.view_mynotes,name='view_mynotes'),
    path('delete_mynotes/<int:pid>', views.delete_mynotes,name='delete_mynotes'),
    path('delete_usernotes/<int:pid>', views.delete_usernotes,name='delete_usernotes'),
    path('view_users', views.view_users,name='view_users'),
    path('delete_users/<int:pid>', views.delete_users,name='delete_users'),
    path('pending_notes', views.pending_notes,name='pending_notes'),
    path('accepted_notes', views.accepted_notes,name='accepted_notes'),
    path('rejected_notes', views.rejected_notes,name='rejected_notes'),
    path('view_allnotes', views.view_allnotes,name='view_allnotes'),
    path('uview_allnotes', views.uview_allnotes,name='uview_allnotes'),
    path('help', views.help,name='help'),
    path('assign_status/<int:pid>/',views.assign_status,name='assign_status'),
    path('download/<str:filename>/', views.download_file, name='download_file'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)