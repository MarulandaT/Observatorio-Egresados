# Generated by Django 2.0.2 on 2019-07-12 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190712_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='biography',
            field=models.CharField(default='biografia', max_length=50),
            preserve_default=False,
        ),
    ]
