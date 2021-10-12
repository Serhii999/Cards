from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class CardCreateView(CreateView):
    model = Card
    form_class = CardCreateForm
    success_url = '/'
    template_name = 'card_create.html'


class CardListView(ListView):
    model = Card
    template_name = 'main.html'


class Login(LoginView):
    template_name = 'login.html'


class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'


class DeleteCardView(PermissionRequiredMixin, DeleteView):
    permission_required = 'is_superuser'
    model = Card
    success_url = '/'


class UpdateCardView(PermissionRequiredMixin, UpdateView):
    form_class = CardCreateForm
    permission_required = 'is_superuser'
    model = Card
    template_name = 'update_card.html'
    success_url = '/'


class SearchResultsView(ListView):
    model = Card
    template_name = 'results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Card.objects.filter(
            Q(name__icontains=query) | Q(surname__icontains=query)
            | Q(country__icontains=query) | Q(city__icontains=query)
            | Q(avenue__icontains=query)
        )
        return object_list
