import openai
from django.shortcuts import render
from django.http import JsonResponse
from langchain.document_loaders import YoutubeLoader
from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain
from youtube_transcript_api import YouTubeTranscriptApi
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list',
    }
    return Response(api_urls)


openai.api_key = ''
def summarize_text(text):
        prompt = f"Please summarize the following text:\n\n{text}\n\nSummary:"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        summary = response.choices[0].text.strip()
        return summary


@api_view(['POST'])
def openai_api(request):
    video_id = 'uKrnx81zdnQ'
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    text_list = []
    for transcript in transcript_list:
        text_list.append(transcript['text'])

    coherent_structure = ' '.join(text_list)

    if len(coherent_structure.split()) > 1000:
        chunks = [coherent_structure[i:i+1000] for i in range(0, len(coherent_structure), 1000)]
        summaries = []
        for chunk in chunks:
            summary = summarize_text(chunk)
            summaries.append(summary)
        final_summary = summarize_text(' '.join(summaries))
    else:
        final_summary = summarize_text(coherent_structure)

    return Response(final_summary)