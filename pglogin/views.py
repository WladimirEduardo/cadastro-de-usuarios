from django.shortcuts import reverse
from django.views.generic import TemplateView, FormView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import Usuario
from django.contrib.auth.models import User
from django.urls import reverse_lazy

#cadastrar usuario
class Cadastro(FormView):
    template_name = 'cadastro.html'
    form_class = Usuario
    

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
            
    def get_success_url(self):
        return reverse('login')

#area de configuracoes
class Logado(LoginRequiredMixin, TemplateView):
    template_name= 'logado.html'


class Configuracao(LoginRequiredMixin, TemplateView):
    template_name = 'confi.html'

class Deletar(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'delete.html'
    success_url = reverse_lazy('login')
