from django import template
from users.models import Profile

register = template.Library()

@register.filter(name='is_liked_by_user')
def is_liked_by_user(post, user):
    return post.is_liked_by_user(user)

@register.filter(name='is_following')
def is_following(profile_user, current_user):
    try:
        profile = Profile.objects.get(user=current_user)
        return profile.following.filter(user=profile_user).exists()
    except Profile.DoesNotExist:
        return False
