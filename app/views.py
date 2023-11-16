from django.shortcuts import render

# Create your views here.
def data_render(request):
    data = 'This data we are assuming that we are taking the data from the data base'
    d = {'assumption': data}
    return render(request,'data_render.html',context=d)