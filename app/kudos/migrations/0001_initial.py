# Generated by Django 2.1.2 on 2018-10-19 23:13

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0109_bounty_funding_organisation'),
    ]

    operations = [
        migrations.CreateModel(
            name='KudosTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('web3_type', models.CharField(default='v3', max_length=50)),
                ('emails', django.contrib.postgres.fields.jsonb.JSONField(blank=True)),
                ('url', models.CharField(blank=True, default='', max_length=255)),
                ('tokenName', models.CharField(default='ETH', max_length=255)),
                ('tokenAddress', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=4, default=1, max_digits=50)),
                ('comments_public', models.TextField(blank=True, default='')),
                ('ip', models.CharField(max_length=50)),
                ('github_url', models.URLField(blank=True, null=True)),
                ('from_name', models.CharField(blank=True, default='', max_length=255)),
                ('from_email', models.CharField(blank=True, default='', max_length=255)),
                ('from_username', models.CharField(blank=True, default='', max_length=255)),
                ('username', models.CharField(blank=True, default='', max_length=255)),
                ('network', models.CharField(default='', max_length=255)),
                ('txid', models.CharField(default='', max_length=255)),
                ('receive_txid', models.CharField(blank=True, default='', max_length=255)),
                ('received_on', models.DateTimeField(blank=True, null=True)),
                ('from_address', models.CharField(blank=True, default='', max_length=255)),
                ('receive_address', models.CharField(blank=True, default='', max_length=255)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('is_for_bounty_fulfiller', models.BooleanField(default=False, help_text='If this option is chosen, this tip will be automatically paid to the bounty fulfiller, not self.usernameusername.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('price_finney', models.IntegerField()),
                ('num_clones_allowed', models.IntegerField(blank=True, null=True)),
                ('num_clones_in_wild', models.IntegerField(blank=True, null=True)),
                ('cloned_from_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=510)),
                ('image', models.CharField(max_length=255, null=True)),
                ('rarity', models.CharField(max_length=255, null=True)),
                ('tags', models.CharField(max_length=255, null=True)),
                ('artist', models.CharField(blank=True, max_length=255, null=True)),
                ('platform', models.CharField(blank=True, max_length=255, null=True)),
                ('external_url', models.CharField(max_length=255, null=True)),
                ('background_color', models.CharField(max_length=255, null=True)),
                ('owner_address', models.CharField(max_length=255)),
                ('txid', models.CharField(blank=True, max_length=255, null=True)),
                ('contract_address', models.CharField(max_length=255)),
                ('token_id', models.IntegerField()),
                ('network', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('address', models.CharField(max_length=255, unique=True)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kudos_wallets', to='dashboard.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='kudostransfer',
            name='kudos_token',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kudos_transfer', to='kudos.Token'),
        ),
        migrations.AddField(
            model_name='kudostransfer',
            name='kudos_token_cloned_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kudos_token_cloned_from', to='kudos.Token'),
        ),
        migrations.AddField(
            model_name='kudostransfer',
            name='recipient_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_kudos', to='dashboard.Profile'),
        ),
        migrations.AddField(
            model_name='kudostransfer',
            name='sender_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_kudos', to='dashboard.Profile'),
        ),
    ]
