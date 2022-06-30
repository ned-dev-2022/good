# Generated by Django 4.0.5 on 2022-06-26 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoachGoodLangue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profil', models.FileField(upload_to='profil-good/')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom complet : ')),
                ('fonction', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
