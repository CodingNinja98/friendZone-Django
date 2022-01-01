# Generated by Django 2.2 on 2019-05-10 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_auto_20190510_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='notify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=100)),
                ('add', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.register')),
            ],
        ),
    ]