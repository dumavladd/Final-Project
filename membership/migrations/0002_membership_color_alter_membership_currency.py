# Generated by Django 4.2.6 on 2023-10-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='color',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='membership',
            name='currency',
            field=models.CharField(choices=[('USD', 'Dollar'), ('EUR', 'Euro'), ('RON', 'Ron')], max_length=3),
        ),
    ]