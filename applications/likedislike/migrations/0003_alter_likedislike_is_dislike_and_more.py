# Generated by Django 4.0.1 on 2023-03-28 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likedislike', '0002_alter_likedislike_is_dislike_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likedislike',
            name='is_dislike',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='likedislike',
            name='is_like',
            field=models.BooleanField(default=False),
        ),
    ]
