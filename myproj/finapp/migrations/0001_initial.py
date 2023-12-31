# Generated by Django 4.2.5 on 2023-10-02 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rf_rate', models.FloatField(null=True)),
                ('erp', models.FloatField(null=True)),
                ('gdp', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyBeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('beta', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GlobalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qend', models.DateField(null=True)),
                ('longticker', models.CharField(max_length=25, null=True)),
                ('revenue', models.FloatField(null=True)),
                ('ebitda', models.FloatField(null=True)),
                ('ecos', models.FloatField(null=True)),
                ('ev', models.FloatField(null=True)),
                ('mcap', models.FloatField(null=True)),
                ('period', models.CharField(max_length=10, null=True)),
                ('annlrev', models.FloatField(null=True)),
                ('annlebitda', models.FloatField(null=True)),
                ('annlecos', models.FloatField(null=True)),
                ('pp1mcap', models.FloatField(null=True)),
                ('pp2mcap', models.FloatField(null=True)),
                ('pp1annlrev', models.FloatField(null=True)),
                ('pp2annlrev', models.FloatField(null=True)),
                ('revg6m', models.FloatField(null=True)),
                ('revg3m', models.FloatField(null=True)),
                ('ecosmgn', models.FloatField(null=True)),
                ('pp1annlecos', models.FloatField(null=True)),
                ('pp2annlecos', models.FloatField(null=True)),
                ('conmgn3m', models.FloatField(null=True)),
                ('conmgn6m', models.FloatField(null=True)),
                ('mcapg3m', models.FloatField(null=True)),
                ('mcapg6m', models.FloatField(null=True)),
                ('exch', models.CharField(max_length=15, null=True)),
                ('tick', models.CharField(max_length=10, null=True)),
                ('beta', models.FloatField(null=True)),
                ('industry', models.CharField(max_length=100, null=True)),
                ('indrev', models.FloatField(null=True)),
                ('indecos', models.FloatField(null=True)),
                ('indmgm', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HousePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_date', models.DateField()),
                ('symbol', models.CharField(max_length=250)),
                ('vector', models.CharField(max_length=250)),
                ('coordinate', models.FloatField(null=True)),
                ('value', models.FloatField(null=True)),
                ('status', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('return_email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('longticker', models.CharField(blank=True, max_length=20, null=True)),
                ('ticker', models.CharField(max_length=15)),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='industry', to='finapp.industry')),
            ],
        ),
        migrations.CreateModel(
            name='BackTestData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=10)),
                ('ticker', models.CharField(max_length=25)),
                ('mcap', models.FloatField(blank=True, null=True)),
                ('mcapg3m', models.FloatField(blank=True, null=True)),
                ('mcapg6m', models.FloatField(blank=True, null=True)),
                ('flag_val', models.CharField(blank=True, max_length=20, null=True)),
                ('flag_revg', models.CharField(blank=True, max_length=20, null=True)),
                ('flag_revga3y', models.CharField(blank=True, max_length=20, null=True)),
                ('flag_igr', models.CharField(blank=True, max_length=20, null=True)),
                ('flag_mgn', models.CharField(blank=True, max_length=20, null=True)),
                ('flag_disc_prem', models.CharField(blank=True, max_length=20, null=True)),
                ('flag_disc_prem_cy', models.CharField(blank=True, max_length=20, null=True)),
                ('flag_mcap', models.CharField(blank=True, max_length=20, null=True)),
                ('flag_spread_yoy', models.CharField(blank=True, max_length=20, null=True)),
                ('flag_spread_3ya', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'unique_together': {('period', 'ticker')},
            },
        ),
    ]
