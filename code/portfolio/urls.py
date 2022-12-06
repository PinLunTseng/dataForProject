from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'portfolio'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('questionnaire/', views.questionnaire, name='questionnaire'),
    # 問卷試算
    path('calculation/', views.calculation, name='calculation'),
    path('signUp/', views.signUp, name='signUp'),
    path('signIn/', views.signIn, name='signIn'),
    path('signOut/', views.signOut, name='signOut'),
    # path('portfolio_list/', views.portfolio_list),

    path('information/<str:company_name>', views.company_information, name='company_information'),

    # init assets detail
    # path('init/', views.create_company_detail_in_database),
    # path('init/', views.create_industry_name_in_database),
    path('test/', views.fn_test),
]