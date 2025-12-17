from django.shortcuts import render

# Create your views here.
def landing(req):
    return render(req,'landing.html')


def login(req):
    return render(req,'login.html')

def login_data(req):
    if req.method=='POST':
        e = req.session.get('email')
        p = req.session.get('password')
        if e =='admin@gmail.com' and p=='admin':
            data = {
                'name':'Admin',
                'contact':9834586756,
                'email':'admin@gmail.com',
                'pass':'admin',
                
            }
            
        
            