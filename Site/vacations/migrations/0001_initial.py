# Generated by Django 3.1.7 on 2021-02-28 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacationReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VacationRejectionReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vacation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True)),
                ('updated_at', models.DateTimeField(db_index=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('confirmed_at', models.DateTimeField(null=True)),
                ('confirmed_by', models.ForeignKey(limit_choices_to={'is_approver': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='confirmed_vacations', to='home.employee')),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vacations', to='vacations.vacationreason')),
                ('rejected_by', models.ForeignKey(limit_choices_to={'is_rejector': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rejected_vacations', to='home.employee')),
                ('rejection_reason', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vacations', to='vacations.vacationrejectionreason')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vacations', to='home.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
