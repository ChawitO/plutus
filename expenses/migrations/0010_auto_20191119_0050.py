# Generated by Django 2.2.7 on 2019-11-19 00:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expenses', '0009_ledger_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expense',
            name='updator',
            field=models.ForeignKey(default='be7783a2-d5d5-41de-a9b9-0d561e0c6802', on_delete=django.db.models.deletion.DO_NOTHING, related_name='updated_expenses', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
