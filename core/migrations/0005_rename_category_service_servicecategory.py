# Generated by Django 3.2.3 on 2023-05-05 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20230505_0811'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='category',
            new_name='servicecategory',
        ),
    ]
