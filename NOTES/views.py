from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import HttpResponseRedirect
from datetime import date
from django.contrib.auth.decorators import login_required
import logging
from django.http import HttpResponse, Http404
import os
from django.conf import settings
from .models import UploadedNotes
from .models import Help
from .models import Help


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')

def admin_nav(request):
    return render(request,'admin_nav.html')

def index(request):
     return render(request,'index.html')

def about(request):
     return render(request,'about.html') 

def contact(request):
   return render(request,'contact.html')

def adminlogin(request):
    error=""
    if request.method == 'POST':
        u = request.POST['uname'] 
        p = request.POST['password']
        user = authenticate(username = u, password = p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes" 
    d = {'error': error}
    return render(request, 'adminlogin.html', d)

def adminHome(request):
    if not request.user.is_staff:
        return redirect('adminlogin')
    pn = UploadedNotes.objects.filter(status="Pending").count()
    an = UploadedNotes.objects.filter(status="Accepted").count()
    rn = UploadedNotes.objects.filter(status="Rejected").count()
    alln = UploadedNotes.objects.all().count()
    d = {'pn': pn, 'an': an, 'rn': rn, 'alln':alln}
    return render(request,'adminHome.html',d)

def userlogin(request):
    error=""
    if request.method == 'POST':
        u = request.POST.get('emailID') 
        p = request.POST.get('pwd')
        user = authenticate(username = u, password = p)
        try:
            if not user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes" 
    d = {'error': error}
    return render(request, 'userlogin.html', d)

def Logout(request):
    logout(request)
    return redirect('index')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user = user)
    d = {'data': data,'user': user}
    return render(request,'profile.html',d)

def createaccount(request):
    error=""
    if request.method == 'POST':
        f = request.POST.get('firstname')
        l = request.POST.get('lastname')
        c = request.POST.get('contact')
        e = request.POST.get('emailID')
        r = request.POST.get('role')
        b = request.POST.get('branch')
        p = request.POST.get('password')
        try:
            user = User.objects.create_user(username=e,password=p,first_name=f,last_name=l)
            Signup.objects.create(user=user, contact=c, branch=b,role=r)
            error="no"
        except:  
            error="yes"
    d={'error': error}
    return render(request, 'createaccount.html',d)

def changepassword(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error=""
    if request.method=="POST":
        o = request.POST['old']
        n = request.POST['new']
        c = request.POST['confirm']
        if c==n:
            u = User.objects.get(username=request.user.username)
            u.set_password(n)
            u.save()
            error="no"
        else:
            error="yes"
    d={'error': error}
    return render(request,'changepassword.html', d)

def editprofile(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user = user)
    error= False
    if request.method == 'POST':
        f = request.POST['firstname']
        l = request.POST['lastname']
        c = request.POST['contact']
        b = request.POST['branch']
        r = request.POST['role']
        user.first_name = f
        user.last_name = l
        data.contact = c
        data.branch = b
        data.role = r
        user.save()
        data.save()
        error = True

    d = {'data': data,'user': user, 'error': error}
    return render(request,'editprofile.html',d)


logger = logging.getLogger(__name__)

@login_required  # This decorator ensures that only authenticated users can access this view
def upload_notes(request):
    error = ""
    if request.method == 'POST':
        b = request.POST.get('branch', '').strip()
        s = request.POST.get('subject', '').strip()
        n = request.FILES.get('notesfile')
        f = request.POST.get('filetype', '').strip()
        d = request.POST.get('description', '').strip()

        # Validate that all fields are filled
        if not (b and s and n and f and d):
            error = "All fields are required"
        else:
            error = ""
            try:
                # Get the authenticated user
                u = request.user
                # Create a new Notes object
                UploadedNotes.objects.create(
                    user=u,
                    uploadingdate=date.today(),  
                    branch=b,
                    subject=s,
                    notesfile=n,
                    filetype=f,
                    description=d,
                    status='Pending'
                )
                error = "no"
            except:
                error = "yes"

    # Ensure that the view always returns an HttpResponse
    context = {'error': error}
    return render(request, 'upload_notes.html', context)

logger = logging.getLogger(__name__)

@login_required  # This decorator ensures that only authenticated users can access this view
def adminuploadnotes(request):
    error = ""
    if request.method == 'POST':
        b = request.POST.get('branch', '').strip()
        s = request.POST.get('subject', '').strip()
        n = request.FILES.get('notesfile')
        f = request.POST.get('filetype', '').strip()
        d = request.POST.get('description', '').strip()

        # Validate that all fields are filled
        if not (b and s and n and f and d):
            error = "All fields are required"
        else:
            error = ""
            try:
                # Get the authenticated user
                u = request.user
                # Create a new Notes object
                UploadedNotes.objects.create(
                    user=u,
                    uploadingdate=date.today(),  
                    branch=b,
                    subject=s,
                    notesfile=n,
                    filetype=f,
                    description=d,
                    status='Pending'
                )
                error = "no"
            except:
                error = "yes"

    # Ensure that the view always returns an HttpResponse
    context = {'error': error}
    return render(request, 'adminuploadnotes.html', context)

def view_mynotes(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    user = User.objects.get(id=request.user.id)
    notes = UploadedNotes.objects.filter(user = user)
    
    d = {'notes': notes}
    return render(request,'view_mynotes.html',d)

def delete_mynotes(request,pid):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    notes=UploadedNotes.objects.get(id=pid)
    notes.delete()
    return redirect('view_mynotes')

def delete_usernotes(request,pid):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    notes=UploadedNotes.objects.get(id=pid)
    notes.delete()
    return redirect('view_allnotes')

def view_users(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    users = Signup.objects.all()
    d = {'users': users}
    return render(request,'view_users.html',d)

def delete_users(request,pid):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    user=User.objects.get(id=pid)
    user.delete()
    return redirect('view_users')

def pending_notes(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    notes = UploadedNotes.objects.filter(status="Pending")
    
    d = {'notes': notes}
    return render(request,'pending_notes.html',d)

def accepted_notes(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    notes = UploadedNotes.objects.filter(status="Accepted")
    
    d = {'notes': notes}
    return render(request,'accepted_notes.html',d)

def rejected_notes(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    notes = UploadedNotes.objects.filter(status="Rejected")
    
    d = {'notes': notes}
    return render(request,'rejected_notes.html',d)

def view_allnotes(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    notes = UploadedNotes.objects.all()
    
    d = {'notes': notes}
    return render(request,'view_allnotes.html',d)

def uview_allnotes(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    notes = UploadedNotes.objects.filter(status="Accepted")
    
    d = {'notes': notes}
    return render(request,'uview_allnotes.html',d)

def assign_status(request,pid):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    notes =UploadedNotes.objects.get(id=pid)
    error=""
    if request.method == 'POST':
        s= request.POST.get('status')
        try:
            notes.status = s
            notes.save()
            error= "no"
        except:
            error= "yes"
    d= {'notes': notes,'error': error}
    return render(request,'assign_status.html',d)

def help(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    help = Help.objects.all()
    
    d = {'help': help}
    return render(request,'help.html',d)


def contact(request):
    error = False
    if request.method == 'POST':
        e = request.POST.get('email', '').strip()
        s = request.POST.get('subject', '').strip()
        m = request.POST.get('message', '').strip()

        if not (e and s and m):
            error = "All fields are required"
            
        else:
                Help.objects.create(
                    uploadingdate=date.today(),
                    email=e,
                    subject=s,
                    message=m
                )
                error = True
    context = {'error': error}
    return render(request, 'contact.html', context)

def download_file(filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    else:
        raise Http404("File not found")