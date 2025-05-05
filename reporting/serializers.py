from rest_framework import serializers

from reporting.models import Order

class OrderSerializer(serializers.ModelSerializer):
    # 内部类
    class Meta:
        # 告诉序列化器用哪个模型
        model = Order 
        # 要序列化的字段
        fields = ['id', 'amount', 'description', 'created_time']