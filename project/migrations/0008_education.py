# Generated by Django 2.2 on 2019-05-02 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20190502_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=200)),
                ('position', models.CharField(blank=True, max_length=200)),
                ('work_city', models.CharField(blank=True, max_length=200)),
                ('work_from', models.CharField(blank=True, max_length=200)),
                ('work_to', models.CharField(blank=True, max_length=200)),
                ('university', models.CharField(blank=True, max_length=200)),
                ('stream', models.CharField(blank=True, max_length=200)),
                ('uni_city', models.CharField(blank=True, max_length=200)),
                ('uni_from', models.CharField(blank=True, max_length=200)),
                ('uni_to', models.CharField(blank=True, max_length=200)),
                ('school', models.CharField(blank=True, max_length=200)),
                ('school_city', models.CharField(blank=True, max_length=200)),
                ('school_from', models.CharField(blank=True, max_length=200)),
                ('school_to', models.CharField(blank=True, max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.register')),
            ],
        ),
    ]
