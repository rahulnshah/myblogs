from django.shortcuts import render, get_object_or_404, redirect
from .models import Post 
from django.utils import timezone 
from .forms import PostForm
from .forms import NameForm
 # Both views.py and models.py are in the same directory. This means we can use . 
# and the name of the file (without .py). 
# Then we import the name of the model (Post).


# Create your views here.
def post_list(request):
    posts = Post.objects.all() # returns a queryset 
    post_Query_Set = posts.filter(published_date__lte=timezone.now()).order_by('published_date') # also a query set 
    return render(request, 'blog/post_list.html', {'posts' : post_Query_Set})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # The following example gets the object with the primary key pk from Post
    return render(request, 'blog/post_detail.html', {'post': post})
    
def post_new(request): 
    if request.method == "POST": # if any field is filled, this will become true 
        form = PostForm(request.POST)
        if form.is_valid(): # else Django will tell me what to correct 
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else: # if a GET (or any other method) we'll create a blank form; This is what we can expect to happen the first time we visit the URL.
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
         # Create a form to edit an existing Article, but use
            # POST data to populate the form.
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    

def search_post(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:, blank field is not allowed by deafualt in Django, so same behavior will apply here as in methods above
        if form.is_valid():
            posts = Post.objects.all().filter(text__contains=form.cleaned_data['your_name']) # returns a queryset 
            return render(request, 'blog/search_results.html', {'posts' : posts})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'blog/name.html', {'form': form})