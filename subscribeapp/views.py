from django.shortcuts import render, get_object_or_404
from django.views.generic import RedirectView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import ListView

from projectapp.models import Project
from articleapp.models import Article
from subscribeapp.models import Subscription

# Create your views here.


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):

        project = get_object_or_404(
            Project, pk=self.request.GET.get('project_pk'))

        user = self.request.user

        subcription = Subscription.objects.filter(user=user, project=project)

        if subcription.exists():
            subcription.delete()
        else:
            Subscription(user=user, project=project).save()

        return super(SubscriptionView, self).get(request, *args, **kwargs)


@method_decorator(login_required, 'get')
class SubscriptionListVeiw(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 5

    def get_queryset(self):
        projects = Subscription.objects.filter(
            user=self.request.user).values_list('project')
        article_list = Article.objects.filter(project__in=projects)
        return article_list
