from django.shortcuts import render

# Create your views here.
def love(request):
    return render(request,'love.html')

def love_liqian(request):
        return render(request,'love_liqian.html')
