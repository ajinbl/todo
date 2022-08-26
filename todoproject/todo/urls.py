from . import views
from django.urls import path
app_name = 'todo'
urlpatterns = [
    path('',views.index,name='index'),
    # path('',views.detail,name='detail'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    # path('',views.TaskList.as_view(),name='cview'),
    # path('detail/<int:pk>/', views.TaskDetail.as_view(),name='detail'),
    # path('update/<int:pk>/', views.TaskUpdate.as_view(), name='update'),
    # path('delete/<int:pk>/', views.TaskDelete.as_view(), name='delete'),

]
