from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from todo.models import taskModel
from django.contrib import messages
from django.contrib.auth import authenticate,logout, login
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        # print(request.user)
        return redirect("/login")
    
    alltasks = taskModel.objects.filter(user=request.user)
    # print(alltasks)
    # print(request.user)
    # send all tasks to index.html
    context = {'alltasks': alltasks}
    print(context)
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')


def addtask(request):
    if request.method == "POST":
        title = request.POST.get('name')
        completed = False
        created = datetime.now()
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        category = request.POST.get('category')
        description = request.POST.get('desc')
        user = request.user
        task = taskModel(name=title, completed=completed, created=created, due_date=due_date, priority=priority, category=category, description=description, user=user)
        task.save()
        messages.success(request, 'your task is added!')
    return redirect("/")

def delete(request, taskid):
    task = taskModel.objects.get(id=taskid)
    task.delete()
    messages.warning(request, 'your task is deleted!')
    return redirect("/")


def edit(request, taskid):
    if request.method == "POST":
        task = taskModel.objects.get(id=taskid)
        task.name = request.POST.get('name')
        task.completed = False
        task.created = datetime.now()
        task.due_date = request.POST.get('due_date')
        task.priority = request.POST.get('priority')
        task.category = request.POST.get('category')
        task.description = request.POST.get('desc')
        task.save()
        messages.success(request, 'your task is edited!')
        return redirect("/")
    else:
        task = taskModel.objects.get(id=taskid)
        context = {'task': task}
        return render(request,'edit.html',context)


def register(request):
    if(request.method=='POST'):
        username = request.POST['logname']
        email = request.POST['logemail']
        password = request.POST['logpass']
        if(User.objects.filter(username=username).exists()):
            messages.error(request, "username already taken!")
            return render(request,'registerUser.html')
        elif(User.objects.filter(email=email).exists()):
            messages.error(request, "Account with this email already exists.. try logging in!")
            return render(request,'registerUser.html')
        else:
            user = User.objects.create_user(username=username,email=email, password=password)
            user.save()
            print('User Created')
            messages.warning(request, "Created Account successfully!")
            return redirect('/')
    else:
        return render(request,'registerUser.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Logged in !')
            return redirect("/")
        else:
            messages.warning(request, 'Invalid Credentials !')
            return render(request, 'registerUser.html')
    return render(request, 'registerUser.html')

def logoutUser(request):
    logout(request)
    messages.warning(request, 'Logged out !')
    return redirect("/")