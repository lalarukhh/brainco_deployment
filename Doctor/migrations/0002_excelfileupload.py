# Generated by Django 4.2.1 on 2023-05-20 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelFileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excel_file_upload', models.FileField(upload_to='excel')),
            ],
        ),
    ]