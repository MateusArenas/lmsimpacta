# Generated by Django 2.1.3 on 2019-02-19 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='status',
            field=models.CharField(blank=True, choices=[('ABERTA', 'Aberta'), ('FECHADA', 'Fechada')], default='Aberta', max_length=50, null=True),
        ),
    ]
