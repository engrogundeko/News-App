from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import DeleteView, UpdateView
from .models import Articles
from django.urls import reverse_lazy
from .forms import CommentForm
from django.views import View
# Create your views here.

class ArticleListView(LoginRequiredMixin, ListView):
    model = Articles
    template_name = 'article_list.html'
    context_object_name = 'article_list'


class CommentGet(LoginRequiredMixin, DetailView):
    model = Articles
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm 
        return context
    

class CommentPost(SingleObjectMixin, FormView):
    model = Articles
    template_name = 'article_detail.html'
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.articles = self.object
        comment.save()
        return super().form_valid(form)
    

    def get_success_url(self):
        article = self.get_object()
        return reverse('article_detail', kwargs={'pk': article.pk})



class ArticleDetailView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)

   # context_object_name = 'article_list'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articles
    template_name = 'article_update.html'
    fields = ['title',
        'body',]
    success_url = reverse_lazy('article_list')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

    
    #def get_success_url(self):
     #   return reverse_lazy('article_detail', kwargs={'pk': self.object.pk})
        
    
    
    #context_object_name = 'article_list'


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Articles
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    #context_object_name = 'article_list'


class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Articles
    template_name = 'article_create.html'
    success_url = reverse_lazy('article_list')
    fields = ['title',
       'body',]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    #context_object_name = 'article_list'
