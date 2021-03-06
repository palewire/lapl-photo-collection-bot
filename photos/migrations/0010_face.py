# Generated by Django 2.2.2 on 2019-06-15 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0009_auto_20190523_0112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Face',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Photo')),
            ],
        ),
    ]
