# Generated by Django 2.0.2 on 2018-02-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Some description', max_length=255, verbose_name='User name')),
                ('start_education', models.DateField(auto_now=True)),
                ('start_education_time', models.DateTimeField(auto_now_add=True)),
                ('is_flag', models.BooleanField(verbose_name='True or false')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('int_some', models.IntegerField()),
                ('float_some', models.FloatField()),
                ('decimal_some', models.DecimalField(decimal_places=3, max_digits=5)),
                ('some_url', models.URLField(verbose_name='Url address')),
                ('some_slug', models.SlugField()),
                ('text', models.TextField()),
                ('some_file', models.FileField(upload_to='samlpes_txt')),
                ('some_image', models.ImageField(upload_to='img')),
            ],
        ),
    ]
