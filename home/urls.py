from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .import views
urlpatterns = [
    path("", views.homepage,name="homepage"),
    path("contact", views.contactus,name="contact_us"),
    path('testpage', views.TestMethod, name="Sample"),
    path('aboutus', views.aboutus, name="AboutUs"),
    path('blogs', views.blogs, name="Blog"),
    path('contacts', views.contacts, name="Contact"),
    path('destinations', views.destinations, name="Destination"),
    path('guides', views.guides, name="Guide"),
    path('packages', views.packages, name="Package"),
    # path('panoramics',views.panoramics,name='Panoramic'),
    path('view3d/<id>', views.viewPlaces, name="placesviewurl"),
    path('services', views.services, name="Service"),
    path('singles', views.singles, name="Single"),
    path('testimonials', views.testimonials, name="Testimonial"),
    path('register',views.regUser,name='register_user'),
    path('login',views.logUser,name='log_user'),
    path('logout', views.logoutUsers, name="logoutUsers"),
    path('homepostlogins',views.homepagepost,name='Homepagepost')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()