from django.shortcuts import render,redirect,HttpResponse
from .models import InfoModel
from .forms import StudentForm
# Create your views here.


def Home(request):
    return render(request,'home.html')

def Registration(request):
    try:
        if request.method == 'POST':
            Names = request.POST.get('name')
            Phones = request.POST.get('phone')
            createData = InfoModel.objects.create(Name=Names,Phone=Phones)
            return redirect('home')
        else:
            return redirect('home')
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
    
def EditData(request, pk):
    try:
        gettt = InfoModel.objects.get(id=pk)
        return render(request, 'update.html', {'gettt':gettt})
    except InfoModel.DoesNotExist:
        return HttpResponse('CODE ERROR')

def UpdateData(request, pk):
    try:
        settt = InfoModel.objects.get(id=pk)
        settt.Name = request.POST.get('name')
        settt.Phone = request.POST.get('phone')
        settt.save()
        return redirect('showdata')
    except InfoModel.DoesNotExist:
        return HttpResponse('CODE ERROR')
    
def DeleteData(reuqest,pk):
    try:
        Delt = InfoModel.objects.filter(id=pk)
        Delt.delete()
        return redirect('showdata')
    except:
        return HttpResponse('CODE ERROR')
    
def SearchData(request):
    try:
        Names = request.POST.get('names') 
        srch = InfoModel.objects.filter(Name__icontains=Names)
        return render(request,'result.html',{'srch':srch})
    except:
        return HttpResponse('CODE ERROR')