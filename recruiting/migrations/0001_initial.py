# Generated by Django 2.2.5 on 2019-09-02 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_code', models.CharField(max_length=20, unique=True)),
                ('questions', models.ManyToManyField(to='recruiting.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Sith',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planet_siths', to='recruiting.Planet')),
            ],
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planet_recruits', to='recruiting.Planet')),
                ('sith', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shadow_hands', to='recruiting.Sith')),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.BooleanField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_recruit_answers', to='recruiting.Question')),
                ('recruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recruit_answers', to='recruiting.Recruit')),
            ],
            options={
                'unique_together': {('recruit', 'question')},
            },
        ),
    ]