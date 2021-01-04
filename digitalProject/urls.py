"""digitalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include


from django.conf.urls.static import static
from django.conf import settings

# authentication

# simple jwt
# from rest_framework_simplejwt import views as jwt_views 


# jwt only

# from rest_framework_jwt.views import   obtain_jwt_token,  verify_jwt_token

# simple jwt auth
# from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView





urlpatterns = [
    path('admin/', admin.site.urls),


    # api url
    path('', include('LibraryBook.urls')), 

    # path('api-auth/', include('rest_framework.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # authencation

    # # simple auth
    # path('api/token/',TokenObtainPairView.as_view(), name ='token_obtain_pair'), 
    # path('api/token/refresh/',TokenRefreshView.as_view(), name ='token_refresh'),


    # # auth  simple
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    # jwt
    
    # path('api-token-auth/',obtain_jwt_token),
   
    # path('api-token-verify/',verify_jwt_token),

    # path('api-token-verify/',verify_jwt_token), 


    # path('auth-jwt/', obtain_jwt_token),
    # path('auth-jwt-refresh/', refresh_jwt_token),
    # path('auth-jwt-verify/', verify_jwt_token),







]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 