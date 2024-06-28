# Generated by Django 4.2.13 on 2024-06-28 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0045_coresettings_enable_server_scripts_and_more"),
        ("alerts", "0013_alerttemplate_action_env_vars_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="alerttemplate",
            name="action_rest",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="url_action_alert_template",
                to="core.urlaction",
            ),
        ),
        migrations.AddField(
            model_name="alerttemplate",
            name="action_type",
            field=models.CharField(
                choices=[("script", "Script"), ("server", "Server"), ("rest", "Rest")],
                default="script",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="alerttemplate",
            name="resolved_action_rest",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="resolved_url_action_alert_template",
                to="core.urlaction",
            ),
        ),
        migrations.AddField(
            model_name="alerttemplate",
            name="resolved_action_type",
            field=models.CharField(
                choices=[("script", "Script"), ("server", "Server"), ("rest", "Rest")],
                default="script",
                max_length=10,
            ),
        ),
    ]
