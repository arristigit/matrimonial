# Generated by Django 3.2.2 on 2021-07-02 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_image_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.image'),
        ),
    ]
