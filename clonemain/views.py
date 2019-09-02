from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from .models import Post

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
    
    return render(request, 'all-post/today-post.html', {"date": date,"news":news,"letterForm":form})


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

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-post/search.html',{"message":message})




@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.editor = current_user
            post.save()
        return redirect('postToday')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})

