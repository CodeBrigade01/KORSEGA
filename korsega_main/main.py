from flask import Flask, request, render_template
import openai
from googleapiclient.discovery import build
import re

app = Flask(__name__, template_folder='template')

# Replace with your OpenAI GPT-3 API key
openai.api_key = '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'
lst2=[]
a=""
# HTML form to enter the skill name
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        skill_name = request.form.get("skill_name")
        topics = generate_skill_topics(skill_name)
        print("\nTopics related to", skill_name, "learning:")
        for i, topic in enumerate(topics, start=1):
            print(f"{i}. {topic}")
            url_list = re.findall(r"https://www\.youtube\.com/watch\?v=[^\s]+",topic)
            extracted_letters = [re.search(r'https://www\.youtube\.com/watch\?v=(\w+)', url).group(1) for url in url_list]
            #yt="https://www.youtube.com/embed/"
            global a
            a=str(extracted_letters)
            return render_template("index.html", video_id=a)
    
    return render_template("index.html", video_id=a)

# Generate subtopics using GPT-3
def generate_skill_topics(skill_name):
    # Define a prompt for GPT-3 to generate topics
    prompt = f"i need for learning {skill_name}. So give me a list of 30 youtube links of 10- 15min duration in which they teach only a single topic at a time"
    # Use the OpenAI API to generate topics
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can use a different engine if needed
        prompt=prompt,
        max_tokens=50,  # Adjust the length of the response as needed
        n=2  # Number of topics to generate
    )

    # Extract and return the generated topics
    topics = [choice["text"] for choice in response.choices]
    return topics

# Search for YouTube videos using the YouTube Data API

if __name__ == "__main__":
    app.run(debug=True)
