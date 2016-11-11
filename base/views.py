
from django.shortcuts import render
from django.conf import settings
from django.utils.http import is_safe_url
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView, View, RedirectView


class LoginView(View):

    template_name = 'login.html'

    def post(self, request, **kwargs):

        if request.user.is_authenticated():
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                next_url = request.GET.get('next', settings.LOGIN_REDIRECT_URL)
                if not is_safe_url(next_url):
                    next_url = settings.LOGIN_REDIRECT_URL

                return HttpResponseRedirect(next_url)
            else:
                context = {'state': 'Your account is not active, please contact the site admin.',
                           'username': username,
                           'next': request.GET.get('next', settings.LOGIN_REDIRECT_URL)}
                return render(request, self.template_name, context)
        else:
            context = {'state': 'Your username and/or password were incorrect.',
                       'username': username,
                       'next': request.GET.get('next', settings.LOGIN_REDIRECT_URL)}
            return render(request, self.template_name, context)

    def get(self, request, **kwargs):

        if request.user.is_authenticated():
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

        return render(request, self.template_name, {})

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)


class LogoutView(RedirectView):
    url = '/login/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    redirect_field_name = 'next'
    login_url = '/login/'
