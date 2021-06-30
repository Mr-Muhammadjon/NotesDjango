# Generated by Django 3.2.4 on 2021-06-30 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=330, verbose_name='title')),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='poster/', verbose_name='rasim')),
            ],
        ),
    ]