# Generated by Django 4.2.10 on 2024-02-17 13:24

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
            name='DefaultChecklistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DailyActivityChecklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'unique_together': {('user', 'date')},
            },
        ),
        migrations.CreateModel(
            name='ChecklistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_name', models.CharField(blank=True, max_length=255, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('checklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='checklist.dailyactivitychecklist')),
                ('default_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='checklist.defaultchecklistitem')),
            ],
        ),
        migrations.CreateModel(
            name='SalahChecklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('fardh_fajr', models.BooleanField(default=False)),
                ('fardh_duhr', models.BooleanField(default=False)),
                ('fardh_asr', models.BooleanField(default=False)),
                ('fardh_maghrib', models.BooleanField(default=False)),
                ('fardh_isha', models.BooleanField(default=False)),
                ('sunnah_fajr', models.BooleanField(default=False)),
                ('sunnah_duhr', models.BooleanField(default=False)),
                ('sunnah_asr', models.BooleanField(default=False)),
                ('sunnah_maghrib', models.BooleanField(default=False)),
                ('sunnah_isha', models.BooleanField(default=False)),
                ('sunnah_taraweeh', models.BooleanField(default=False)),
                ('sunnah_tahajjud', models.BooleanField(default=False)),
                ('sunnah_duha', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'unique_together': {('user', 'date')},
            },
        ),
        migrations.CreateModel(
            name='QuranChecklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('last_read_unit', models.CharField(choices=[('ayah', 'AYAH'), ('page', 'PAGE'), ('juz', 'JUZ'), ('surah', 'SURAH')], max_length=255)),
                ('last_read_surah', models.IntegerField()),
                ('last_read_value', models.IntegerField()),
                ('completed_value', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'unique_together': {('user', 'date')},
            },
        ),
    ]