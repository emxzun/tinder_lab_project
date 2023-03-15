# Generated by Django 4.1.7 on 2023-03-15 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeDislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('dislike', models.BooleanField(default=False)),
                ('who_liked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who_likedislike', to=settings.AUTH_USER_MODEL, verbose_name='Кто поставил лайк/дизлайк')),
                ('whom_liked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='whom_likedislike', to=settings.AUTH_USER_MODEL, verbose_name='На кого поставили лайк/дизлайк')),
            ],
            options={
                'verbose_name': 'Лайк-Дизлайк',
                'verbose_name_plural': 'Лайки-Дизлайки',
            },
        ),
    ]