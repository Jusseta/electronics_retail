from rest_framework.routers import DefaultRouter
from chain.apps import ChainConfig
from chain.views import RetailChainViewSet, ProductViewSet, ContactsViewSet

app_name = ChainConfig.name


router = DefaultRouter()
router.register(r'chain', RetailChainViewSet, basename='chain')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'contacts', ContactsViewSet, basename='contacts')


urlpatterns = [] + router.urls
