from django.urls import path

from .views import index, other_page
from .views import BBLoginView
from .views import BBLogoutView
from .views import profile
from .views import ChangeUserInfoView

app_name = 'main'

urlpatterns = [
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
