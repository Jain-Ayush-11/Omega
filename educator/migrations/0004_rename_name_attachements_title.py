# Generated by Django 3.2.4 on 2022-05-25 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educator', '0003_attachements'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attachements',
            old_name='name',
            new_name='title',
        ),
    ]
