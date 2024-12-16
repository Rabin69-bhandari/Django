from django.shortcuts import render
from .models import products,Contact,Orders,order_update
from math import ceil
import json
from django.http import HttpResponse

def index(request):
    allprod=[]
    catprods = products.objects.values('product_category','product_id')
    print(catprods)
    uniqueprods = {items['product_category'] for items in catprods}
    print(uniqueprods)
    for category in uniqueprods:
        product = products.objects.filter(product_category=category)
        n = len(product)
        nslides = n //4 + ceil((n/4)-n//4) 
        allprod.append([product,range(1,n),nslides])

    params = {'allprod':allprod}
        
    
    return render(request, 'shop/index.html',params)

def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        message = request.POST.get('message','')
        contact = Contact(name=name,email=email,phone=phone,message=message)
        contact.save()
        thank = True
    return render(request, 'shop/contact.html',{'thank':thank})

def about(request):
    return render(request, 'shop/about.html')

def tracker(request):
    if request.method=="POST":
        order_id = request.POST.get('orderid','')
        email = request.POST.get('email','')
        try:
            order = Orders.objects.filter(order_id=order_id,email=email)
            if len(order)>0:
                update = order_update.objects.filter(order_id=order_id)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response = json.dumps([updates,order[0].items_json],default=str)
                return HttpResponse(response)
            else:
                 return HttpResponse('{}')
        except Exception as e:
             return HttpResponse('{}')
    return render(request, 'shop/tracker.html')

def checkout(request):
    thank = False
    id = 0
    if request.method=="POST":
        items_json = request.POST.get('itemsJson','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip = request.POST.get('zip','')
        print(items_json)
        order = Orders(items_json=items_json,name=name,email=email,phone=phone,city = city,States=state,ZIP_State=zip)
        order.save()
        update = order_update(order_id = order.order_id,update_desc="The Order Has Been Placed")
        update.save()
        id = order.order_id
        thank = True
    return render(request, 'shop/checkout.html',{'thanks':thank,'id':id})