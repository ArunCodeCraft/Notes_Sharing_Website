# Generated by Django 4.2.12 on 2024-05-28 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NOTES', '0004_rename_uplodingdate_uploadednotes_uploadingdate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploadingdate', models.DateField(auto_now_add=True)),
                ('subject', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
