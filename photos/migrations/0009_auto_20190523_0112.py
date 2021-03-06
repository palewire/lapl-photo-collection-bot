# Generated by Django 2.2.1 on 2019-05-23 01:12

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('photos', '0008_photo_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='collection',
        ),
        migrations.AddField(
            model_name='photo',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
