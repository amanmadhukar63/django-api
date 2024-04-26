from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DataSerializer
from textblob import TextBlob

def get_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

class HelloAPIView(APIView):
    def post(self, request):
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data['data']
            response_data = {'sentiment': get_sentiment(data)}
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

