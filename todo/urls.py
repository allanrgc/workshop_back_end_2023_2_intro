from rest_framework import routers
from .views import ToDoListViewSet, PessoaViewSet

router = routers.DefaultRouter()
router.register(r'', ToDoListViewSet)
router.register(r'pessoa', PessoaViewSet)
urlpatterns = router.urls