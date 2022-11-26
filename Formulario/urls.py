"""Formulario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from pglogin.views import Logado, Cadastro, Deletar, Configuracao



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('cadastro/', Cadastro.as_view(template_name = 'cadastro.html'), name='cadastro'),
    path('logado/', Logado.as_view(template_name = 'logado.html'), name='logado'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'logout.html'), name='logout'),
    path('editarsenha/<int:pk>/', auth_views.PasswordChangeView.as_view(template_name='editarsenha.html',
    success_url = reverse_lazy('logado')), name='editarsenha'),
    path('deletar/<int:pk>/', Deletar.as_view(template_name='delete.html'), name='deletar' ),
    path('configuracao/', Configuracao.as_view(template_name = 'confi.html'), name='configuracao')
]


#configuracoes de arquivos
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

