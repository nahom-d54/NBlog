# Generated by Django 4.1.1 on 2023-04-15 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_tag_post_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content_short',
            new_name='introduction',
        ),
    ]
