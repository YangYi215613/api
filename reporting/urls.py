from reporting.views import ReportingViewSet, OrderViewSet
from django.urls import path, include

from rest_framework.routers import DefaultRouter


"""
router 是 Django REST Framework（DRF）中用于自动生成 URL 路由的工具，它专门为 ViewSet 类型的视图服务。

例子：

创建了一个默认路由器。把 OrderViewSet 注册到了路由器上，路径前缀是 'orders'。

DRF 会自动生成如下 API：

    GET /orders/ → 列表
    POST /orders/ → 创建 
    GET /orders/<pk>/ → 详情
    PUT /orders/<pk>/ → 修改
    DELETE /orders/<pk>/ → 删除
"""
router = DefaultRouter()
router.register('orders', OrderViewSet, basename='orders')

urlpatterns = [
    path('reporting/', ReportingViewSet.as_view(), name='reporting'),
    path('', include(router.urls))
]