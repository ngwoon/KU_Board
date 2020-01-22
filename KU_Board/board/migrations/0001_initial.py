# Generated by Django 3.0.2 on 2020-01-22 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('boardNum', models.IntegerField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=10, unique=True)),
                ('title', models.CharField(max_length=15)),
                ('content', models.CharField(max_length=100)),
                ('recommend', models.IntegerField()),
                ('unrecommend', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('category', models.CharField(default='자유', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replyNum', models.IntegerField()),
                ('content', models.CharField(max_length=20)),
            ],
        ),
    ]
