# Generated by Django 3.2.4 on 2022-06-02 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educator', '0004_rename_name_attachements_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachements',
            name='category',
        ),
    ]
