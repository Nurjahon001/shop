from django.urls import path
# from .views import get_list_phone,get_phone_info
from .views import ListPhone,PhoneDetail
urlpatterns=[
    # path('',get_list_phone,name='list-phone'),
    # path('<int:pk>/', get_phone_info, name='detail-phone')
    path('',ListPhone.as_view(),name='list-phone'),
    path('<int:pk>/', PhoneDetail.as_view(), name='detail-phone')

]