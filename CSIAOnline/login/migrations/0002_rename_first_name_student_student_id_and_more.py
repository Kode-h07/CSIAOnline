# Generated by Django 5.0.1 on 2024-01-10 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='first_name',
            new_name='student_id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='color',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
