# Generated by Django 4.2.5 on 2023-10-02 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('nome', models.CharField(max_length=200)),
                ('data_pub', models.DateTimeField(verbose_name='My datetime')),
                ('inicio', models.DateTimeField(verbose_name='My datetime')),
                ('fim', models.DateTimeField(verbose_name='My datetime')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('date_pub', models.DateTimeField(verbose_name='My datetime')),
                ('organizador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Palestrante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_reg', models.DateTimeField(verbose_name='My datetime')),
                ('Atividade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.atividade')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
        migrations.AddField(
            model_name='atividade',
            name='palestrante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.palestrante'),
        ),
    ]
