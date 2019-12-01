# Generated by Django 2.2.7 on 2019-12-01 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('X', models.FloatField(help_text='Longitude')),
                ('Y', models.FloatField(help_text='Latitude')),
                ('Unique_squirrel_id', models.CharField(help_text='Unique Squirrel ID', max_length=100)),
                ('Shift', models.CharField(choices=[('PM', 'PM'), ('AM', 'AM')], max_length=100)),
                ('Date', models.DateField(help_text='Date')),
                ('Age', models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], max_length=100, null=True)),
                ('Primary_Fur_Color', models.CharField(help_text='Primary Fur Color', max_length=100, null=True)),
                ('Location', models.CharField(help_text='Location', max_length=100, null=True)),
                ('Specific_location', models.CharField(help_text='Specific Location', max_length=100, null=True)),
                ('Running', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Running', max_length=100)),
                ('Chasing', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Chasing', max_length=100)),
                ('Climbing', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Climbing', max_length=100)),
                ('Eating', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Eating', max_length=100)),
                ('Foraging', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Foraging', max_length=100)),
                ('Other_activities', models.CharField(help_text='Other Activities', max_length=100, null=True)),
                ('Kuks', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Kuks', max_length=100)),
                ('Quaas', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Quaas', max_length=100)),
                ('Moans', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Moans', max_length=100)),
                ('Tail_flags', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Tail flags', max_length=100)),
                ('Tail_twitches', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Tail twitches', max_length=100)),
                ('Approaches', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Approaches', max_length=100)),
                ('Indifferent', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Indifferent', max_length=100)),
                ('Runs_from', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], help_text='Runs_from', max_length=100)),
            ],
        ),
    ]
