# Generated by Django 4.1.1 on 2023-04-13 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
