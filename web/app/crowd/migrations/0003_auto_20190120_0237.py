# Generated by Django 2.1.5 on 2019-01-20 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crowd', '0002_basestation_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientconnection',
            name='channel',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientconnection',
            name='gain',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientconnection',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connections', to='crowd.WirelessClient'),
        ),
        migrations.AlterField(
            model_name='clientconnection',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='crowd.BaseStation'),
        ),
        migrations.AlterField(
            model_name='clientconnection',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
