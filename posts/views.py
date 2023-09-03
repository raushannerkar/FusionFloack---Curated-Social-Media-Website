import os
from typing import Optional
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, CreateView
from django.views.generic.base import View
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile
from django.http import JsonResponse


def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'posts/home.html',context)

@login_required
def frames(request):
    return render(request, 'posts/frames.html')

@login_required
def technology(request):
    technology_posts = Post.objects.filter(topic='technology').order_by('-date_posted')
    context = {'posts': technology_posts}
    return render(request, 'topics/technology.html', context)

@login_required
def animals(request):
    animals_posts = Post.objects.filter(topic='animals').order_by('-date_posted')
    context = {'posts': animals_posts}
    return render(request, 'topics/animals.html', context)

@login_required
def automobiles(request):
    automobiles_posts = Post.objects.filter(topic='automobiles').order_by('-date_posted')
    context = {'posts': automobiles_posts}
    return render(request, 'topics/automobiles.html', context)

@login_required
def humour(request):
    humour_posts = Post.objects.filter(topic='humour').order_by('-date_posted')
    context = {'posts': humour_posts}
    return render(request, 'topics/humour.html', context)

@login_required
def nature(request):
    nature_posts = Post.objects.filter(topic='nature').order_by('-date_posted')
    context = {'posts': nature_posts}
    return render(request, 'topics/nature.html', context)

@login_required
def news(request):
    news_posts = Post.objects.filter(topic='news').order_by('-date_posted')
    context = {'posts': news_posts}
    return render(request, 'topics/news.html', context)

@login_required
def money(request):
    money_posts = Post.objects.filter(topic='money').order_by('-date_posted')
    context = {'posts': money_posts}
    return render(request, 'topics/money.html', context)

@login_required
def entertainment(request):
    entertainment_posts = Post.objects.filter(topic='entertainment').order_by('-date_posted')
    context = {'posts': entertainment_posts}
    return render(request, 'topics/entertainment.html', context)

@login_required
def motivational(request):
    motivational_posts = Post.objects.filter(topic='motivational').order_by('-date_posted')
    context = {'posts': motivational_posts}
    return render(request, 'topics/motivational.html', context)

@login_required
def sports(request):
    sports_posts = Post.objects.filter(topic='sports').order_by('-date_posted')
    context = {'posts': sports_posts}
    return render(request, 'topics/sports.html', context)

@login_required
def art(request):
    art_posts = Post.objects.filter(topic='art').order_by('-date_posted')
    context = {'posts': art_posts}
    return render(request, 'topics/art.html', context)

@login_required
def clips(request):
    clips_posts = Post.objects.filter(topic='clips').order_by('-date_posted')
    context = {'posts': clips_posts}
    return render(request, 'topics/clips.html', context)


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['caption', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TopicPostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['caption', 'content', 'topic'] 

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, username):
        profile_user = User.objects.get(username=username)
        user_posts = Post.objects.filter(user=profile_user)
        context = {
            'user_posts': user_posts,
            'profile_user': profile_user,
        }

        if request.user.is_authenticated:
            current_user_profile = Profile.objects.get(user=request.user)
            context['current_user_profile'] = current_user_profile

        return render(request, 'posts/profile2.html', context)



@login_required
def follow(request):
    if request.method == 'POST':
        follower_profile = request.user.profile
        user_id = request.POST['user_id']
        profile_user = User.objects.get(id=user_id).profile

        if follower_profile.following.filter(id=profile_user.id).exists():
            follower_profile.following.remove(profile_user)
        else:
            follower_profile.following.add(profile_user)

        # Update followers count for both profiles
        follower_profile.update_followers_count()
        profile_user.update_followers_count()

        return redirect('profile2', username=profile_user.user.username)
    else:
        return redirect('posts-home')


    
@login_required 
def search(request):
    username_profile_list = []  

    if request.method == 'POST':
        username = request.POST['username']
        matching_users = User.objects.filter(username__icontains=username)
        
        for user in matching_users:
            user_profile = Profile.objects.get(user=user)  
            username_profile_list.append(user_profile)

    return render(request, 'posts/search.html', {'username_profile_list': username_profile_list})

    
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return JsonResponse({'liked': liked, 'likes_count': post.likes.count()})

@login_required
def followers_list(request, username):
    user = User.objects.get(username=username)
    profile = user.profile
    followers = profile.get_followers()
    context = {
        'profile_user': user,
        'followers': followers,
    }
    return render(request, 'posts/followers_list.html', context)








