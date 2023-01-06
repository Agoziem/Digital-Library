from django.urls import path
from .views import *

app_name = 'Resources'
urlpatterns = [
    path('', home_view, name='departments'),
    path('<int:id>/<str:level>/', department_view, name='department'),
    # path('update_item/', updateItem, name='update_item'),
    # path('delete_item/', delete_item, name='delete_item'),
    # path('review_item/', review_item, name='review_item'),
    # path('like/', like_book, name='like_book'),
]