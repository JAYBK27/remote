from django.shortcuts import render

def Home(request):
    return render(request,'gender_home.html'
                  )


def Boys(request):
    return render(request,'gender_boys.html')


def Girls(request):
    return render(request,'gender_girls.html')