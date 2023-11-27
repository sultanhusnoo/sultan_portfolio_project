

from django.urls import path
from .views import PortfolioHomepageView

urlpatterns = [
    path('', PortfolioHomepageView.as_view(), name='portfolio_home')
]