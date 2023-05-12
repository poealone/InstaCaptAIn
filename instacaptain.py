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

# ASCII art title with attribution
f = Figlet(font='slant')
ascii_art = f.renderText("InstaCaptAIn") + "by poealone"
print(colored(ascii_art, "green"))

# Generate up to 5 posts
num_posts = input("Enter the number of posts (1-5): ")
num_posts = int(num_posts) if num_posts.isdigit() else 1
num_posts = max(1, min(num_posts, 5))  # Limit the number of posts between 1 and 5

for i in range(num_posts):
    print(colored(f"Post {i+1}", "cyan"))

    # Ask for the post text
    post_text = input("Enter the text for the Instagram post: ")

    caption, hashtags = generate_caption_and_hashtags(post_text)

    # Print the generated caption and hashtags
    print(colored("Generated Caption:", "yellow"))
    print(caption)

    print(colored("\nGenerated Hashtags:", "yellow"))
    for hashtag in hashtags:
        print(colored(hashtag, "magenta"))

    print()  # Add a blank line between posts
