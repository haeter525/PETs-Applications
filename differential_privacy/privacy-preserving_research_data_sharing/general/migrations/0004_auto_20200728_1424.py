# Generated by Django 3.0.7 on 2020-07-28 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_auto_20200728_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='executemodel',
            name='log',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='executemodel',
            name='num_progress',
            field=models.IntegerField(default=0),
        ),
    ]