from django.shortcuts import render

# Create your views here.
def love(request):
    return render(request,'love.html')