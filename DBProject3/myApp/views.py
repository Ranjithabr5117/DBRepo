from django.shortcuts import render
from myApp.models import Customer
# Create your views here.
def view1(request):
    c=Customer.objects.all()
    c1={'cust':c}
    return render(request,'myApp/1.html',c1)
