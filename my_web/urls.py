from django.contrib.sitemaps.views import sitemap
from django.urls import path
from .sitemaps import PostSitemap, QuoteSitemap, FactSitemap, InfoSitemap
from . import views

sitemaps_posts = {
    'posts': PostSitemap,
}

sitemaps_quotes = {
    'quotes': QuoteSitemap,
}

sitemaps_facts = {
    'facts': FactSitemap,
}

sitemaps_info = {
    'facts': InfoSitemap,
}

urlpatterns = [
    path('', views.index, name='index_page'),
    path('info/', views.info, name='info_page'),
    path('status', views.status, name='status_page'),
    path('stats', views.stats, name='stats_page'),
    path('bot', views.botpage, name='bot_page'),
    path('load_more', views.load_more, name='load_more'),
    path('post/', views.error_400, name='postaddr'),
    path('quote/', views.error_400, name='quoteaddr'),
    path('fact/', views.error_400, name='factaddr'),
    path('aware/', views.error_400, name='awareaddr'),
    path('story/', views.error_400, name='storyaddr'),
    path('quote/<str:quoteid>/', views.quoteview),
    path('post/<str:postid>/', views.postview),
    path('fact/<str:factid>/', views.factview),
    path('aware/<str:awareid>/', views.awareview),
    path('story/<str:storyid>/', views.storyview),
    path('image/', views.image_proxy_view, name='imageproxy'),
    path('sitemap_posts_time_to_upgrade.xml', sitemap, {'sitemaps': sitemaps_posts},
         name='django.contrib.sitemaps.views.sitemap'),
    path('sitemap_quotes_time_to_upgrade.xml', sitemap, {'sitemaps': sitemaps_quotes},
         name='django.contrib.sitemaps.views.sitemap'),
    path('sitemap_facts_time_to_upgrade.xml', sitemap, {'sitemaps': sitemaps_facts},
         name='django.contrib.sitemaps.views.sitemap'),
]
