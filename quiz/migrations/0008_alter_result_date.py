# Generated by Django 4.0.3 on 2024-03-20 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_alter_result_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
