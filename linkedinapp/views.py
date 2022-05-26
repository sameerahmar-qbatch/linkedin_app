from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CompanyForm, EducationDetailForm, ExperienceDetailForm, JobLocationForm, JobPostForm, JobTypeForm, SeekerProfileForm, SeekerSkillSetForm, UserAccountForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from linkedinapp.models import Company, JobLocation, JobPost, JobType, SeekerSkillSet, UserAccount, SeekerProfile, EducationDetail, ExperienceDetail, User


def home(request):
    return render(request, 'linkedinapp/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Hi {username}, your account creation process has been started. Just provide little more details. Thankyou!')
            return redirect('useraccount')
    else:
        form = UserRegisterForm()

    return render(request, 'linkedinapp/register.html', {'form': form})


def useraccount(request):
    if request.method == "POST":
        form = UserAccountForm(request.POST)
        if form.is_valid():
            form.save()
            usertype_name = form.cleaned_data.get('usertype_name')
            messages.success(
                request, f'Thankyou, for specifying your role as {usertype_name}')
            if usertype_name == 'jobseeker':
                return redirect('seekerprofile')
            elif usertype_name == 'company':
                return redirect('company')
            # return redirect('profile')
    else:
        current_user = User.objects.last()
        form = UserAccountForm(initial={'user_id': current_user.id})

    return render(request, 'linkedinapp/useraccount.html', {'form': form})


@login_required
def profile(request):
    current_user = request.user
    current_user_type = UserAccount.objects.get(
        user_id=current_user.id).usertype_name
    if current_user_type == 'jobseeker':
        # try:
        jobseeker = SeekerProfile.objects.get(
            useraccount_id=current_user.id)
        jobseeker_education = jobseeker.educationdetail_set.first()
        jobseeker_experience = jobseeker.experiencedetail_set.first()
        jobseeker_skillset = jobseeker.seekerskillset_set.first()
        if jobseeker_education is None:
            messages.success(
                request, 'Your Education Details Are Missing.')
        if jobseeker_experience is None:
            messages.success(
                request, 'Your Experience Details Are Missing.')
        if jobseeker_skillset is None:
            messages.success(
                request, 'Your SkillSet Details Are Missing.')
        return redirect('educationdetail')
        # except:
        #    return redirect('seekerprofile')

    elif current_user_type == 'company':
        return redirect('jobtype')

    return render(request, 'linkedinapp/profile.html')


def seekerprofile(request):

    if request.method == "POST":
        form = SeekerProfileForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            messages.success(
                request, f'Thankyou {first_name}, for completing the account creation process successfully. Kindly Sign In Now.')
            return redirect('profile')
    else:
        current_user = User.objects.last()
        form = SeekerProfileForm(initial={'useraccount_id': current_user.id})

    return render(request, 'linkedinapp/seekerprofile.html', {'form': form})


def educationdetail(request):
    if request.method == "POST":
        form = EducationDetailForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            messages.success(
                request, 'Thankyou, for setting up the education details in your profile. If you want to add up another details, fill up the form again, otherwise shift to the experience detail form through the following link')
            return redirect('educationdetail')
    else:
        current_user = request.user
        form = EducationDetailForm(
            initial={'seekerprofile_id': current_user.id})

    return render(request, 'linkedinapp/educationdetail.html', {'form': form})


def experiencedetail(request):
    if request.method == "POST":
        form = ExperienceDetailForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Thankyou, for setting up the experience details in your profile. If you want to add up another details, fill up the form again, otherwise shift to the skillset form through the following link')
            return redirect('experiencedetail')
    else:
        current_user = request.user
        form = ExperienceDetailForm(
            initial={'seekerprofile_id': current_user.id})

    return render(request, 'linkedinapp/experiencedetail.html', {'form': form})


def seekerskillset(request):
    if request.method == "POST":
        form = SeekerSkillSetForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            messages.success(
                request, 'Thankyou, for setting up the education details in your profile. If you want to add up another details, fill up the form again, otherwise shift to the home through the following link')
            return redirect('seekerskillset')
    else:
        current_user = request.user
        form = SeekerSkillSetForm(
            initial={'seekerprofile_id': current_user.id})

    return render(request, 'linkedinapp/seekerskillset.html', {'form': form})


def company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            company_name = form.cleaned_data.get('company_name')
            messages.success(
                request, f'Thankyou {company_name}, for completing the account creation process successfully. Kindly Sign In Now.')
            return redirect('profile')
    else:
        current_user = User.objects.last()
        form = CompanyForm(initial={'useraccount_id': current_user.id})

    return render(request, 'linkedinapp/company.html', {'form': form})


def jobtype(request):
    if request.method == "POST":
        form = JobTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Thankyou for specifying the job type')
            return redirect('joblocation')
    else:
        form = JobTypeForm()

    return render(request, 'linkedinapp/jobtype.html', {'form': form})


