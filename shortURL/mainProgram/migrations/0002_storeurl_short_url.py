# Generated by Django 3.0.6 on 2020-07-03 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainProgram', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeurl',
            name='short_url',
            field=models.CharField(default='d', max_length=100),
            preserve_default=False,
        ),
    ]
