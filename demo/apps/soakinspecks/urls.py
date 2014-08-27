""" Urls for hello app
"""
from rest_framework import routers

from soakinspecks import views as ss_views

router = routers.DefaultRouter(trailing_slash=False)
router.register('/flavors', ss_views.FlavorViewset)
router.register('/orders', ss_views.OrderViewset)
router.register('/mixtures', ss_views.MixtureViewset)
router.register('/mixture-parts', ss_views.MixturePartViewset)
router.register('/production-batches', ss_views.ProductionBatchViewSet)
router.register('/order-process-batches', ss_views.OrderProcessBatchViewSet)
router.register('/inventories', ss_views.InventoryViewset)

urlpatterns = router.urls
