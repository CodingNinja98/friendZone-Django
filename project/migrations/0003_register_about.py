# Generated by Django 2.2 on 2019-04-27 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_register_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='about',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]