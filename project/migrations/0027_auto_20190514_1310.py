# Generated by Django 2.2 on 2019-05-14 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0026_auto_20190514_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='postid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Post'),
        ),
    ]