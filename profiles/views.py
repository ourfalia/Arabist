from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def profile_view(request):
    """ A view to return the index page """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
