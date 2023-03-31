# Generated by Django 4.0.1 on 2023-03-31 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_interests'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(choices=[('SP', 'Sport'), ('AT', 'Art'), ('MS', 'Music'), ('SD', 'Self development'), ('CN', 'Creation'), ('AR', 'Another')], max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='interests',
        ),
        migrations.AddField(
            model_name='profile',
            name='interests',
            field=models.ManyToManyField(to='account.Interests'),
        ),
    ]
