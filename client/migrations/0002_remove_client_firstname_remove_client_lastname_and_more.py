# Generated by Django 4.2.6 on 2023-10-23 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='client',
            name='lastname',
        ),
        migrations.AddField(
            model_name='client',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=31, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='profile',
            field=models.ImageField(null=True, upload_to='profiles/'),
        ),
        migrations.AddField(
            model_name='client',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='provider.provider'),
        ),
        migrations.AddField(
            model_name='client',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='telephone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
