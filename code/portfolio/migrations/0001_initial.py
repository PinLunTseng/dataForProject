# Generated by Django 4.0.1 on 2022-10-19 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='WeightWOmega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('assets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.assets')),
                ('index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.index')),
            ],
        ),
        migrations.CreateModel(
            name='WeightMV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('assets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.assets')),
                ('index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.index')),
            ],
        ),
        migrations.CreateModel(
            name='WeightCVaR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('assets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.assets')),
                ('index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.index')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('assets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.assets')),
                ('index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.index')),
            ],
        ),
        migrations.AddField(
            model_name='index',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.period'),
        ),
    ]
