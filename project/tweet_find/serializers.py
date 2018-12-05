from rest_framework import serializers
from .forms import TickerSymbol

class TickerSymbolSerializer(serializers.FormSerializer):
    class Meta:
        form = TickerSymbol
        field = ("ticker_symbol")

