# Generated by Django 4.2.9 on 2024-10-08 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bizz', '0014_remove_config_login_config_host_config_password_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='script',
            old_name='schedule_days',
            new_name='schedule_day',
        ),
        migrations.AlterField(
            model_name='config',
            name='port',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
