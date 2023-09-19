# from django.shortcuts import render, redirect
# import openai
# import re

# openai.api_key = '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'


# def generate_skill_topics(skill_name):
#     # Define a prompt for GPT-3 to generate topics
#     prompt = f"generate an ordered list of topics i need to learn basics of {skill_name}. also provide a relevant youtube link for each of those title. make sure to keep the same font throughout and generate the response containing only the title and links"
#     # Use the OpenAI API to generate topics
#     response = openai.Completion.create(
#         engine="text-davinci-002",  # You can use a different engine if needed
#         prompt=prompt,
#         max_tokens=50,  # Adjust the length of the response as needed
#         n=5  # Number of topics to generate
#     )
#     # Extract and return the generated topics
#     topics= [choice["text"] for choice in response.choices]
#     # print(topics)
#     # print(type(topics))
#     return topics

# def youtube_API(request):
#     lst2=[]
#     subtopcis = []
#     a=""
#     skill_name = request.GET.get("skill_name")
#     topics = generate_skill_topics(skill_name)
#     # print(topics)
#     print("\nTopics related to", skill_name, "learning:")
#     for i, topic in enumerate(topics, start=1):
#         # print(f"{i}. {topic}")
#         # print(i)
#         # print(topic)
#         url_list = re.findall(r"https://www\.youtube\.com/watch\?v=[^\s]+",topic)
#         extracted_letters = [re.search(r'https://www\.youtube\.com/watch\?v=(\w+)', url).group(1) for url in url_list]
#         a=str(extracted_letters)
#         print(type(a))
#         print(a)
#         yt="https://www.youtube.com/embed/" + a[2:len(a)-2]
#         lst2.append(yt)
#         subtopcis.append(i)
#         # print('this is a')
#         # print(a, end=" ")
#         # print('this is a end'

#     context = {
#             "subtopics":subtopcis,
#             "url_list":lst2
#         }
    
#     return render(request,"youtube.html",context)


import requests
from django.shortcuts import render, redirect
import openai
import re

openai.api_key = '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'

# Define the YouTube API endpoint for search
search_endpoint = "https://www.googleapis.com/youtube/v3/search"

def generate_skill_topics(skill_name):
    # Define a prompt for GPT-3 to generate topics
    prompt = f"Give me an ordered list of topics that I need to learn for learning {skill_name} from basics. Make sure that the generated response contains only the list of topics and nothing else. Do not include any text."
    # Use the OpenAI API to generate topics
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can use a different engine if needed
        prompt=prompt,
        max_tokens=50,  # Adjust the length of the response as needed
        n=1 # Number of topics to generate
        )
    # Extract and return the generated topics
    topics= [choice["text"] for choice in response.choices]

    # input_string = topics
    
    # topics_match = re.search(r'\((\d+),\s*(\'[^\']*\'\))', input_string)

    # if topics_match:
    #     topic_str = topics_match.group(2)
    #     topic_list = re.findall(r'\d+\.\s*([^0-9]+)', topic_str)
    #     print(topic_list)
    # else:
    #     print("No topics found in the input string.")

    return topics

def youtube_API(request):
    lst2=[]
    subtopcis = []
    a=""
    api_key = "AIzaSyDWcJzm1ZpjCG-M72NcF5jWKiLzw6tAomE"
    skill_name = request.GET.get("skill_name")
    topics = generate_skill_topics(skill_name)
    print("\nTopics related to", skill_name, "learning:")
    print(topics)
    n_topic = topics[0]

    for n_topic in topics:
        topic_list = n_topic.split('/n')
        topic_list = [word.strip() for word in topic_list if word.strip()]
        for topic in topic_list:
            print(type(topic))
            print(f". {topic}")
            print('/n')
            print('/n')
            query = topic
            params = {
                "q": query,
                "part": "snippet",
                "maxResults": 1,
                "type": "video",
                "key": api_key,
            }
            response = requests.get(search_endpoint, params=params)
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()

                # Check if there are search results
                if "items" in data:
                    # Extract the link of the first video
                    first_video = data["items"][0]
                    video_id = first_video["id"]["videoId"]
                    video_url = f"https://www.youtube.com/embed/{video_id}"
                    lst2.append(video_url)

                    # Print the link of the first video
                    print("Link to the first video:", video_url)
                else:
                    print("No search results found.")
            else:
                print("Error:", response.status_code)

    return render(request, "youtube.html", {"video_url": lst2, "subtopics": topics})