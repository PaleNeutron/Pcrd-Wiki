# Generated by Django 2.0.3 on 2018-05-30 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcrd_unpack', '0008_solution'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solution',
            name='left_team',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='right_team',
        ),
        migrations.RemoveField(
            model_name='team',
            name='units',
        ),
        migrations.DeleteModel(
            name='Solution',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]