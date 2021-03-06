from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClForm
from .models import Client, Product, Event
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

def main(request):
    return render(request,'main.html')
def base(request):
    return render(request,'base.html')

@login_required(login_url='/login/')
def create(request):
    if request.method == "POST":
        filled_form = ClForm(request.POST)
        if filled_form.is_valid():
            temp_form = filled_form.save(commit=False)
            temp_form.author = request.user
            temp_form.save()
            return redirect('index')
    cl_form = ClForm()
    return render(request, 'create.html', {'cl_form' : cl_form})

@login_required(login_url='/login/')
def detail(request, cl_id):
    my_cl = get_object_or_404(Product, pk=cl_id)
    return render(request, 'detail.html', {'my_cl' : my_cl})

def delete(request, cl_id):
    my_cl = cl.objects.get(pk=cl_id)
    if request.user == my.cl.author:
        my_cl.delete()
        return redirect('index')
    
    raise PermissionDenied

def update(request, cl_id):
    my_cl = Client.objects.get(pk=cl_id)
    cl_form = ClForm(instance=my_cl)
    if request.method == "POST":
        updated_form = ClForm(request.POST, instance=my_cl)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('index')

    return render(request, 'create.html', {'cl_form' : cl_form})

def eventdetail(request, event_id): #views.py의 pk변수명과 urls.py의 변수명은 같아야 함
    event = get_object_or_404(Event, pk = event_id) #모델과 pk를 designer_id라고 부를거야
    return render(request, 'eventdetail.html',{'event':event})
    #값을 보낼거임

def event(request):
    event = Event.objects.all()
    return render(request,'event.html', {'event':event})

def product(request, store_id, menu_id): #product.html
    products = Client.objects.all()
    store = get_object_or_404(Product, pk = product_id)
    product_object = get_object_or_404(Product, pk=product_id)
    product = product_object.menu.split('\r\n')[menu_id - 1].split(':')[0]
    product_quantity = product_object.menu.split('\r\n')[menu_id - 1].split(':')[1]
    total = 0
    for price in products:
        total += price.price
    return render(request,'product.html', {'product':product,'products':products,'product':product,'product_quantity':product_quantity,'total':total})

def payment(request):
    return render(request,'payment.html')

def goods(request):
    return render(request,'goods.html')

def mypage(request):
    return render(request,'mypage.html')