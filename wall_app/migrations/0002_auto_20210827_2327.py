# Generated by Django 3.2.6 on 2021-08-28 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wall_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='message_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='wall_app.message'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='wall_app.user'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='wall_app.user'),
        ),
    ]