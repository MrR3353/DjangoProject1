"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<int:product_pk>/<int:adding>/<int:employer_id2>/', views.catalog_buy, name='catalog'),
    path('catalog/<int:product_pk>/<int:adding>/', views.catalog_buy, name='catalog'),
    path('add_product/', views.add_product, name='add_product'),
    path('del_product/<int:product_id>', views.del_product, name='del_product'),
    path('create_product/', views.create_product, name='create_product'),
    path('shoplist/', views.shoplist, name='shoplist'),
    path('orders/', views.orders, name='orders'),
    path('make_order/', views.make_order, name='make_order'),
    path('manage_orders/', views.manage_orders, name='manage_orders'),
    path('change_order/<int:order_id>/<str:status>', views.change_order, name='change_order'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('links/', views.links, name='links'),
    path(r'anketa', views.anketa, name='anketa'),
    # path(r'^anketa$', views.anketa, name='anketa'),
    path('registration/', views.registration, name='registration'),
    path('blog/', views.blog, name='blog'),
    path('blogpost/<int:parametr>/', views.blogpost, name='blogpost'),
    path('newpost/', views.newpost, name='newpost'),
    path('videopost/', views.videopost, name='videopost'),

    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Войти',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
