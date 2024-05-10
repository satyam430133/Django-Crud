from django.shortcuts import render,redirect,HttpResponse
from .models import InfoModel
from .forms import StudentForm
# Create your views here.

def Home(request):
    context = {}
    context['form'] = StudentForm
    return render(request,'index.html',context)

def Registration(request):
    try:
        if request.method == 'POST':
            Names = request.POST.get('Name')
            Phones = request.POST.get('Phone')
            createData = InfoModel.objects.create(Name=Names,Phone=Phones)
            return redirect('index')
        else:
            return redirect('index')
    except:
        return HttpResponse('CODE ERROR')
    
def ShowData(request):
    try:
        alldata = InfoModel.objects.all()
        data = {
            'alldata':alldata
        }
        return render(request,'show.html',data) 
    except:
        return HttpResponse('CODE ERROR')
    
def EditData(request,pk):
    # try:  
        updtt = InfoModel.objects.get(pk=pk)
        context = {}
        context['form'] = StudentForm
        return render(request,'update.html',context,{'updtt':updtt})    
    # except:
    #     return HttpResponse('CODE ERROR')

def UpdateData(request,pk):
    try:
        updtt = InfoModel.objects.get(id=pk)
        if request.method == 'POST':
            Names = request.POST.get('Name')
            Phones = request.POST.get('Phone')
            updtt.update(Name=Names,Phone=Phones)
            return redirect('update',pk=pk)
    except:
        return HttpResponse('CODE ERROR')
    
def DeleteData(reuqest,pk):
    try:
        Delt = InfoModel.objects.filter(id=pk)
        Delt.delete()
        return redirect('showdata')
    except:
        return HttpResponse('CODE ERROR')