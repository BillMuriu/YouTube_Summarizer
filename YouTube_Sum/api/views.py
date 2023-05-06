import openai
from django.shortcuts import render
from django.http import JsonResponse


from langchain.document_loaders import YoutubeLoader
from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list',
    }
    return Response(api_urls)

# @api_view(['POST'])
# def openai_api(request):
#     prompt = request.data.get('prompt')
#     openai.api_key = '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'
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=prompt,
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )

#     text = response.choices[0].text
#     return Response({'text': text})


@api_view(['POST'])
def openai_api(request):
    youtube_url = request.data.get('url')
    loader = YoutubeLoader.from_youtube_url(youtube_url, add_video_info=True)
    result = loader.load()
    llm = OpenAI(temperature=0, openai_api_key='')
    chain = load_summarize_chain(llm, chain_type="stuff", verbose=False)
    chain.run(result)
    return Response(str(result))