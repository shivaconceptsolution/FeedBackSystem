# Generated by Django 2.2.7 on 2020-02-01 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedby', models.CharField(max_length=200)),
                ('feedto', models.CharField(max_length=200)),
                ('feeddesc', models.CharField(max_length=200)),
                ('feedbackrate', models.IntegerField()),
            ],
        ),
    ]
