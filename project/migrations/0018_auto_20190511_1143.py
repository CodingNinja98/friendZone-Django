# Generated by Django 2.2 on 2019-05-11 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0017_remove_notify_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='notify',
            name='frm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='frm', to='project.register'),
        ),
        migrations.AlterField(
            model_name='notify',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to', to='project.register'),
        ),
    ]
