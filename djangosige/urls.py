# -*- coding: utf-8 -*-

from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from .configs.settings import DEBUG, MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djangosige.apps.base.urls')),
    path('login/', include('djangosige.apps.login.urls', namespace='login')),
    path('cadastro/', include('djangosige.apps.cadastro.urls', namespace='cadastro')),
    path('fiscal/', include('djangosige.apps.fiscal.urls', namespace='fiscal')),
    path('vendas/', include('djangosige.apps.vendas.urls', namespace='vendas')),
    path('compras/', include('djangosige.apps.compras.urls', namespace='compras')),
    path('financeiro/', include('djangosige.apps.financeiro.urls', namespace='financeiro')),
    path('estoque/', include('djangosige.apps.estoque.urls', namespace='estoque')),
]

if DEBUG is True:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
