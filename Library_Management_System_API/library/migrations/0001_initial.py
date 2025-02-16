# Generated by Django 5.1.2 on 2024-12-30 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('publication_date', models.DateField()),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('number_of_copies', models.PositiveIntegerField()),
            ],
        ),
    ]
