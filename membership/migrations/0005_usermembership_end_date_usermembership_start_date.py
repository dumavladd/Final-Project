# Generated by Django 4.2.6 on 2023-10-31 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0004_usermembership'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermembership',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='usermembership',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
