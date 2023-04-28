from rest_framework import serializers
from stock.models import Stock


class StockDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = ["id", "name", "item_class", "quantity", "selling_price", "cost_price", "shelf_number", "expiry_date"]

    
    def get(self, validated_data):
        print("data", validated_data)
