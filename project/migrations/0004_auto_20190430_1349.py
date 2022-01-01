# Generated by Django 2.2 on 2019-04-30 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_register_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='date_of_birth',
            field=models.DateField(blank=True),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
                ('media', models.FileField(blank=True, upload_to='posts/%Y/%m/%d')),
                ('upload_on', models.DateField(auto_now_add=True)),
                ('edit_on', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.register')),
            ],
        ),
    ]