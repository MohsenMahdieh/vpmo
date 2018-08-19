# Generated by Django 2.0.7 on 2018-08-19 09:28

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vpmoapp', '0005_auto_20180819_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='id',
        ),
        migrations.AddField(
            model_name='team',
            name='_id',
            field=djongo.models.fields.ObjectIdField(auto_created=True, default='3c47a127f71668c0a47fd1bd', primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='path',
            field=models.CharField(default='---', max_length=4048),
            preserve_default=False,
        ),
    ]
