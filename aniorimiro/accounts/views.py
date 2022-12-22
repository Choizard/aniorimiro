from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from accounts.forms import CreateUserForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings

def index(request):
  return render(request, 'index.html')

User = get_user_model()

class ProfileView(LoginRequiredMixin, TemplateView):
  template_name = 'accounts/profile.html'

profile = ProfileView.as_view()

@login_required
def update(request):
  if request.method == 'POST':
    user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
    if user_change_form.is_valid():
        user_change_form.save()
        return redirect('/accounts/profile', request.user.username)
  else:
    user_change_form = CustomUserChangeForm(instance = request.user)
    return render(request, 'accounts/update.html', {
                          'user_change_form':user_change_form
                          })


signup = CreateView.as_view(
  model = User,
  form_class = CreateUserForm,
  success_url = settings.LOGIN_URL,
  template_name = 'accounts/signup.html',

)
