# Generated by Django 4.0.1 on 2023-03-29 20:57

import applications.account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('activation_code', models.CharField(blank=True, max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', applications.account.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('age', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('sexual_orientation', models.CharField(choices=[('HE', 'Heterosexual'), ('BI', 'Bisexual'), ('HO', 'Homosexual'), ('AS', 'Asexual'), ('PA', 'Pansexual'), ('PO', 'Polisexual'), ('QU', 'Queer'), ('DE', 'Demisexual'), ('ND', 'Not decide')], max_length=2)),
                ('description', models.TextField(max_length=200)),
                ('status', models.CharField(choices=[('LP', 'Long term partner'), ('FR', 'Find a friend'), ('HF', 'To have a fan'), ('OD', 'One Date')], max_length=2)),
                ('interests', models.CharField(choices=[('SP', 'Sport'), ('AT', 'Art'), ('MS', 'Music'), ('SD', 'Self development'), ('CN', 'Creation'), ('AR', 'Another')], max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='account.profile')),
            ],
        ),
    ]
