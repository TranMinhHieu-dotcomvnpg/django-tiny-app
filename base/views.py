from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants as messages
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Task
from . forms import TaskForm

# Create your views here.
@login_required
def home(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            logout(request) 
            messages.success(request, 'Logout Successful')
            return redirect('registration/login.html')
    else:
        return render(request,"home.html",{})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('base:login')
    else:
        form = UserCreationForm()
    return render(request,"registration/signup.html",{"form":form})

def user_logout(request):
    logout(request)
    messages.SUCCESS(request,("Log out successfull"))
    return redirect("home")
 # Đảm bảo chỉ user đã đăng nhập mới có thể truy cập
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task(request):
    form = TaskForm()
    tasks = Task.objects.all() # Sắp xếp task theo ID mới nhất

    # Phân trang: mỗi trang có 10 task
    paginator = Paginator(tasks, 3)  
    page_number = request.GET.get('page')  # Lấy số trang từ URL
    page_obj = paginator.get_page(page_number)  # Lấy dữ liệu trang hiện tại

    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('/task/')  # Reload lại trang sau khi thêm Task

    context = {'page_obj': page_obj, 'TaskForm': form}
    return render(request, 'tasks.html', context)  # Trả về trang `tasks.html`



def custom_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("home.html")  # Điều hướng đến trang chính
            else:
                messages.error(request, "Tài khoản của bạn đã bị khóa.")
        else:
            messages.error(request, "Sai tên đăng nhập hoặc mật khẩu.")

    return render(request, "templates/login.html")



def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/task/')
    # Truyền dữ liệu vào context
    context = {'TaskForm':form}
    # Render template và trả về response
    return render(request, 'update_task.html', context)       

# xoa cac task da them
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        
        task.delete()

        return redirect('/task/')
    
    context = {'task':task}

    return render(request,'delete_task.html', context)

