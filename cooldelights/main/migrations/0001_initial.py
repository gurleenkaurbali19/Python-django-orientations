# Generated by Django 5.0.4 on 2024-05-10 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.IntegerField(max_length=20)),
                ('desc', models.TextField(max_length=20)),
            ],
        ),
    ]
