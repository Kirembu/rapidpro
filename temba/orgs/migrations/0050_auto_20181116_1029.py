# Generated by Django 2.0.9 on 2018-11-16 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0049_org_flow_server_enabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='brand',
            field=models.CharField(default='callcenter.africa', help_text='The brand used in emails', max_length=128, verbose_name='Brand'),
        ),
    ]
