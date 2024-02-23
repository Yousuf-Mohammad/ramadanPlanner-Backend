# Generated by Django 4.2.10 on 2024-02-23 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quranchecklist',
            name='completed_value',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='quranchecklist',
            name='last_read_surah',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='quranchecklist',
            name='last_read_unit',
            field=models.CharField(blank=True, choices=[('ayah', 'AYAH'), ('page', 'PAGE'), ('juz', 'JUZ'), ('surah', 'SURAH')], max_length=255),
        ),
        migrations.AlterField(
            model_name='quranchecklist',
            name='last_read_value',
            field=models.IntegerField(blank=True),
        ),
    ]