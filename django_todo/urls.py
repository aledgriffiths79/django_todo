"""django_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# add functions from the views.py file here:
from todo.views import get_todo_list, create_an_item, edit_an_item

# the contruction of belows patterns in the () is the end of the url name i.e. www.sport/football.co.uk (football) and the function that affiliates that url
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_todo_list),
    url(r'^add$', create_an_item),
    # \d is for digit between 0-9 and with the + u can have any number. ?P to say this is going to be an expression
    url(r'^edit/(?P<id>\d+)$', edit_an_item)
]
# r in the url patterns above stands for regular expression
