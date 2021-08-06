from django.urls import path
from .views import home,categor,detel_news

urlpatterns =[
    path('',home,name='home'),
    path('catgor/<int:cate_id>/',categor,name='categor'),
    path('detele_news/<int:new_id>/',detel_news,name='detel_news')
]