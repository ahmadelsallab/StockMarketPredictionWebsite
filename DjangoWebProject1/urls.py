"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm


# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'app.views.index', name='index'),
    url(r'^prototype$', 'app.views.index_proto', name='index_proto'),
    url(r'^home_proto$', 'app.views.home_proto', name='home_proto'),
    url(r'^home$', 'app.views.home', name='home'),
    url(r'^get_hours_distribution$', 'app.views.get_hours_distribution', name='get_hours_distribution'),
    url(r'^get_stacked_sentiment$', 'app.views.get_stacked_sentiment', name='get_stacked_sentiment'),
    url(r'^get_tweeter_by_sname$', 'app.views.get_tweeter_by_sname', name='get_tweeter_by_sname'),
    url(r'^get_tweets_by_tweeter$', 'app.views.get_tweets_by_tweeter', name='get_tweets_by_tweeter'),
    url(r'^profile/(.*)/$', 'app.views.profile', name='profile'),
    url(r'^home_filtered$', 'app.views.home_filtered', name='home_filtered'),
    url(r'^test123$', 'app.views.test123', name='test123'),
    url(r'^get_tweets_proto$', 'app.views.get_tweets_proto', name='get_tweets_proto'),
    url(r'^get_tweets_filtered$', 'app.views.get_tweets_filtered', name='get_tweets_filtered'),
    url(r'^get_stock_price$', 'app.views.get_stock_price', name='get_stock_price'),
    url(r'^get_stock_price_by_id$', 'app.views.get_stock_price_by_id', name='get_stock_price_by_id'),
    url(r'^p_table$', 'app.views.p_table', name='p_table'),
    url(r'^h_table$', 'app.views.h_table', name='h_table'),
    url(r'^c_table$', 'app.views.c_table', name='c_table'),
    url(r'^ch_table$', 'app.views.ch_table', name='ch_table'),
    url(r'^get_tweets_predicted$', 'app.views.get_tweets_predicted', name='get_tweets_predicted'),
    url(r'^get_news$', 'app.views.get_news', name='get_news'),
    url(r'^add_tweet_by_ref$', 'app.views.add_tweet_by_ref', name='add_tweet_by_ref'),
    url(r'^get_tweets$', 'app.views.get_tweets', name='get_tweets'),
    url(r'^get_prices_line', 'app.views.get_prices_line', name='get_prices_line'),
    url(r'^get_prices_candle', 'app.views.get_prices_candle', name='get_prices_candle'),
    url(r'^get_stock_volume', 'app.views.get_stock_volume', name='get_stock_volume'),
    url(r'^get_overall_stats', 'app.views.get_overall_stats', name='get_overall_stats'),
    url(r'^get_last_100', 'app.views.get_last_100', name='get_last_100'),
    url(r'^get_overall_rel_info', 'app.views.get_overall_rel_info', name='get_overall_rel_info'),
    url(r'^get_overall_sent_info', 'app.views.get_overall_sent_info', name='get_overall_sent_info'),
    url(r'^get_stock_rel_info', 'app.views.get_stock_rel_info', name='get_stock_rel_info'),
    url(r'^get_stock_sent_info', 'app.views.get_stock_sent_info', name='get_stock_sent_info'),
    url(r'^get_stock_col_rel_info', 'app.views.get_stock_col_rel_info', name='get_stock_col_rel_info'),
    url(r'^get_stock_col_sent_info', 'app.views.get_stock_col_sent_info', name='get_stock_col_sent_info'),
    url(r'^get_stocks_weights', 'app.views.get_stocks_weights', name='get_stocks_weights'),
    url(r'^get_correction', 'app.views.get_correction', name='get_correction'),    
    url(r'^correct', 'app.views.correct', name='correct'),    
    url(r'^contact', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^login_proto/authenticated/?$', 'app.views.twitter_authenticated', name='twitter_authenticated'),
    url(r'^login_proto', 'app.views.login_user_proto', name='login_proto'),
    url(r'^login', 'app.views.login_user', name='login'),
    url(r'^register', 'app.views.register', name='register'),
    url(r'^twitter_register', 'app.views.twitter_register', name='twitter_register'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/prototype',}, name='logout'),
    url(r'^news', 'app.views.news', name='news'),
    url(r'^update_counters', 'app.views.update_counters', name='update_counters'),
    url(r'^statistics$', 'app.views.home_statistics', name='statistics'),
    url(r'^filtered$', 'app.views.home_filtered', name='filtered'),
    url(r'^training$', 'app.views.home_training', name='training'),
    url(r'^train_filters', 'app.views.train_filters', name='train_filters'),
    url(r'^evaluate_filters', 'app.views.evaluate_filters', name='evaluate_filters'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
