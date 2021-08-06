from django.urls import path
from .views import add_news, admin_cabinet, delete_news, edite_news, news_detel, sign_in,sign_up,logout_admin

urlpatterns =[
    path('sign_in/',sign_in,name='sign_in'),
    path('sign_up/',sign_up,name='sign_up'),
    path('logout/',logout_admin,name='logout'),
    path('admin_cabinet/',admin_cabinet,name='admin_cabinet'),
    path('add_news/',add_news,name='add_news'),
    path('news_deteil/<int:news_id>/',news_detel,name='news_deteil'),
    path('delete_news/<delete_news_id>/',delete_news,name='delete_news'),
    path('edite_news/<int:edite_news_id>/',edite_news,name='edite_news')
]