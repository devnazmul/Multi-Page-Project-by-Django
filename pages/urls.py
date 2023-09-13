from django.urls import path
from .views import HomePage, AboutPage, PortfolioPage, ContactPage

# CODE START FROM HERE
urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("about/", AboutPage.as_view(), name="about"),
    path("portfolio/", PortfolioPage.as_view(), name="portfolio"),
    path("contact/", ContactPage.as_view(), name="contact"),
]
