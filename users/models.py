from django.db import models


class RegisterModel(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=255, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'User Registration'
        verbose_name_plural = 'User Registrations'

    def __str__(self):
        return self.full_name

    def generate_username(self):
        username = self.full_name.lower().replace(" ", "_")
        count = RegisterModel.objects.filter(username__startswith=username).count()
        if count > 0:
            username = f"{username}{count + 1}"
        return username

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.generate_username()
        super(RegisterModel, self).save(*args, **kwargs)


class LoginModel(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    login_at = models.DateTimeField(auto_now_add=True)
    logout_at = models.DateTimeField(null=True)
    user = models.ForeignKey(RegisterModel, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'User Login'
        verbose_name_plural = 'User Logins'

    def __str__(self):
        return self.email
