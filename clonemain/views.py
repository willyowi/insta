from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Project,Profile,Comment
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from .models import Post
from .models import NewsLetterRecipients
from .forms import NewsLetterForm,NewPostForm
from .email import send_welcome_email

from .forms import ProfileForm,VoteForm,NewComment, NewsLetterForm, NewPostForm



# Create your views here.
def daily_post(request):
    date = dt.date.today()
    clonemain = Post.todays_post()

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name = name,email =email)
            
            recipient.save()
            # send_welcome_email
            send_welcome_email(name,email)
            
            HttpResponseRedirect('daily_post')
    else:
        form = NewsLetterForm()
    
    return render(request, 'all-post/today-post.html', {"date": date,"clonemain":clonemain,"form":form})


def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day 


def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-post/search.html',{"message":message,"posts": searched_posts})

=======
from .forms import ProjectForm,ProfileForm,VoteForm,NewComment

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    projects = Project.get_all()
    return render(request,'landing.html',{'projects':projects})
    
def project(request,project_id):
    project = Project.objects.get(id = project_id)
    rating = round(((project.userinterface)/2),2)
    # if request.method == 'POST':
    #     form = VoteForm(request.POST)
    #     if form.is_valid:
    #         if project.userinterface == 1:
    #             project.userinterface = int(request.POST['userinterface'])
    #         else:
    #             project.userinterface = (project.userinterface + int(request.POST['userinterface']))/2
        # form = VoteForm()
    current_user=request.user
    if request.method=='POST':
        form=NewComment(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.comment_owner=current_user
            comment.save()
          
            messages.success(request,f'Comment made') 
>>>>>>> revert
    else:
        form=NewComment()
    comments=Comment.get_comments(project_id)
    return render(request,'project.html',{'form':form,'project':project,'rating':rating,'comments':comments})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = current_user
            project.save()
        return redirect('indexPage')

    else:
        form = ProjectForm()
    return render(request, 'new_post.html', {"form": form})

def vote_project(request, project_id):
    project = Project.objects.get(id=project_id)
    rating = round(((project.userinterface)/2),2)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid:
            if project.userinterface == 1:
                project.userinterface = int(request.POST['userinterface'])
            else:
                project.userinterface = (project.userinterface + int(request.POST['userinterface']))/2
    else:
        form = VoteForm()
    return render(request,'vote.html',{'form':form,'project':project,'rating':rating})


def profile(request):
    current_user = request.user
    projects = Project.objects.filter(profile=current_user).all()
    profile = Profile.objects.filter(profile=current_user)

    if len(profile)<1:
        profile = "No profile"
    else:
        profile = Profile.objects.get(profile=current_user)

    return render(request, 'profile/profile.html',{'projects':projects,'profile':profile,'user':current_user})

def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.post = current_user
            profile.save()
            messages.success(request,'Your account has been updated')
        return redirect('Profile')
    else:
        form = ProfileForm()
    return render(request,'profile/edit_profile.html',{'form':form})

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

<<<<<<< HEAD
def vote_post(request, project_id):
    post = Post.objects.get(id=project_id)
    rating = round(((post.userinterface)/2),2)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid:
            if post.userinterface == 1:
                post.userinterface = int(request.POST['userinterface'])
            else:
                post.userinterface = (post.userinterface + int(request.POST['userinterface']))/2
    else:
        form = VoteForm()
    return render(request,'vote.html',{'form':form,'post':post,'rating':rating})
=======
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def search_project(request,project_id):
    try :
        project = Project.objects.get(id = project_id)

    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'project_details.html', {'project':project})
>>>>>>> revert



