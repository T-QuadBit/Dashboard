# Generated by Django 4.0.4 on 2022-05-16 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowd_status', '0002_traindensity'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('News', models.CharField(max_length=500)),
            ],
        ),
    ]
