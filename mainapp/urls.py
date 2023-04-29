
from django.urls import path 
from .import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('register/',views.registerUser,name='register'),
    path('login/', views.loginUser, name='login_user'),
    path('logout/', views.logoutUser, name='logout_user'),
    path('user-profile/', views.user_profile, name='user_profile'),

    path('e-table/',views.employee_table,name='e-table'),
    path('e-create/',views.createEmployee,name='e-create'),
    path('e-update/<str:pk>',views.updateEmployee,name='e-update'),
    path('e-delete/<str:pk>',views.deleteEmployee,name='e-delete'),

    path('test/',views.testPage,name='test'),
    path('p-table/',views.product_table,name='p-table'),
]
