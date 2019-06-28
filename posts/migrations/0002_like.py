# Generated by Django 2.2.2 on 2019-06-26 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_follower'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_liked', to='posts.Post', verbose_name='Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_liked', to='users.Profile', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Like',
            },
        ),
    ]
