# Generated by Django 3.1.2 on 2020-10-07 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VacationsUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(db_index=True)),
                ('updated_at', models.DateTimeField(db_index=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('activated_at', models.DateTimeField(null=True)),
                ('subscribed_at', models.DateTimeField(null=True)),
                ('is_approver', models.BooleanField(default=False)),
                ('is_rejector', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]