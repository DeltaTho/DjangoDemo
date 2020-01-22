# Generated by Django 2.2.5 on 2019-10-06 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exhibit_title', models.CharField(max_length=200)),
                ('exhibit_description', models.TextField()),
                ('exhibit_picture_link', models.CharField(max_length=200)),
            ],
        ),
    ]