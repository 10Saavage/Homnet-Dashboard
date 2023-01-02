from django.urls import path

from .views import IndexView, addrouter, DetailRouter, ListRouters, router_log, active_user

app_name = "home"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('addrouter', addrouter, name='addrouter'),
    path('listrouters', ListRouters.as_view(), name="listrouters"),
    path('detail/<uuid:serialnumber>', DetailRouter.as_view(), name='details'),
    path('router_log/', router_log, name="router_log"),
    path('active_user/', active_user, name="active_user")
]