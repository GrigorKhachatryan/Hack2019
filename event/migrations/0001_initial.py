# Generated by Django 2.1.3 on 2019-03-22 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('log', models.CharField(max_length=50)),
                ('pas', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('time', models.DateTimeField()),
                ('artist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Artists')),
            ],
        ),
        migrations.CreateModel(
            name='Fans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Events')),
            ],
        ),
        migrations.CreateModel(
            name='Polls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Events')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
                ('poll_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Polls')),
            ],
        ),
    ]