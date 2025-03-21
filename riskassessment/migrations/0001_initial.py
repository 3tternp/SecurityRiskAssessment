# Generated by Django 3.1.7 on 2021-04-13 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tc_name', models.CharField(max_length=100, verbose_name='Name')),
                ('tc_email', models.EmailField(max_length=100, verbose_name='Email')),
                ('tc_phone', models.CharField(max_length=10, verbose_name='Phone')),
                ('exst_contract', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Under Negotiation', 'Under Negotiation')], max_length=18)),
                ('vend_has_perm', models.BooleanField(default=False, verbose_name='Vendor can edit?')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Vendor Information',
                'verbose_name_plural': 'Vendor Information',
            },
        ),
        migrations.CreateModel(
            name='SWIntegrity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Software Integrity Question 1')),
                ('q2', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Software Integrity Question 2')),
                ('q3', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Software Integrity Question 3')),
                ('q4', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Software Integrity Question 4')),
                ('q5', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Software Integrity Question 5')),
                ('vend_has_perm', models.BooleanField(default=False, verbose_name='Vendor can edit?')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Software Integrity',
                'verbose_name_plural': 'Software Integrity',
            },
        ),
        migrations.CreateModel(
            name='SecureDesign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Secure Design Question 1')),
                ('q2', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Secure Design Question 2')),
                ('q3', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Secure Design Question 3')),
                ('q4', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Secure Design Question 4')),
                ('q5', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Secure Design Question 5')),
                ('q6', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Secure Design Question 6')),
                ('vend_has_perm', models.BooleanField(default=False, verbose_name='Vendor can edit?')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Secure Design',
                'verbose_name_plural': 'Secure Design',
            },
        ),
        migrations.CreateModel(
            name='SecureComms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Secure Communications Question 1')),
                ('q2', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Secure Communications Question 2')),
                ('q3', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Secure Communications Question 3')),
                ('q4', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Secure Communications Question 4')),
                ('q5', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Secure Communications Question 5')),
                ('q6', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Secure Communications Question 6')),
                ('q7', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Secure Communications Question 7')),
                ('q8', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Secure Communications Question 8')),
                ('vend_has_perm', models.BooleanField(default=False, verbose_name='Vendor can edit?')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Secure Communications',
                'verbose_name_plural': 'Secure Communications',
            },
        ),
        migrations.CreateModel(
            name='SecMatEvidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attst_o_comp', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Attestation of Compliance')),
                ('soc2_reports', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Current system’s vendor 3rd party SOC2 Type 2 reports')),
                ('ann_pen_scan_results', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Annual penetration/vulnerability scanning results of all system components')),
                ('ann_wa_vuln_scan', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Annual web application vulnerability scan of all system web applications')),
                ('vend_has_perm', models.BooleanField(default=False, verbose_name='Vendor can edit?')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Security Maturity Evidence',
                'verbose_name_plural': 'Security Maturity Evidence',
            },
        ),
        migrations.CreateModel(
            name='QAEnvironment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Quality Assurance Environment Question 1')),
                ('q2', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Quality Assurance Environment Question 2')),
                ('q3', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Quality Assurance Environment Question 3')),
                ('q4', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Quality Assurance Environment Question 4')),
                ('q5', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Quality Assurance Environment Question 5')),
                ('vend_has_perm', models.BooleanField(default=False, verbose_name='Vendor can edit?')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Quality Assurance Environment',
                'verbose_name_plural': 'Quality Assurance Environment',
            },
        ),
        migrations.CreateModel(
            name='Integration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sso', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Single Sign-on')),
                ('mfa', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Multi-Factor Authentication')),
                ('adfs', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Active Directory Federation Services')),
                ('vend_has_perm', models.BooleanField(default=False, verbose_name='Vendor can edit?')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Integration',
                'verbose_name_plural': 'Integration',
            },
        ),
        migrations.CreateModel(
            name='Encryption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p1q1', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Encryption Part 1 - Question 1')),
                ('p1q2', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Encryption Part 1 - Question 2')),
                ('p1q3', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Encryption Part 1 - Question 3')),
                ('p1q4', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Encryption Part 1 - Question 4')),
                ('p1q5', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Encryption Part 1 - Question 5')),
                ('p1q6', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Encryption Part 1 - Question 6')),
                ('p1q7', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Encryption Part 1 - Question 7')),
                ('p1q8', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Encryption Part 1 - Question 8')),
                ('p1q9', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Encryption Part 1 - Question 9')),
                ('p2q1', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Encryption Part 2 - Question 1')),
                ('p2q2', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Encryption Part 2 - Question 2')),
                ('p2q3', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Encryption Part 2 - Question 3')),
                ('p2q4', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Encryption Part 2 - Question 4')),
                ('p2q5', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Encryption Part 2 - Question 5')),
                ('p2q6', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Encryption Part 2 - Question 6')),
                ('p2q7', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Encryption Part 2 - Question 7')),
                ('vend_has_perm', models.BooleanField(default=False, verbose_name='Vendor can edit?')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Encryption',
                'verbose_name_plural': 'Encryption',
            },
        ),
        migrations.CreateModel(
            name='DeptInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ta_name', models.CharField(max_length=100, verbose_name='Name')),
                ('ta_email', models.EmailField(max_length=100, verbose_name='Email')),
                ('ta_phone', models.CharField(max_length=10, verbose_name='Phone')),
                ('eur_name', models.CharField(max_length=100, verbose_name='Name')),
                ('eur_email', models.EmailField(max_length=100, verbose_name='Email')),
                ('eur_phone', models.CharField(max_length=10, verbose_name='Phone')),
                ('ds_name', models.CharField(max_length=100, verbose_name='Name')),
                ('ds_email', models.EmailField(max_length=100, verbose_name='Email')),
                ('ds_phone', models.CharField(max_length=10, verbose_name='Phone')),
                ('vend_has_perm', models.BooleanField(default=False, verbose_name='Vendor can edit?')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Department Information',
                'verbose_name_plural': 'Department Information',
            },
        ),
        migrations.CreateModel(
            name='DataManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_data', models.CharField(max_length=5, verbose_name='Regulated Data')),
                ('data_classi', models.CharField(max_length=16, verbose_name='Data Classification')),
                ('recs_in_data', models.IntegerField(choices=[('500', '500'), ('1000', '1000'), ('2000', '2000'), ('3000', '3000'), ('4000', '4000'), ('5000', '5000'), ('6000', '6000'), ('7000', '7000')], verbose_name='Number of Records in Data')),
                ('recs_purged', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Are records purged from Data?')),
                ('est_add_recs', models.IntegerField(choices=[('500', '500'), ('1000', '1000'), ('2000', '2000'), ('3000', '3000'), ('4000', '4000'), ('5000', '5000'), ('6000', '6000'), ('7000', '7000')], verbose_name='Estimated yearly additional records')),
                ('data_process_outside', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Is data processing performed outside the US?')),
                ('data_stored_outside', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Is data stored outside the US?')),
                ('data_rcvd_outside', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Is any data received (directly or indirectly by ASU) from individuals outside of the US?')),
                ('data_accss_outside', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Are data or Systems accessible outside the US?')),
                ('vend_has_perm', models.BooleanField(default=False, verbose_name='Vendor can edit?')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Data Management',
                'verbose_name_plural': 'Data Management',
            },
        ),
        migrations.CreateModel(
            name='DatabaseServers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Database Servers Question 1')),
                ('q2', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Database Servers Question 2')),
                ('q3', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Database Servers Question 3')),
                ('q4', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Database Servers Question 4')),
                ('q5', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Database Servers Question 5')),
                ('q6', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Database Servers Question 6')),
                ('vend_has_perm', models.BooleanField(default=False, verbose_name='Vendor can edit?')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Database Servers',
                'verbose_name_plural': 'Database Servers',
            },
        ),
        migrations.CreateModel(
            name='Compliance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sso', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Single Sign-on Systems?')),
                ('audit_req_std_comp', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Company System Audit Requirements Standard Compliant?')),
                ('auto_patch', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Vendor Provides automated patching?')),
                ('vend_has_perm', models.BooleanField(default=False, verbose_name='Vendor can edit?')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Compliance',
                'verbose_name_plural': 'Compliance',
            },
        ),
        migrations.CreateModel(
            name='CloudService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saas_sol', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Is this a SaaS solution?')),
                ('iaas_hosted', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Is it hosted in IaaS owned by the Company?')),
                ('on_prem', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name="Is the solution built on premises in the Company's datacenter?")),
                ('vend_has_perm', models.BooleanField(default=False, verbose_name='Vendor can edit?')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Cloud Service Model',
                'verbose_name_plural': 'Cloud Service Model',
            },
        ),
        migrations.CreateModel(
            name='AvailabiltyCriticality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_rating', models.CharField(choices=[('Tier 1', 'Tier 1'), ('Tier 2', 'Tier 2'), ('Tier 3', 'Tier 3')], max_length=6, verbose_name='Availability Rating')),
                ('c_rating', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=6, verbose_name='Criticality Rating')),
                ('vend_has_perm', models.BooleanField(default=False, verbose_name='Vendor can edit?')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Availabilty and Criticality',
                'verbose_name_plural': 'Availabilty and Criticality',
            },
        ),
    ]
