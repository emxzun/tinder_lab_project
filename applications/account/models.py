from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.create_activation_code()
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=100, blank=True)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return f'{self.username}, {self.email}'

    def create_activation_code(self):
        import uuid
        code = str(uuid.uuid4())
        self.activation_code = code



class Profile(models.Model):

    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')

    class SexualOrientation(models.TextChoices):
        HETEROSEXUAL = 'HE', _('Heterosexual')
        BISEXUAL = 'BI', _('Bisexual')
        HOMOSEXUAL = 'HO', _('Homosexual')
        ASEXUAL = 'AS', _('Asexual')
        PANSEXUAL = 'PA', _('Pansexual')
        POLISEXUAL = 'PO', _('Polisexual')
        QUEER = 'QU', _('Queer')
        DEMISEXUAL = 'DE', _('Demisexual')
        NOT_DECIDE = 'ND', _('Not decide')

    class Status(models.TextChoices):
        LONG_TERM_PARTNER = 'LP', _('Long term partner')
        FIND_A_FRIEND = 'FR', _('Find a friend')
        TO_HAVE_A_FAN = 'HF', _('To have a fan')
        ONE_DATE = 'OD', _('One Date')

    INTERESTS = (
        ('SP', 'Sport'),
        ('AT', 'Art'),
        ('MS', 'Music'),
        ('SD', 'Self development'),
        ('CN', 'Creation'),
        ('AR', 'Another'),
    )

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    sexual_orientation = models.CharField(max_length=2, choices=SexualOrientation.choices)
    description = models.TextField(max_length=200)
    status = models.CharField(max_length=2, choices=Status.choices)
    interests = models.CharField(max_length=2, choices=INTERESTS)

    def __str__(self):
        return f'{self.user}: {self.age}'


class Image(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
