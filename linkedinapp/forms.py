from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Company, EducationDetail, ExperienceDetail, JobLocation, JobPost, JobType, SeekerProfile, SeekerSkillSet, UserAccount

from linkedinapp.models import UserAccount


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ('user_id', 'usertype_name')


class SeekerProfileForm(forms.ModelForm):
    class Meta:
        model = SeekerProfile
        fields = ('useraccount_id', 'first_name', 'last_name',
                  'current_salary', 'is_annualy_monthly', 'currency')


class EducationDetailForm(forms.ModelForm):
    class Meta:
        model = EducationDetail
        fields = ('seekerprofile_id', 'degree_name', 'institute_name',
                  'starting_date', 'completition_date', 'percentage', 'cgpa')


class ExperienceDetailForm(forms.ModelForm):
    class Meta:
        model = ExperienceDetail
        fields = ('seekerprofile_id', 'is_current_job', 'job_title',
                  'job_description', 'start_date', 'end_date', 'company_name', 'company_address')


class SeekerSkillSetForm(forms.ModelForm):
    class Meta:
        model = SeekerSkillSet
        fields = ('seekerprofile_id', 'skill_name', 'skill_level')


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('useraccount_id', 'company_name', 'company_description',
                  'establishment_date', 'company_website_url')


class JobTypeForm(forms.ModelForm):
    class Meta:
        model = JobType
        fields = ('jobtype',)


class JobLocationForm(forms.ModelForm):
    class Meta:
        model = JobLocation
        fields = ('street_address', 'city', 'state',
                  'country', 'zip')


class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ('jobtype_id', 'company_id', 'joblocation_id',
                  'job_description', 'created_date', 'is_active')
