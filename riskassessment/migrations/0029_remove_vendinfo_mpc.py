
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('riskassessment', '0028_auto_20210429_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendinfo',
            name='mpc',
        ),
    ]
