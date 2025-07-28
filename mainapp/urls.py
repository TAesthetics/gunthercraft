from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    YouthMemberCreateView, YouthMemberUpdateView, youth_dashboard
)

urlpatterns = [
    path('sovereign-youth/', views.sovereign_youth, name='sovereign_youth'),
    path('statutes/', views.statutes, name='statutes'),
    path('programm/', views.programm, name='programm'),
    path('youth/statutes/', views.statutes, name='youth-statutes'),
    # Home and authentication
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    
    # Member area
    path('member/', views.member, name='member'),
    
    # Youth Organization URLs
    path('youth/', views.organization_list, name='organization_list'),
    path('youth/join/', youth_dashboard, name='youth-dashboard'),
    path('youth/org/<int:pk>/', views.organization_detail, name='organization_detail'),
    
    # Staff-only URLs
    path('youth/org/add/', views.organization_create, name='organization_create'),
    path('youth/org/<int:pk>/edit/', views.organization_update, name='organization_update'),
    
    # Member profile URLs
    path('youth/member/add/', YouthMemberCreateView.as_view(), name='youth-member-create'),
    path('youth/member/<int:pk>/edit/', YouthMemberUpdateView.as_view(), name='youth-member-update'),
]
