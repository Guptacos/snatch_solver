# Generated by Django 3.0.3 on 2020-02-26 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0002_auto_20200225_0338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='text',
        ),
        migrations.AddField(
            model_name='comment',
            name='post_input_text',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
