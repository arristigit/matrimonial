from django.db.models.fields import files
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from .form import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage # as fs
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    profiles = Profile.objects.all()    
    users = User.objects.all()    

    # for i in profiles:
    #     print('profile id:', i.id)
    # for j in users:
    #     print('user id:', j.id)
     
    dic = {"profiles": profiles, 'users': users}
    return render(request, 'home/index.html', dic)

def register_user(request):   
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        try:
            if not username.isalnum():
                messages.warning(request, " User name should only contain letters and numbers")
                return redirect('/register')

            if User.objects.filter(username=username).first():
                messages.warning(request, 'Username is taken!')
                return redirect('/register')
            
            if User.objects.filter(email=email).first():
                messages.warning(request, 'Email is taken!')
                messages.info(request, 'and Email is taken!')
                return redirect('/register')    
            
            if password != confirmpassword:
                messages.warning(request, 'The Confirm Password not matched with the Password!!')
                return redirect('/register')

            user_obj = User(username=username, first_name=firstname, last_name=lastname, email=email)
            user_obj.set_password(password)
            user_obj.save()
            user = authenticate(username=username, password=password)
            # print("user id:", user.id)
            login(request, user)
            request.session['username'] = username
            # request.session['id'] = user.id
            messages.success(request, 'You have registered & loggged-In succussfully.')
            messages.info(request, 'Please fill your details to display your profile on merishaadi.com')

            # return redirect('/')
            # return redirect(f'/inputdetails.html/{user.id}')
            return redirect('/inputdetails')

        except Exception as e:
            print(e)
    return render(request, 'home/register.html')

