# Generated by Django 4.0.3 on 2022-04-18 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0048_remove_agent_has_patches_pending_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='agent',
            index=models.Index(fields=['monitoring_type'], name='agents_agen_monitor_df8816_idx'),
        ),
    ]