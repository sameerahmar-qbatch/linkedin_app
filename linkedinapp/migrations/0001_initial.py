# Generated by Django 4.0.4 on 2022-05-10 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('zip', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtype', models.CharField(choices=[('fulltime', 'Full Time'), ('parttime', 'Part Time')], max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertype_name', models.CharField(choices=[('jobseeker', 'Job Seeker'), ('company', 'Company')], max_length=9)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('useraccount_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='linkedinapp.useraccount')),
                ('company_name', models.CharField(max_length=50)),
                ('company_description', models.TextField()),
                ('establishment_date', models.DateField()),
                ('company_website_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='SeekerProfile',
            fields=[
                ('useraccount_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='linkedinapp.useraccount')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('current_salary', models.IntegerField()),
                ('is_annualy_monthly', models.CharField(choices=[('annualy', 'Annualy'), ('monthly', 'Monthly')], max_length=7)),
                ('currency', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_description', models.TextField()),
                ('created_date', models.DateField()),
                ('is_active', models.CharField(choices=[('true', 'True'), ('false', 'False')], max_length=5)),
                ('joblocation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linkedinapp.joblocation')),
                ('jobtype_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linkedinapp.jobtype')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linkedinapp.company')),
            ],
        ),
        migrations.CreateModel(
            name='SeekerSkillSet',
            fields=[
                ('skill_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('skill_level', models.CharField(choices=[('beginner', 'Beginner'), ('average', 'Average'), ('skilled', 'Skilled'), ('specialist', 'Specialist'), ('expert', 'Expert')], max_length=10)),
                ('seekerprofile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linkedinapp.seekerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='JobPostActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_date', models.DateField()),
                ('jobpost_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linkedinapp.jobpost')),
                ('seekerprofile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linkedinapp.seekerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceDetail',
            fields=[
                ('is_current_job', models.CharField(choices=[('true', 'True'), ('false', 'False')], max_length=5)),
                ('job_title', models.CharField(max_length=50)),
                ('job_description', models.TextField()),
                ('start_date', models.DateField(primary_key=True, serialize=False)),
                ('end_date', models.DateField()),
                ('company_name', models.CharField(max_length=50)),
                ('company_address', models.TextField()),
                ('seekerprofile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linkedinapp.seekerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='EducationDetail',
            fields=[
                ('degree_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('institute_name', models.CharField(max_length=50)),
                ('starting_date', models.DateField()),
                ('completition_date', models.DateField()),
                ('percentage', models.FloatField()),
                ('cgpa', models.FloatField()),
                ('seekerprofile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='linkedinapp.seekerprofile')),
            ],
        ),
    ]
