from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('garage-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        ru_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                        instance=request.user.userprofileadditional)  #UserProfileAdditional
        if u_form.is_valid() and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')
        else:
            messages.error(request, f'Please fill in missing fields.')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofileadditional)  #UserProfileAdditional

    # if request.method == 'POST':
    #     form = PasswordChangeForm(request.user ,request.POST)
    #     if form.is_valid():
    #         form.save()
    #         update_session_auth_hash(request, User)
    #         messages.success(request, f'Your password was successfully updated!')
    #         return redirect('profile')
    #     else:
    #         messages.error(request, f'Please correct the error below.')
    # else:
    #     form = PasswordChangeForm(request.user)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)



    



