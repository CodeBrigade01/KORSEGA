from django.shortcuts import render, redirect
import openai
import re

openai.api_key = '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'





def generate_skill_topics(skill_name):
    # Define a prompt for GPT-3 to generate topics
    prompt = f"generate an ordered list of topics i need to learn basics of {skill_name}. also provide a relevant youtube link for each of those title. make sure to keep the same font throughout and generate the response containing only the title and links"
    # Use the OpenAI API to generate topics
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can use a different engine if needed
        prompt=prompt,
        max_tokens=50,  # Adjust the length of the response as needed
        n=5  # Number of topics to generate
    )

    # Extract and return the generated topics
    topics= [choice["text"] for choice in response.choices]
    # print(topics)
    # print(type(topics))
    return topics

def youtube_API(request):
    lst2=[]
    subtopcis = []
    a=""
    skill_name = request.GET.get("skill_name")
    topics = generate_skill_topics(skill_name)
    # print(topics)
    print("\nTopics related to", skill_name, "learning:")
    for i, topic in enumerate(topics, start=1):
        # print(f"{i}. {topic}")
        # print(i)
        # print(topic)
        url_list = re.findall(r"https://www\.youtube\.com/watch\?v=[^\s]+",topic)
        extracted_letters = [re.search(r'https://www\.youtube\.com/watch\?v=(\w+)', url).group(1) for url in url_list]
        a=str(extracted_letters)
        print(type(a))
        print(a)
        yt="https://www.youtube.com/embed/" + a[2:len(a)-2]
        lst2.append(yt)
        subtopcis.append(i)
        # print('this is a')
        # print(a, end=" ")
        # print('this is a end'

    context = {
            "subtopics":subtopcis,
            "url_list":lst2
        }
    
    return render(request,"youtube.html",context)
    
    