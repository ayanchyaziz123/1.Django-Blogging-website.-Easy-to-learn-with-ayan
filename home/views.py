from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Post, Category, Contact, Comment, Sliders
from programmingTutorial.models import Language
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from .forms import Contact
from django.shortcuts import get_object_or_404
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse

# Create your views here.

def home(request):
    populer = Post.objects.all().order_by('-views')[0:10]
    Recent = Post.objects.all().order_by('-postTimeDate')[0:10]
    cat = Category.objects.all()
    slider = Sliders.objects.all().order_by('-date')[0:1]
    tc = Comment.objects.all().count()
    context = {'RecentPost': Recent,
               'Categories': cat, 
               'Populer': populer,
               'Slider': slider,
               'TotalComment': tc, }
    return render(request, 'home.html', context)

def blog(request):

    Posts = Post.objects.all().order_by('-postTimeDate')
    paginator = Paginator(Posts, 4)
    page = request.GET.get('page')

    #?page = 2

    Recent = Post.objects.all().order_by('-postTimeDate')[0:3]

    Posts = paginator.get_page(page)
    cat = Category.objects.all()
    populer = Post.objects.all().order_by('-views')[0:10]
    tc = Comment.objects.all().count()

    context = {'Posts': Posts,
               'RecentPost': Recent,
               'Categories': cat,
               'Populer': populer,
               'TC': tc,}
    return render(request, 'blog.html', context)


def readMore(request, slug):
    # return HttpResponse(f'this is blogPost : {slug}')

    Recent = Post.objects.all().order_by('-postTimeDate')[0:3]
    post = Post.objects.filter(postId=slug).first()
    cat = Category.objects.all()[0:3]
    populer = Post.objects.all().order_by('-views')[0:10]
    comment = BlogComment.objects.filter(post=post) 
    context = {'post': post,
               'RecentPost': Recent,
               'Categories': cat,
                'comments': comment,
                'Populer': populer, }
   
    return render(request, 'readMore.html', context)


def search(request):
    Recent = Post.objects.all().order_by('-postTimeDate')[0:3]
    populer = Post.objects.all().order_by('-views')[0:10]
    cat = Category.objects.all()
    Recent = Post.objects.all().order_by('-postTimeDate')[0:4]



    query = request.GET['search']
    if query =="":
        paginator = Paginator(Posts, 2)
        page = request.GET.get('page')
        Posts = paginator.get_page(page)
    else:
        Pag = Post.objects.filter(Q(postTitle__icontains=query) | Q(postDescriptions__contains=query))
        Posts = Pag
            

    parms = {'allPosts': Posts,
             'RecentPost': Recent,
             'Categories': cat,
             'query': query,
             'Populer': populer,}
    return render(request, 'search.html', parms)


def aboutMe(request):
    Recent = Post.objects.all().order_by('-postTimeDate')[0:3]
    cat = Category.objects.all()[0:3]
    context = {'RecentPost': Recent,
               'Categories': cat, }
    return render(request, 'aboutMe.html', context)




def categories(request, cat):
    # return HttpResponse(f'this is blogPost : {slug}')

    Recent = Post.objects.all().order_by('-postTimeDate')[0:3]
    allPosts = Post.objects.filter(Q(category__icontains=cat) | Q(postText__contains=cat))
    parms = {'allPosts': allPosts,
             'Categories': Category.objects.all(),
             'RecentPost': Recent}
    return render(request, 'home/category.html', parms)



def contactUs(request):
    context = {}
    populer = Post.objects.all().order_by('-views')[0:10]
    if request.POST:
        form = Contact(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message was added successfully.Thanks to you")
            context = {'form': form, 'RecentPost': Post.objects.all()[0:3],
                       'Categories': Category.objects.all(),
                       'Populer': populer,}
            return render(request, 'contact.html', context)
        else:
            messages.error(request, "Please fill the form correctly")
            context = {'form': form, 'RecentPost': Post.objects.all()[0:3],
                       'Categories': Category.objects.all(),
                       'Populer': populer,}
            return render(request, 'contact.html', context)
    else:  # GET request
        form = Contact()
        context = {'form': form, 'RecentPost': Post.objects.all()[0:3],
            'Categories': Category.objects.all(),
            'Populer': populer,}
    return render(request, 'contact.html', context)




def post_detail(request, post):

    
    past = Post.objects.filter(postId=post).first()
    
    past.views = past.views + 1
    past.save()
    populer = Post.objects.all().order_by('-views')[0:10]
    Recent = Post.objects.all().order_by('-postTimeDate')[0:3]
    cat = Category.objects.all()
    # get post object
    go_back = post
    post = get_object_or_404(Post, postId=post)
    # list of active parent comments
    comments = post.comments.filter(active=True, parent__isnull=True)
    if request.method == 'POST':
        # comment has been added
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                # if parent object exist
                if parent_obj:
                    # create replay comment object
                    replay_comment = comment_form.save(commit=False)
                    # assign parent_obj to replay comment
                    replay_comment.parent = parent_obj
            # normal comment
            # create comment object but do not save to database
            new_comment = comment_form.save(commit=False)
            # assign ship to the comment
            new_comment.post = post
            # save
            new_comment.save()
            return HttpResponseRedirect(reverse('readMore', args=[str(go_back)]))
    else:
        comment_form = CommentForm()
    return render(request,
                  'extra.html',
                  {'post': post,
                   'comments': comments,
                   'comment_form': comment_form,
                   'RecentPost': Recent,
               'Categories': cat,
               'Populer': populer,})





def category(request, cat):
    populer = Post.objects.all().order_by('-views')[0:10]
    Recent = Post.objects.all().order_by('-postTimeDate')[0:3]
    query = cat
    allPosts = Post.objects.filter(category__category__contains=query).order_by('-postTimeDate')
    cat = Category.objects.all()

    parms = {'allPosts': allPosts,
             'RecentPost': Recent,
             'Categories': cat,
             'Populer': populer}
    return render(request, 'category.html', parms)
    