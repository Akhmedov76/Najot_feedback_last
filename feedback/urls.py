from django.urls import path

from feedback.views import home_page_view, comments_view, submit_offer_view, profile_view, offer_view, error_view, \
    problem_view, about_site_view

app_name = 'home_page'
urlpatterns = [
    path('', home_page_view, name='home'),

    path('comments/', comments_view, name='comments'),

    path('offer/', offer_view, name='offer'),
    path('profile/', profile_view, name='profile'),
    path('submit-offer/', submit_offer_view, name='submit_offer'),
    path('problem/', problem_view, name='problem'),
    path('about/', about_site_view, name='about'),

    path('error/', error_view, name='error'),

]
