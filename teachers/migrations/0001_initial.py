# Generated by Django 3.2.5 on 2021-07-14 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Ten giao vien')),
                ('bo_mon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.subject')),
                ('khoa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.khoa')),
            ],
            options={
                'ordering': ['khoa', 'bo_mon', 'name'],
            },
        ),
    ]
