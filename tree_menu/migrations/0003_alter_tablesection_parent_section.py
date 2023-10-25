# Generated by Django 4.2.6 on 2023-10-25 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu', '0002_tablesection_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablesection',
            name='parent_section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_sections', to='tree_menu.tablesection'),
        ),
    ]