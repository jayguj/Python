# Generated by Django 2.1.1 on 2018-12-19 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_app', '0005_auto_20181219_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_message', models.CharField(max_length=500)),
                ('user_id', models.ForeignKey(on_delete=False, to='bot_app.UserDetails')),
            ],
        ),
        migrations.RemoveField(
            model_name='u_requests',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='u_Requests',
        ),
    ]