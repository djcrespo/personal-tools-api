# Generated by Django 5.1.1 on 2024-10-03 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='downloaded_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
