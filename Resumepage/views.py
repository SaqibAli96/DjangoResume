from django.shortcuts import render





def index(request):
    return render(request,'index.html')

def interpreted(request):
        return render(request,'indexMod.html')

