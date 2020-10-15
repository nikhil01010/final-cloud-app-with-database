# Generated by Django 3.1.2 on 2020-10-15 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20201015_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data.user')),
                ('full_time', models.BooleanField(default=True)),
                ('total_learners', models.IntegerField()),
            ],
            bases=('data.user',),
        ),
    ]
