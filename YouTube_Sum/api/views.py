import openai
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list',
    }
    return Response(api_urls)

@api_view(['POST'])
def openai_api(request):
    prompt = request.data.get('prompt')
    # replace 'YOUR_API_KEY' with your actual OpenAI API key
    openai.api_key = ''
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text = response.choices[0].text
    return Response({'text': text})