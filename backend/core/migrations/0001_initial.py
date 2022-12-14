# Generated by Django 4.0.5 on 2022-06-25 05:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('PAST', 'Pastor'), ('STAF', 'Church Staff'), ('MEMBER', 'Church Staff')], max_length=6, null=True, verbose_name='Type of Person')),
                ('attendance', models.IntegerField(default=0, verbose_name='Number of Attendance')),
                ('alt_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Alternative Name')),
                ('sex', models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male')], max_length=3, null=True, verbose_name='Sex')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('marital_status', models.CharField(blank=True, choices=[('DI', 'Divorced'), ('MA', 'Married'), ('SI', 'Single'), ('WI', 'Widowed')], max_length=2, null=True, verbose_name='Marital Status')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone Number')),
                ('date_accept_christ', models.DateField(blank=True, null=True, verbose_name='Date of Accepting Christ')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person_user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
