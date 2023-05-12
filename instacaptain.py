import openai
from pyfiglet import Figlet
from termcolor import colored


openai.api_key = 'YOUR_API_KEY'  # Replace with your OpenAI API key

def generate_caption_and_hashtags(post_text):
    prompt = f"Generate a caption and hashtags for an Instagram post:\n\n{post_text}\n\n---\nCaption:"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,  # Adjust the length of the generated caption as desired
        n=1,
        stop=None,
        temperature=0.7
    )
    caption = response.choices[0].text.strip()

    prompt = f"Generate hashtags for the Instagram post:\n\n{caption}\n\n---\nHashtags:"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=30,  # Adjust the number of hashtags as desired
        n=1,
        stop=None,
        temperature=0.7
    )
    hashtags = [tag.strip() for tag in response.choices[0].text.strip().split("\n")]

    return caption, hashtags

# ASCII art title
f = Figlet(font='slant')
print(colored(f.renderText("InstaCaptAIn"), "green"))

# Ask for the post text
post_text = input("Enter the text for the Instagram post: ")

caption, hashtags = generate_caption_and_hashtags(post_text)

# Print the generated caption and hashtags
print("Generated Caption:")
print(caption)

print("\nGenerated Hashtags:")
for hashtag in hashtags:
    print(hashtag)

