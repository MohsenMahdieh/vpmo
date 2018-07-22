# Generated by Django 2.0.2 on 2018-03-26 19:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vpmoapp', '0002_auto_20180307_0647'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Organisation',
            new_name='Team',
        ),
        migrations.AddField(
            model_name='myuser',
            name='fullname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]