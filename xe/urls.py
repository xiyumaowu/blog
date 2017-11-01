"""xe URL Configuration

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
import blog.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$',blog.views.index),
    url(r'^index/ui-elements.html$', blog.views.ui_elements),
    url(r'^index/chart.html$', blog.views.chart),
    url(r'^index/tab-panel.html$', blog.views.tab_panel),
    url(r'^index/table.html$', blog.views.table),
    url(r'^index/empty.html$', blog.views.empty),
    url(r'^index/form.html$', blog.views.form),
    url(r'^index/index.html$', blog.views.index),
]
