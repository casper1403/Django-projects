from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm ,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# requires crispyforms (also in settings)


def Register(request):
    # Check if post
    if request.method == 'POST':
        #setup the form
        form = UserRegisterForm(request.POST)
        print("1", form)
        #Check if form is valid
        if form.is_valid():
            print("2", form)
            #save the form
            form.save()
            #Fetch the username
            username = form.cleaned_data.get('username')
            #print a message to the screen
            messages.success(request, f'Your account has been created, you can now login')
            # Redict to index (note: Message is implemented in layout.html so that its site wide)
            return redirect('users:Login')
    else:
        # If the form is not valid return just the form
        form = UserRegisterForm()
    # If request is not post retrn the html page
    return render(request, 'users/register.html', {'form': form})


@login_required
def Profile(request):

    # Init the forms which can change database user data
    if request.method == 'POST':

        # Call the form classes from the form.py file
        # the vairables are the default information shown in the form
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance = request.user.profile)

        # IF the form is Valid safe it to the database and show succes message
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Account updated')
            return redirect('users:Profile')
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Account updated')
            return redirect('users:Profile')
    # if form not filled in still show the default user info
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    # let the browser know what the different forms are.
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)
