# Generated by Django 3.1.2 on 2020-10-25 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_task_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='week_num',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='modified',
            field=models.DateTimeField(choices=[('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9), ('ten', 10)], default='4'),
        ),
    ]
