from django.urls import path
from stock.views import AllStockAPI, addStock, deleteStock, stock, itemAdjustment, updateStock


urlpatterns = [

    path('', stock, name = 'stock'),
    path('add-stock/', addStock, name = 'add-stock'),
    path('update-stock/<str:stock_id>/', updateStock, name = 'update-stock'),
    path('delete-stock/<str:stock_id>/', deleteStock, name = 'delete-stock'),
    path('item-adjustment/', itemAdjustment, name = 'item-adjustment'),
    path('all_stock_api/', AllStockAPI.as_view(), name = 'all_stock_api'),

]