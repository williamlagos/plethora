from django.conf.urls import patterns,url,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django_pagseguro.urls import pagseguro_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$','core.views.main'),
    (r'^mosaic','core.views.mosaic'),
    (r'^config','core.views.config'),
    (r'^profile','core.views.profile'),
    (r'^photo','core.views.photo'),
    (r'^appearance','core.views.appearance'),
    (r'^options','core.views.options'),
    (r'^place','core.views.place'),
    (r'^password','core.views.password'),
    (r'^integrations','core.views.integrations'),
    (r'^enter','core.views.authenticate'),
    (r'^leave','core.views.leave'),
    (r'^delete','core.views.delete'),
    (r'^userid','core.views.ids'),
    (r'^search','core.views.search'),
    (r'^explore','core.views.search'),
    (r'^known','core.views.explore'),
    (r'^activity','core.views.activity'),
    (r'^following','core.views.following'),
    (r'^follow','core.views.follow'),
    (r'^unfollow','core.views.unfollow'),
    (r'^twitter/post','core.views.twitter_post'),
    (r'^facebook/post','core.views.facebook_post'),
    (r'^facebook/event','core.views.facebook_event'),
    (r'^participate','core.views.participate'),
    (r'^tutorial','core.views.tutorial'),
    (r'^pagseguro','core.views.pagseguro'),
    (r'^paypal','core.views.paypal'),
    (r'^pages','core.views.page'),
    (r'^pageview','core.views.pageview'),
    (r'^pageedit','core.views.pageedit'),
    (r'^discharge','core.views.discharge'),
    (r'^recharge','core.views.recharge'),
    (r'^balance','core.views.balance'),

    (r'^products','spread.views.store_main'),
    (r'^cart','spread.views.cart'),
    (r'^cancel','spread.views.cancel'),
    (r'^payment','spread.views.payment'),
    (r'^delivery','spread.views.delivery'),
    (r'^correios','spread.views.mail'),
    (r'^spreadable','spread.views.spreadable'),
    (r'^spreaded','spread.views.spreaded'),
    (r'^spreadspread','spread.views.spreadspread'),
    (r'^spreads','spread.views.init_spread'),
    (r'^spread','spread.views.main'),
    (r'^playable','spread.views.playable'),
    (r'^images','spread.views.image'),
    (r'^image','spread.views.imageview'),
    (r'^contents','spread.views.content'),
    (r'^expose','spread.views.upload'),
    (r'^media','spread.views.media'),
    (r'^productimage','spread.views.product_image'),
    
    (r'^projects','promote.views.main'),
    (r'^create','promote.views.init_create'),
    (r'^backers','promote.views.backers'),
    (r'^movements','promote.views.movements'),
    (r'^promote','promote.views.promote'),
    (r'^project','promote.views.project'),
    (r'^linkproj','promote.views.link'),
    (r'^movement','promote.views.movement'),
    (r'^pledge','promote.views.pledge'),
    (r'^grab','promote.views.grab'),
    (r'^deadlines','promote.views.deadlines'),
    (r'^event','promote.views.eventview'),
    (r'^calendar','promote.views.event'),
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += pagseguro_urlpatterns()
