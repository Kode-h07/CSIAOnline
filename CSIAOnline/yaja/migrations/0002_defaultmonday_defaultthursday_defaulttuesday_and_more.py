# Generated by Django 5.0.1 on 2024-06-04 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yaja', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultMonday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(blank=True, max_length=10, null=True)),
                ('period1', models.CharField(max_length=50)),
                ('period2', models.CharField(max_length=50)),
                ('period3', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DefaultThursday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(blank=True, max_length=10, null=True)),
                ('period1', models.CharField(max_length=50)),
                ('period2', models.CharField(max_length=50)),
                ('period3', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DefaultTuesday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(blank=True, max_length=10, null=True)),
                ('period1', models.CharField(max_length=50)),
                ('period2', models.CharField(max_length=50)),
                ('period3', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DefaultWednesday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(blank=True, max_length=10, null=True)),
                ('period1', models.CharField(max_length=50)),
                ('period2', models.CharField(max_length=50)),
                ('period3', models.CharField(max_length=50)),
            ],
        ),
    ]
