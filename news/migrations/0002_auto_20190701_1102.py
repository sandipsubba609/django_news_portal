# Generated by Django 2.2.2 on 2019-07-01 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.CharField(choices=[('0', 'Politics'), ('1', 'Sport'), ('2', 'International')], max_length=2),
        ),
    ]
