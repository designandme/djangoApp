from django.conf.urls import include, url
from django.contrib import admin

# import the views of our app i.e. VisamoKids views.py
from visamokids import views

urlpatterns = [
    url(r'^$', views.login_view, name='login'),
    url(r'^index/', views.index, name='index'),
    # url(r'^search/', views.search, name='search'),    
    url(r'^students/', views.student, name='student'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^donors/', views.donor, name='donor'),
    url(r'^student/(?P<gr_no>\d+)/',views.student_detail, name='student_detail'),
    url(r'^donor/(?P<id>\d+)/',views.donor_detail, name='donor_detail'),
    url(r'^sendEmail/(?P<id>\d+)',views.sendEmail, name='send_email'),

    # below is the url pre defined for the admin app
    url(r'^admin/', include(admin.site.urls),name='admin_site'),
]
