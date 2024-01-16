from django.urls import path
from .views import index, earth, mars, venus

urlpatterns = [
    path('', index, name='main-page'),
    path('earth/', earth, name='earth-page'),
    path('mars/', mars, name='mars-page'),
    path('venus/', venus, name='venus-page')

]