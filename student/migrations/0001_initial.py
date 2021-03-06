# Generated by Django 3.2.5 on 2021-07-14 15:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_lastname', models.CharField(max_length=80, verbose_name='Ho va ten dem')),
                ('student_firstname', models.CharField(max_length=50, verbose_name='Ten')),
                ('student_gender', models.CharField(blank=True, choices=[('Nam', 'Nam'), ('Nu', 'Nu'), ('Khac', 'Khac')], default='Nam', max_length=10, verbose_name='Gioi tinh')),
                ('student_email', models.EmailField(blank=True, max_length=254)),
                ('student_date_of_birth', models.DateField(default=django.utils.timezone.now, verbose_name='Ngay sinh')),
                ('student_reg', models.DateField(auto_now_add=True)),
                ('student_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.class')),
            ],
            options={
                'ordering': ['student_class', 'student_firstname'],
            },
        ),
    ]
