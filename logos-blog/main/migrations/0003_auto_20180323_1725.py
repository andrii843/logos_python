# Generated by Django 2.0.3 on 2018-03-23 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20180314_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Article likes',
                'verbose_name': 'Article like',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(to='main.ArticleLike'),
        ),
    ]
