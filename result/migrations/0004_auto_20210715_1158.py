# Generated by Django 3.2.5 on 2021-07-15 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
        ('subjects', '0003_auto_20210714_2250'),
        ('result', '0003_auto_20210715_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectscore',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student', verbose_name='Hoc sinh'),
        ),
        migrations.AlterField(
            model_name='subjectscore',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.subject', verbose_name='Mon hoc'),
        ),
    ]
