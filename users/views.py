from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

from conf.settings import EMAIL_HOST_USER
from users.form import LoginForm, RegistrationForm
from users.token import account_activation_token


def verify_email(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect(reverse_lazy('users:login'))
    else:
        return render(request, 'email_not_verify.html')


def send_email_verification(request, user):
    token = account_activation_token.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    current_site = get_current_site(request)
    verification_url = reverse('users:verify-email', kwargs={'uidb64': uid, 'token': token})
    full_url = f"http://{current_site.domain}{verification_url}"

    text_content = render_to_string(
        'verify_email.html',
        {'user': user, 'full_url': full_url}
    )

    message = EmailMultiAlternatives(
        subject="Verification Email",
        body=text_content,
        from_email=EMAIL_HOST_USER,
        to=[user.email]
    )
    message.attach_alternative(text_content, "text/html")
    message.send()


def generate_username(full_name):
    if not full_name:
        full_name = "user"
    base_username = full_name.lower().replace(" ", "_")
    username = base_username
    count = 1
    while User.objects.filter(username=username).exists():
        username = f"{base_username}_{count}"
        count += 1
    return username


@csrf_protect
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])

            full_name = form.cleaned_data.get('full_name')
            user.username = generate_username(full_name)

            user.is_active = False
            user.save()

            # send email verification
            send_email_verification(request, user)
            return redirect(reverse_lazy('users:login'))
        else:
            errors = form.errors
            return render(request, 'main/auth/register/register.html', {'errors': errors, 'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'main/auth/register/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request=request, email=email, password=password)
            if user is not None:
                login(user, request)
                return redirect(reverse_lazy('/'))
            else:
                errors = form.errors
                return render(request, 'main/auth/login/login.html', {'errors': errors})
    return render(request, 'main/auth/login/login.html')


def logout_view(request):
    return HttpResponse("This is a logout view")
