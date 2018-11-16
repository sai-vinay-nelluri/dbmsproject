# Generated by Django 2.1.1 on 2018-09-27 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0004_auto_20180927_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.CharField(choices=[('btech', 'B.Tech'), ('mtech', 'M.Tech'), ('mca', 'MCA')], default='B.tech', max_length=32),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(choices=[('s&h', 'science and humanities'), ('eee', 'electrical and electronical engineering'), ('me', 'mechanical engineering'), ('civil', 'civil engineering'), ('cse', 'computer science engineering'), ('ece', 'electronics and communication engineering'), ('it', 'information technology')], max_length=64, verbose_name='Branch'),
        ),
    ]