def joblocation(request):
    if request.method == "POST":
        form = JobLocationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Thankyou for specifying the job location')
            return redirect('jobpost')
    else:
        form = JobLocationForm()

    return render(request, 'linkedinapp/joblocation.html', {'form': form})


def jobpost(request):
    if request.method == "POST":
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Job has been posted successfully!')
            return redirect('home')
    else:
        current_user = request.user
        company_jobtype = JobType.objects.last()
        company_joblocation = JobLocation.objects.last()
        jobpost_dict = {
            'company_id': current_user.id,
            'joblocation_id': company_joblocation,
            'jobtype_id': company_jobtype
        }
        form = JobPostForm(initial=jobpost_dict)

    return render(request, 'linkedinapp/jobpost.html', {'form': form})


def userdetail(request):
    current_user = request.user
    current_user_type = UserAccount.objects.get(
        user_id=current_user.id).usertype_name
    userdetail_dict = {
        'current_user_type': current_user_type
    }
    if current_user_type == 'jobseeker':
        jobseeker = SeekerProfile.objects.get(useraccount_id=current_user.id)
        jobseeker_education = jobseeker.educationdetail_set.all()
        jobseeker_experience = jobseeker.experiencedetail_set.all()
        jobseeker_skillset = jobseeker.seekerskillset_set.all()
        userdetail_dict['first_name'] = jobseeker.first_name
        userdetail_dict['last_name'] = jobseeker.last_name
        userdetail_dict['current_salary'] = jobseeker.current_salary
        userdetail_dict['is_annualy_monthly'] = jobseeker.is_annualy_monthly
        userdetail_dict['currency'] = jobseeker.currency
        if jobseeker_education is not None:
            userdetail_dict['degree_name'] = list()
            userdetail_dict['institute_name'] = list()
            userdetail_dict['starting_date'] = list()
            userdetail_dict['completition_date'] = list()
            userdetail_dict['percentage'] = list()
            userdetail_dict['cgpa'] = list()
            for jobseeker_education in jobseeker_education.iterator():
                userdetail_dict['degree_name'].append(
                    jobseeker_education.degree_name)
                userdetail_dict['institute_name'].append(
                    jobseeker_education.institute_name)
                userdetail_dict['starting_date'].append(
                    jobseeker_education.starting_date)
                userdetail_dict['completition_date'].append(
                    jobseeker_education.completition_date)
                userdetail_dict['percentage'].append(
                    jobseeker_education.percentage)
                userdetail_dict['cgpa'].append(jobseeker_education.cgpa)
        else:
            messages.success(
                request, 'Education Details are Missing')
        if jobseeker_experience is not None:
            userdetail_dict['is_current_job'] = list()
            userdetail_dict['start_date'] = list()
            userdetail_dict['end_date'] = list()
            userdetail_dict['job_title'] = list()
            userdetail_dict['job_description'] = list()
            userdetail_dict['company_name'] = list()
            userdetail_dict['company_address'] = list()
            for jobseeker_experience in jobseeker_experience.iterator():
                userdetail_dict['is_current_job'].append(
                    jobseeker_experience.is_current_job)
                userdetail_dict['start_date'].append(
                    jobseeker_experience.start_date)
                userdetail_dict['end_date'].append(
                    jobseeker_experience.end_date)
                userdetail_dict['job_title'].append(
                    jobseeker_experience.job_title)
                userdetail_dict['job_description'].append(
                    jobseeker_experience.job_description)
                userdetail_dict['company_name'].append(
                    jobseeker_experience.company_name)
                userdetail_dict['company_address'].append(
                    jobseeker_experience.company_address)

        else:
            messages.success(
                request, 'Experience Details are Missing')
        if jobseeker_skillset is not None:
            userdetail_dict['skill_name'] = list()
            userdetail_dict['skill_level'] = list()
            for jobseeker_skillset in jobseeker_skillset.iterator():
                userdetail_dict['skill_name'].append(
                    jobseeker_skillset.skill_name)
                userdetail_dict['skill_level'].append(
                    jobseeker_skillset.skill_level)
        else:
            messages.success(
                request, 'SkillSet Details are Missing')
        return render(request, 'linkedinapp/jobseekeruserdetail.html', userdetail_dict)
    elif current_user_type == 'company':
        company = Company.objects.get(useraccount_id=current_user.id)
        company_jobpost = company.jobpost_set.all()
        userdetail_dict['company_name'] = company.company_name
        userdetail_dict['company_description'] = company.company_description
        userdetail_dict['establishment_date'] = company.establishment_date
        userdetail_dict['company_website_url'] = company.company_website_url
        if company_jobpost is not None:
            userdetail_dict['job_description'] = list()
            userdetail_dict['is_active'] = list()
            for company_jobpost in company_jobpost.iterator():
                userdetail_dict['job_description'].append(
                    company_jobpost.job_description)
                userdetail_dict['is_active'].append(
                    company_jobpost.is_active)
        else:
            messages.success(
                request, 'No job has been posted yet!')
        return render(request, 'linkedinapp/companyuserdetail.html', userdetail_dict)
