from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from user.forms import UserUpdateForm 
from django.views.generic import UpdateView

def register(request):
    if request.method == 'POST':
       
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       password1 = request.POST['password1']

       print(username, email, password, password1)

       if password == password1:
           if User.objects.filter(username=username).exists():
               messages.info(request, 'Username Taken')

           elif User.objects.filter(email=email).exists():
               messages.info(request, 'Email Taken')


           else:
                user = User.objects.create_user(username, email=email, password=password)
                user.save()
                messages.info(request, 'User Successfully Created.')
                return redirect('login')

       else:
            messages.info(request, 'Passwords Not Matching')
            return redirect('register')

    return render(request, 'user/register.html')

    





@login_required
def update_user(request):
    if request.method == 'POST':
        user = request.user 
        old_password = request.POST['password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        # import pdb; pdb.set_trace()

        if new_password == confirm_password:
            if user.check_password(old_password) == True:
                user.set_password(new_password)
                user.save()
                messages.info(request, 'Password Successfully Changed')
                return redirect('login')

            else:
                messages.info(request, 'Wrong Password')
            
        else:
            messages.info(request, 'Passwords do not match.')


    return render(request, 'user/password_change.html')







def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(user)
        
        if  user is not None:
            auth.login(request, user)
            return redirect('list_photo')

        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    return render(request, 'user/login.html')




class UpdateUserView(UserPassesTestMixin ,LoginRequiredMixin ,UpdateView):
    model = User 
    template_name = 'user/update.html'
    context_object_name = 'user'
    success_url = '/profile/list_profile/'
    form_class = UserUpdateForm


    def form_valid(self, form):
        form.instance.username == self.request.user.username
        return super().form_valid(form)


    def test_func(self):
        user = self.get_object()
        if self.request.user == user:
            return True
        return False


