# Generated by Django 3.2.4 on 2021-06-21 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('to_do', '0002_createdbyme'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CreatedByMe',
        ),
        migrations.AddField(
            model_name='newtask',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
