from django.urls import path

from . import views

urlpatterns = [
    path("",views.home,name="home"),
    #lines
    path('lines/',views.LinesView.as_view(),name='lines'),
    path('lines/new/',views.CreateLineView.as_view(), name='create_line'),
    path('lines/<pk>/update/',views.UpdateLineView.as_view(), name='update_line'),
    path('lines/<pk>/delete/',views.DeleteLineView.as_view(),name='delete_line'),
    #stations
    path('stations/',views.LinesView.as_view(),name='stations'),
    path('stations/new/',views.CreateLineView.as_view(), name='create_station'),
    path('stations/<pk>/update/',views.UpdateLineView.as_view(), name='update_station'),
    path('stations/<pk>/delete/',views.DeleteLineView.as_view(),name='delete_station'),
    #stops
    path('stops/',views.LinesView.as_view(),name='stops'),
    path('stops/new/',views.CreateLineView.as_view(), name='create_stop'),
    path('stops/<pk>/update/',views.UpdateLineView.as_view(), name='update_stop'),
    path('stops/<pk>/delete/',views.DeleteLineView.as_view(),name='delete_stop'),
]