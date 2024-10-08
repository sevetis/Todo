# Generated by Django 5.1.1 on 2024-10-01 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='desciption',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('p', 'Pending'), ('d', 'Done')], max_length=1, verbose_name='Todo Status'),
        ),
    ]
