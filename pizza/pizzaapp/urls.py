from django.urls import path
from django.contrib import admin
from .views import adminloginview ,adminhomepageview , authenticateadmin , logoutadmin, addpizza , deletepizza, homepageview , signupuser, userloginview , customerwelcomeview,userauthenticate , userlogout, placeorder , userorders, adminorders , acceptorder , declineorder

urlpatterns=[
    path('admin/',adminloginview , name='adminloginpage'),
    path('adminauthenticate/', authenticateadmin),
    path('admin/homepage/', adminhomepageview, name='adminhomepage'),
    path('adminlogout/', logoutadmin),
    path('addpizza/', addpizza),
    path('deletepizza/<int:pizzapk>/', deletepizza),
    path('', homepageview, name='homepage'),
    path('signupuser/',signupuser),
    path('loginuser/',userloginview, name='userloginpage'),
    path('customer/welcome/',customerwelcomeview, name='customerpage'),
    path('customer/authenticate/', userauthenticate),
    path('userlogout/',userlogout),
    path('placeorder/', placeorder),
    path('userorders/', userorders),
    path('adminorders/',adminorders),
    path('acceptorder/<int:orderpk>/',acceptorder),
    path('declineorder/<int:orderpk>/',declineorder),
]