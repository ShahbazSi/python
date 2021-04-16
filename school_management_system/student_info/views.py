from django.shortcuts import render
from django.http import request
from .models import Details
from django.core.paginator import Paginator
# Create your views here.
def detail_list(request):
    all_detail=Details.objects.all().order_by('id')  #creating object for model class
    paginator=Paginator(all_detail,2) #creating object for pagignator
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'student/home.html',{'page_obj':page_obj})