# Generated by Django 2.0.5 on 2020-02-10 06:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='ig/')),
                ('name', models.CharField(max_length=60)),
                ('caption', models.CharField(max_length=200)),
                ('date_posted', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
