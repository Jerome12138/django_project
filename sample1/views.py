from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect


# Create your views here.


def hello(request):
    return HttpResponse('<div>hello</div>')


def login(request):
    # request 包含用户提交的所有信息
    # 获取用户提交方法post,get
    error_msg = ''
    if request.method == 'POST':
        # request.POST包含用户提交的数据字典，以name字段为key
        # user = request.POST['user']   # 不建议使用，不存在时会报错
        user = request.POST.get('user', None)  # 不存在返回none
        pwd = request.POST.get('pwd')
        if user == 'root' and pwd == '123':
            # 跳转外部页面用redirect重定向
            return redirect('/home/')
        else:
            error_msg = '用户名或密码错误'

    # render找到文件打开，读取并返回值，自动到templates文件夹中寻找
    return render(request, 'login.html', {'error_msg': error_msg})


USER_LIST = [
    {'name': 'alex', 'gender': '男', 'email': '213@123.com'},
    {'name': 'seven', 'gender': '男', 'email': '213@123.com'},
    {'name': 'jason', 'gender': '男', 'email': '213@123.com'},
]


def home(request):
    if request.method == 'POST':
        u = request.POST.get('name')
        e = request.POST.get('email')
        g = request.POST.get('gender')
        temp = {'name': u, 'gender': g, 'email': e}
        USER_LIST.append(temp)
    return render(request, 'home.html', {'user_list': USER_LIST})


def user1(request):
    return render(request,'user1.html')

def user2(request):
    return render(request,'user2.html')