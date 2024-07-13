from django.urls import path, include
from .views import ImportApiView

urlpatterns = [
    path('import/',ImportApiView.as_view(), name='import_view'),
]