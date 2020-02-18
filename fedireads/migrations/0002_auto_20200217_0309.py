# Generated by Django 3.0.3 on 2020-02-17 03:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fedireads', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='added_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='added_date',
            new_name='created_date',
        ),
        migrations.RemoveField(
            model_name='author',
            name='updated_date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='updated_date',
        ),
        migrations.RemoveField(
            model_name='shelf',
            name='updated_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated_date',
        ),
        migrations.AddField(
            model_name='author',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='federatedserver',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='federatedserver',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shelf',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shelfbook',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
