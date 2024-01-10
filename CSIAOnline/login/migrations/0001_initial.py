# Generated by Django 5.0.1 on 2024-01-09 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, unique=True)),
                ('last_name', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(default=True, max_length=20)),
                ('color', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]