# Generated by Django 4.0.3 on 2022-04-12 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='T_Shop',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('online', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='T_Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.DateTimeField()),
                ('budget_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_spent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.t_shop')),
            ],
            options={
                'unique_together': {('shop_id', 'month')},
            },
        ),
    ]
