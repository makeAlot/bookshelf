# Generated by Django 4.2.5 on 2023-10-03 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_delete_samplemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
