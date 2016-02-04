from django.conf.urls import url
from . import views, models

urlpatterns = [
    url(r'^prev-next/$', views.PrevNextPaginatorView.as_view(), name='prev_next'),
    url(r'^prev-next-desc/$', views.PrevNextPaginatorByDescView.as_view(), name='prev_next_desc'),
    url(r'^all/$', views.AllPaginatorView.as_view(), name='all'),
    url(r'^pure/$', views.PurePaginatorView.as_view(), name='pure'),
    url(r'^bootstrap-pure/$', views.BootstrapPurePaginatorView.as_view(), name='bootstrap_pure'),
    url(r'^share/', 
        views.SharedPaginatorView.as_view(),
        name='share')
]