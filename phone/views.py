from django.http import Http404
from django.shortcuts import render,get_object_or_404
from .models import Phone
from django.views.generic import TemplateView,DetailView,ListView
# Create your views here.
# def get_list_phone(request):
#     phones=Phone.objects.all()
#     context={
#         'phones':phones
#     }
#     return  render(request,'list.html',context=context)
# def get_phone_info(request,pk):
#     # phone=get_object_or_404(Phone,pk)
#     # context={'phone':phone}
#     # return render(request,'detail.html',context=context)
#
#     try:
#         phone=Phone.objects.get(id=pk)
#         context={'phone':phone}
#     except Exception as e:
#         raise  Http404
#     return  render(request,'detail.html',context=context)

class ListPhone(ListView):
    model = Phone
    template_name = 'list.html'
    context_object_name = 'phones'

class PhoneDetail(DetailView):
    model=Phone
    template_name = 'detail.html'