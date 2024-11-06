# Generated by Django 5.1.2 on 2024-11-05 19:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WasteRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waste_type', models.CharField(choices=[('plastic', 'Plastic'), ('organic', 'Organic'), ('electronic', 'Electronic'), ('metal', 'Metal'), ('other', 'Other')], max_length=20)),
                ('quantity', models.DecimalField(decimal_places=2, help_text='Quantity in kg', max_digits=5)),
                ('scheduled_time', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waste_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]