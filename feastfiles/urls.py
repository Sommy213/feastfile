from django.urls import path
from .views import home,landding,create_blog,register,My_blog, wait_please
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',landding,name='l'),
    path('home',home,name='home'),
    path('post',create_blog,name='post'),
    path('signup.html',register,name='signup'),
    path('my_blog.html',My_blog,name='my_blog'),
    path('wait', wait_please,name='wait')
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)