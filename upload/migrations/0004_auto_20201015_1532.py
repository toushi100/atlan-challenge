# Generated by Django 3.1.2 on 2020-10-15 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_file_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file_content',
            name='date',
        ),
        migrations.AlterField(
            model_name='file_content',
            name='dollar',
            field=models.CharField(max_length=50),
        ),
    ]
