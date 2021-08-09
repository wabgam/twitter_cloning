from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from .models import Tweet 
from .forms import TweetForm, EditForm

# Create your views here.
def index(request):
    # If the method is TWEET
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
         # If the form is valid
        if form.is_valid():
              # Yes, Save
              form.save()
              # Redirect to Home
              return HttpResponseRedirect('/')
        else:
              # No, Show Error
              return HttpResponseRedirect(form.error.as_json())

    # Get all tweets, limit = 20
    tweets = Tweet.objects.all()[:20]

    # show
    return render(request, 'tweets.html', 
                  {'tweets': tweets})
    
def delete(request, tweet_id):
    # Find tweet
    tweet = Tweet.objects.get(id = tweet_id)
    tweet.delete()
    return HttpResponseRedirect('/')

def edit(request, tweet_id):
  # Get requested tweet
  tweet = Tweet.objects.get(id = tweet_id)
  form = TweetForm()
  # If the method is TWEET
  if request.method == 'POST':
    form = TweetForm(request.POST, request.FILES, instance=tweet)
    if form.is_valid():
      # Save and redirect to home
      form.save()
      return HttpResponseRedirect('/')
    else:
      print(form.errors)

    # Show editting screen
  return render(request, 'Edit.html',
    {'tweet': tweet, 'form': form})



def like(request, tweet_id):
  tweet = Tweet.objects.get(id = tweet_id)
  new_like = tweet.like + 1
  tweet.like = new_like
  tweet.save()
  return HttpResponseRedirect('/')