# Generated by Django 5.0.3 on 2024-06-01 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_leaderboard_options_leaderboard_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameCompletionCounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
