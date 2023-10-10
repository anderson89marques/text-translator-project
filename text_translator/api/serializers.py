from rest_framework import serializers


class TranslateSerializer(serializers.Serializer):
    language_from = serializers.CharField(required=True)
    language_to = serializers.CharField(required=True)
    text = serializers.CharField(required=True)

class TranslateResponseSerializer(TranslateSerializer):
    text_translated = serializers.CharField(required=True)