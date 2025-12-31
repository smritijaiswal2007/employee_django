from django.shortcuts import render, redirect  # Import render to display templates, redirect to navigate to another URL
from app.models import Student               # Import Student model to interact with student database
from django.urls import reverse                 # Import reverse to get URL by name
from urllib.parse import urlencode             # Import urlencode to convert data into URL parameters

# Landing page view
def landing(req):
    return render(req, 'landing.html')  # Render the landing page template

# Registration page view
def register(req):
    return render(req, 'register.html')  # Render the registration form template

# Login page view
def login(req):
    return render(req, 'login.html')  # Render the login form template

# Handle registration form submission
def registerdata(req):
    if req.method == 'POST':
        n = req.POST.get('Name')  # Get user name from form
        e = req.POST.get('Email')  # Get user email from form
        c = req.POST.get('Contact')  # Get contact number
        d = req.POST.get('Details')  # Get additional details
        i = req.FILES.get('Image')  # Get uploaded profile image
        p = req.POST.get('Password')  # Get password
        cp = req.POST.get('Confirm_password')  # Get confirm password

        user = Student.objects.filter(Email=e)  # Check if email already exists
        if user:
            message = 'Email already exist'  # Display error message if email exists
            return render(req, 'register.html', {'message': message})
        else:
            if p == cp:  # Validate password and confirm password match
                Student.objects.create(Name=n, Email=e, Contact=c, Details=d, Image=i, Password=p)  # Save new user
                return render(req, 'login.html')  # Redirect to login page
            else:
                message = 'password and confirm password does not match'  # Error if passwords mismatch
                return render(req, 'register.html', {'message': message})

# Handle login form submission
def logindata(req):
    if req.method == 'POST':
        e = req.POST.get('Email')
        p = req.POST.get('Password')

        
        if e=='admin@gmail.com' and p=='12345':
            data={
                'name':'Admin',
                 'email':'admin@gmail.com',
                 'contact':12345,
                 'pass':12345
                       }
            
            
            return render(req,'admindashboard.html',{"data":data})

        else:
              user = Student.objects.filter(Email=e).first()

              if not user:
                 return render(req, 'login.html', {
                'message': 'Email not register'
                })

              if user.Password != p:
                return render(req, 'login.html', {
                'message': 'Email and password not matched'
              })

            #  LOGIN SUCCESS → SESSION CREATE
              req.session['student_id'] = user.id

              return redirect('dashboard')
        
      

# Dashboard page view
def dashboard(req):
    if 'student_id' not in req.session:
        return redirect('login')

    student_id = req.session['student_id']
    userdata = Student.objects.get(id=student_id)

    data = {
        'name': userdata.Name,
        'email': userdata.Email,
        'contact': userdata.Contact,
        'detail': userdata.Details,
        'image': userdata.Image
    }

    return render(req, 'dashboard.html', {'data': data})