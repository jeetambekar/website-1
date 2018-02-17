from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lean', views.lean),
    
    path('sixsigma', views.sixsigmaoverview, name='sixsigmaoverview'),
    path('sixsigma/define', views.sixsigmadefine, name='sixsigmadefine'),
    path('sixsigma/voc', views.sixsigmavoc, name='sixsigmavoc'),
    path('sixsigma/id', views.sixsigmaid, name='sixsigmaid'),
    path('sixsigma/customerdatacollection', views.sixsigmacustomerdatacollection, name='sixsigmacustomerdatacollection'),

    
    path('supplychain', views.supplychain),
]
