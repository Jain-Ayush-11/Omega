# Generated by Django 3.2.4 on 2022-06-02 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educator', '0007_alter_attachements_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachements',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
