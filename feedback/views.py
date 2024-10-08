from django.shortcuts import render

from feedback.form import OfferForm
from feedback.models import OffersModel, ProblemsModel
from users.models import RegisterModel, LoginModel


def home_page_view(request):
    register_form = RegisterModel()
    login_form = LoginModel()
    return render(request, 'index.html', {'register_form': register_form, 'login_form': login_form})


def comments_view(request):
    return render(request, './main/comments/comment.html')


# def submit_offer_view(request):
#     if request.method == 'POST':
#         form = OfferForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             description = form.cleaned_data['description']
#             OffersModel.objects.create(title=title, description=description)
#             return render(request, 'thank_you.html')
#     else:
#         form = OfferForm()
#     return render(request, 'main/forms/offer/offer-form.html', {'form': form})

def submit_offer_view(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thank_you.html')
    else:
        form = OfferForm()
    return render(request, 'main/forms/offer/offer-form.html', {'form': form})


def problem_view(request):
    problems = ProblemsModel.objects.all()
    return render(request, 'thank_you.html', {'problems': problems})


def offer_view(request):
    return render(request, './main/offers/offer.html')


def profile_view(request):
    return render(request, './main/profile/profile.html')


def error_view(request):
    return render(request, 'main/404/404.html')
