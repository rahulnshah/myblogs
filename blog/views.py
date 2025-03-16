from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, CodeSnippet
from django.utils import timezone 
from .forms import PostForm, NameForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
 # Both views.py and models.py are in the same directory. This means we can use . 
# and the name of the file (without .py). 
# Then we import the name of the model (Post).


# Create your views here.
def post_list(request):
    # Note: Control blocks like If statements in Python do not count and the variables used or initialized inside the block of an If statement can also be used and accessed outside its scope. 
    posts = Post.objects.all() # returns a queryset 
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            #fetch the search results
            posts = Post.objects.all().filter(text__contains=form.cleaned_data['your_name']) # returns a queryset 
            return render(request, 'blog/post_list.html', {'posts' : posts, "form" : form})
    else:
        form = NameForm()
    return render(request, 'blog/post_list.html', {'posts' : posts, "form" : form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # The following example gets the object with the primary key pk from Post
    return render(request, 'blog/post_detail.html', {'post': post})
    
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            # Handle code snippets
            descriptions = request.POST.getlist('snippet_description[]')
            languages = request.POST.getlist('snippet_language[]')
            codes = request.POST.getlist('snippet_code[]')
            
            for description, language, code in zip(descriptions, languages, codes):
                if code.strip():  # Only create snippet if code is not empty
                    CodeSnippet.objects.create(
                        post=post,
                        description=description,
                        language=language,
                        code=code
                    )
            
            return redirect('post_detail', pk=post.pk)
    else: # if a GET (or any other method) we'll create a blank form; This is what we can expect to happen the first time we visit the URL.
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            # Handle code snippets
            descriptions = request.POST.getlist('snippet_description[]')
            languages = request.POST.getlist('snippet_language[]')
            codes = request.POST.getlist('snippet_code[]')
            snippet_ids = request.POST.getlist('snippet_id[]')  # For existing snippets

            # Delete removed snippets
            existing_ids = [int(id) for id in snippet_ids if id]
            post.snippets.exclude(id__in=existing_ids).delete()

            # Update or create snippets
            for i in range(len(descriptions)):  # Use descriptions length since all snippets have description
                description = descriptions[i]
                language = languages[i]
                code = codes[i]
                
                if i < len(snippet_ids) and snippet_ids[i]:  # Check if we have a valid ID
                    # Update existing snippet
                    snippet = CodeSnippet.objects.get(id=snippet_ids[i])
                    snippet.description = description
                    snippet.language = language
                    snippet.code = code
                    snippet.save()
                else:
                    # Create new snippet
                    CodeSnippet.objects.create(
                        post=post,
                        description=description,
                        language=language,
                        code=code
                    )

            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'post': post})
    
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('post_list')
            else:
                # Add error message for invalid credentials
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('post_list')  # Redirect to the post list page after logout

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_delete.html', {'post': post})