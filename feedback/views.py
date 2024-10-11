from django.shortcuts import render

from feedback.form import OfferForm, ProblemsForm
from feedback.models import AboutSiteModel, QuestionModel, TeamAboutModul, AppealsModule
from users.models import RegisterModel, LoginModel


def home_page_view(request):
    register_form = RegisterModel()
    login_form = LoginModel()
    about_site_form = AboutSiteModel.objects.all()
    team_about_form = TeamAboutModul.objects.all()
    question_form = QuestionModel.objects.all()
    appeals_form = AppealsModule.objects.all()
    context={
        'register': register_form,
        'login': login_form,
        'about_site': about_site_form,
        'team_about': team_about_form,
        'question': question_form,
        'appeals': appeals_form,
    }
    return render(request, 'index.html', context)


def comments_view(request):
    return render(request, 'comment.html')


def offers_view(request):
    return render(request, 'offer-form.html')

def submit_offer_view(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thank_you.html')
    else:
        form = OfferForm()
    return render(request, 'offer-form.html', {'form': form})


def problem_view(request):
    if request.method == 'POST':
        form = ProblemsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thank_you.html')
        else:
            form = ProblemsForm()
            return render(request, 'problem-form.html', {'form': form})


def offer_view(request):
    return render(request, 'offer.html')


def profile_view(request):
    return render(request, 'profile.html')


def error_view(request):
    return render(request, '404.html')

