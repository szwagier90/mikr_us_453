from django.shortcuts import render

from django.urls import reverse, reverse_lazy

from django.views.generic.edit import FormView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'mysite/index.html')

class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        form.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)

        next_page = self.request.GET.get('next', default=None)
        print("form_valid")
        print(next_page)
        if next_page:
            self.success_url = next_page
        else:
            self.success_url = reverse('index')

        return super(RegisterView, self).form_valid(form)
