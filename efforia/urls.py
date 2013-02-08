from django.conf.urls import patterns,url,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       
    (r'^$','core.views.main'),
    (r'^config','core.views.config'),
    (r'^profile','core.views.profile'),
    (r'^place','core.views.place'),
    (r'^password','core.views.password'),
    (r'^integrations','core.views.integrations'),
    (r'^enter','core.views.authenticate'),
    (r'^leave','core.views.leave'),
    (r'^delete','core.views.delete'),
    (r'^userid','core.views.ids'),
    (r'^activity','core.views.search'),
    (r'^explore','core.views.search'),
    (r'^known','core.views.explore'),
    (r'^favorites','core.views.favorites'),
    (r'^fan','core.views.fan'),
    
    (r'^products','store.views.main'),
    (r'^store','store.views.init_store'),
    (r'^cart','store.views.cart'),
    (r'^cancel','store.views.cancel'),
    (r'^payment','store.views.payment'),
    (r'^discharge','store.views.discharge'),
    (r'^recharge','store.views.recharge'),
    (r'^balance','store.views.balance'),
    (r'^delivery','store.views.delivery'),
    (r'^correios','store.views.mail'),
    (r'^paypal','store.views.paypal_ipn'),
    
    (r'^spreadable','spread.views.spreadable'),
    (r'^spreads','spread.views.init_spread'),
    (r'^spread','spread.views.main'),
    (r'^calendar','spread.views.event'),
    (r'^contents','spread.views.content'),
    (r'^schedule','spread.views.schedule'),
    (r'^collection','spread.views.collection'),
    (r'^expose','spread.views.upload'),
    (r'^content','spread.views.collection'),
    
    (r'^causes','create.views.main'),
    (r'^create','create.views.init_create'),
    (r'^movement','create.views.movement'),
    
    # Examples:
    # url(r'^$', 'efforia.views.home', name='home'),
    # url(r'^efforia/', include('efforia.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()