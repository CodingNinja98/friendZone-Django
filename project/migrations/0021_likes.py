# Generated by Django 2.2 on 2019-05-13 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0020_auto_20190513_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('is_like', models.BooleanField(default=False)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.register')),
                ('postid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Post')),
            ],
            options={
                'verbose_name_plural': 'Like Table',
            },
        ),
    ]
