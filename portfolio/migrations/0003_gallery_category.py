# Generated by Django 5.0.6 on 2024-08-05 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_gallerycategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='portfolio.gallerycategory'),
            preserve_default=False,
        ),
    ]
