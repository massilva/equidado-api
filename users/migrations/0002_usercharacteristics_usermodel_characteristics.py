# Generated by Django 5.0.6 on 2024-05-19 10:57

from django.db import migrations, models


def populate_user_characteristics(apps, schema_editor):
    UserCharacteristics = apps.get_model('users', 'UserCharacteristics')
    characteristics = [
        {'name': 'Deficiência Visual - Baixa Visão', 'description': 'Condição de baixa visão, onde a pessoa tem uma acuidade visual reduzida.'},
        {'name': 'Deficiência Visual - Oclusão Total', 'description': 'Condição de cegueira total, onde a pessoa não tem percepção visual.'},
        {'name': 'Deficiência Auditiva - Surdez', 'description': 'Condição de perda auditiva total ou quase total.'},
        {'name': 'Deficiência Auditiva - Baixa Audição', 'description': 'Condição de perda auditiva parcial.'},
        {'name': 'Deficiência Física - Braço Amputado', 'description': 'Condição de amputação completa de um braço.'},
        {'name': 'Deficiência Física - Braço Parcialmente Amputado', 'description': 'Condição de amputação parcial de um braço.'},
        {'name': 'Deficiência Física - Perna Amputada', 'description': 'Condição de amputação completa de uma perna.'},
        {'name': 'Deficiência Física - Perna Parcialmente Amputada', 'description': 'Condição de amputação parcial de uma perna.'},
        {'name': 'Deficiência Intelectual', 'description': 'Condição que envolve limitações intelectuais e de comportamento adaptativo.'},
        {'name': 'Deficiência Mental', 'description': 'Condição que afeta a saúde mental, como transtornos psiquiátricos.'},
    ]
    for char in characteristics:
        UserCharacteristics.objects.create(**char)


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCharacteristics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='usermodel',
            name='characteristics',
            field=models.ManyToManyField(related_name='users', to='users.usercharacteristics'),
        ),
        migrations.RunPython(populate_user_characteristics),
    ]
