
import requests
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from text_translator.api.serializers import (TranslateResponseSerializer,
                                             TranslateSerializer)
from text_translator.service import TranslatorService


@extend_schema(
    request=TranslateSerializer,
    responses={status.HTTP_200_OK: TranslateResponseSerializer},
)
@api_view(["POST"])
def translate(request):
    serializer = TranslateSerializer(data=request.data)
    if serializer.is_valid():
        try:
            service = TranslatorService()
            data = service.translate(serializer.data)
            response_serializer = TranslateResponseSerializer(data)
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        except requests.exceptions.HTTPError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    request=TranslateSerializer,
    responses={status.HTTP_200_OK: TranslateResponseSerializer},
)
@api_view(["POST"])
def translate_cache(request):
    serializer = TranslateSerializer(data=request.data)
    if serializer.is_valid():
        try:
            service = TranslatorService()
            data = service.translate(serializer.data)
            response_serializer = TranslateResponseSerializer(data)
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        except requests.exceptions.HTTPError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