def login_user(request):    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.warning(request, 'User not found!')
            return redirect('/login')
        
        user = authenticate(username=username, password=password)
        if user is None:
            messages.warning(request, 'Wrong password!')
            return redirect('/login')

        login(request, user)
        messages.success(request, 'Your are succussfully logged in.')
        return redirect('/')

    return render(request, 'home/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Successfully logged out.")
    return redirect('index')    

def inputdetails(request):
    # id = request.session['id']
    try:
        username = request.session['username']    
    except Exception as e:
        print(e)
        print("Above is exception...")
        messages.info(request, 'Please register yourself firstly!')
        return redirect('/register')


    user = User.objects.filter(username=username).first()

    if request.method == 'POST' and request.FILES['changepic']:
        changepic = request.FILES['changepic']
        fs = FileSystemStorage()
        filename = fs.save(changepic.name, changepic) # Storing image in database with auto generated name:
        url = fs.url(filename)
        
        username = request.POST.get('username')
        age = request.POST.get('age')
        dateofbirth = request.POST.get('dateofbirth')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        address = request.POST.get('address')        
        contact = request.POST.get('contact')
        fathername = request.POST.get('fathername')
        mothername = request.POST.get('mothername')
        fathercontact = request.POST.get('fathercontact')
        qualification = request.POST.get('qualification')
        occupation = request.POST.get('occupation')
        salary = request.POST.get('salary')
        workaddress = request.POST.get('workaddress')
        hobby = request.POST.get('hobby')
        caste = request.POST.get('caste')
        religion = request.POST.get('religion')
        familytype = request.POST.get('familytype')

        user = User.objects.filter(username=username).first()
        firstname = user.first_name
        lastname = user.last_name
        email = user.email

        profile_obj = Profile(user=user, first_name=firstname, last_name=lastname, email=email, gender=gender, age=age, pic=url, date_of_birth=dateofbirth, city=city, address=address,
        phone=contact, father_name=fathername, mother_name=mothername, father_phone=fathercontact, qualification=qualification,
        occupation=occupation, salary=salary, work_address=workaddress, hobby=hobby, caste=caste, religion=religion, family_type=familytype)
        profile_obj.save()
        
        messages.success(request, 'Your details has been succussfully saved.')
        return redirect('/')
    dic = {'user': user}
    return render(request, 'home/inputdetails.html', dic)
    # return render(request, 'home/inputdetails.html')

def profile(request, id):
    print(id)
    try:
        user = User.objects.filter(id=id).first()
        if user is not None:
            profile = Profile.objects.filter(user=user).first()
            dic = {"profile": profile}
            return render(request, 'home/profile.html', dic)

    except Exception as e:
        print(e)
        print("user id is none...:")
    profile = Profile.objects.filter(id=id).first()
    print(profile)
    dic = {"profile": profile}
    return render(request, 'home/profile.html', dic)

@login_required
def editProfile(request, id):      
    if request.method == 'POST' and request.FILES['changepic']:
        changepic = request.FILES['changepic']
        fs = FileSystemStorage()
        filename = fs.save(changepic.name, changepic) # Storing image in database with auto generated name:
        url = fs.url(filename)
        
        userId = request.POST.get('userId')
        # username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        pic = url
        age = request.POST.get('age')
        dateofbirth = request.POST.get('dateofbirth')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        address = request.POST.get('address')
        # email = request.POST.get('email')
        contact = request.POST.get('contact')
        fathername = request.POST.get('fathername')
        mothername = request.POST.get('mothername')
        fathercontact = request.POST.get('fathercontact')
        qualification = request.POST.get('qualification')
        occupation = request.POST.get('occupation')
        salary = request.POST.get('salary')
        workaddress = request.POST.get('workaddress')
        hobby = request.POST.get('hobby')
        caste = request.POST.get('caste')
        religion = request.POST.get('religion')
        familytype = request.POST.get('familytype')
        
        # Update the user's details in Users model:
        user = User.objects.filter(id=userId).first()
        user.first_name = firstname
        user.last_name = lastname
        # user.email = email
        user.save()
        print(user)
        
        # Update the user's details in Profile model:
        profile = Profile.objects.filter(user=user).first()
        profile.first_name = firstname
        profile.last_name = lastname
        profile.pic = pic
        profile.age=age
        profile.date_of_birth=dateofbirth
        profile.gender=gender
        profile.city=city
        profile.address=address
        profile.phone=contact
        profile.father_name=fathername
        profile.mother_name=mothername
        profile.father_phone=fathercontact
        profile.qualification=qualification
        profile.occupation=occupation
        profile.salary=salary
        profile.work_address=workaddress
        profile.hobby=hobby
        profile.caste=caste
        profile.religion=religion
        profile.family_type=familytype
        profile.save()

        messages.success(request, 'Your profile has been succussfully updated.')
        return redirect(f'/profile/{profile.id}')

        # Storing image in database:
        # form = ProfileForm(data=request.POST, files=request.FILES)
        # if form.is_valid():
        #     form.save()
        #     obj = form.instance
            # print(obj)
        #     print("It is if of form.is-valid...")
        #     return render(request,"home/index.html")
        # else:
        #     print("Method is post, but form is not valid")
            
    if request.user.is_authenticated:
        otheruser = User.objects.filter(id=id).first()
        profileuser = Profile.objects.filter(id=id).first()
        logineduser = User.objects.filter(username=request.user).first()
        
        if otheruser != logineduser:
            if profileuser.user == logineduser:
                pass
            else:
                messages.warning(request, "Please don't try to enter into other's areas!!")
                return redirect('/')        
    try:
        user = User.objects.filter(id=id).first()
        # if user
        if user is not None:
            profile = Profile.objects.filter(user=user).first()
            dic = {"profile": profile, "user": user}
            return render(request, 'home/editProfile.html', dic)
    except Exception as e:
        print(e)

    profile = Profile.objects.filter(id=id).first()
    user = User.objects.filter(username=profile.user).first()

    dic = {"profile": profile, "user": user}
    return render(request, 'home/editProfile.html', dic)

# def image(request):
#     if request.method == 'POST':
#         form = ImageForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             obj = form.instance
            
#             print("It is if of form.is-valid...")
#             return render(request,"home/image.html", {"obj":obj})
#         else:
#             print("Method is post, but form is not valid")            

#     else:
#         print("It is else of method.GET")
#         form = ImageForm()
        
#     img = Image.objects.all()
#     dic = {'form': form, 'img': img}
#     return render(request, 'home/image.html', dic)