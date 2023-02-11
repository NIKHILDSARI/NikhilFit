# Generated by Django 4.1.6 on 2023-02-07 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=200, null=True)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.IntegerField(null=True)),
                ('bodytype', models.CharField(choices=[('chubby', 'chubby'), ('skinny', 'skinny'), ('lean', 'lean'), ('athletic ', 'athletic ')], max_length=200, null=True)),
                ('currentweight', models.IntegerField(null=True)),
                ('date', models.DateField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='split',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('split_name', models.CharField(choices=[('chest', 'chest'), ('back', 'back'), ('legs', 'legs'), ('core', 'core')], max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Leg_exercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercises', models.CharField(choices=[('squat', 'squat'), ('lung', 'lung'), ('rdl', 'rdl'), ('legpress', 'legpress')], max_length=200, null=True)),
                ('set1', models.IntegerField(null=True)),
                ('set2', models.IntegerField(null=True)),
                ('set3', models.IntegerField(null=True)),
                ('split', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exercisestracker.split')),
            ],
        ),
        migrations.CreateModel(
            name='Core_exercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercises', models.CharField(choices=[('cablecrunch', 'cablecrunch'), ('hanginglegrises', 'hanginglegrises'), ('suitcasewalk', 'suitcasewalk'), ('sidelegrise', 'sidelegrise'), ('plank', 'plank')], max_length=200, null=True)),
                ('set1', models.IntegerField(null=True)),
                ('set2', models.IntegerField(null=True)),
                ('set3', models.IntegerField(null=True)),
                ('split', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exercisestracker.split')),
            ],
        ),
        migrations.CreateModel(
            name='Chest_exercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercises', models.CharField(choices=[('benchpress', 'benchpress'), ('inclinepress', 'inclinepress'), ('declinepress', 'declinepress'), ('flatpress', 'flatpress')], max_length=200, null=True)),
                ('set1', models.IntegerField(null=True)),
                ('set2', models.IntegerField(null=True)),
                ('set3', models.IntegerField(null=True)),
                ('split', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exercisestracker.split')),
            ],
        ),
        migrations.CreateModel(
            name='Back_exercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercises', models.CharField(choices=[('pullups', 'pullups'), ('bendoverrow', 'bendoverrow'), ('shugs', 'shugs'), ('dumblerow', 'dumblerow')], max_length=200, null=True)),
                ('set1', models.IntegerField(null=True)),
                ('set2', models.IntegerField(null=True)),
                ('set3', models.IntegerField(null=True)),
                ('split', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exercisestracker.split')),
            ],
        ),
    ]
