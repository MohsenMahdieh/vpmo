# Generated by Django 2.0.7 on 2018-07-30 03:49

from django.db import migrations, models
import guardian.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fullname', models.CharField(max_length=100, null=True)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('groups', models.ManyToManyField(related_name='groups', to='auth.Group')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, guardian.mixins.GuardianUserMixin),
        ),
    ]
