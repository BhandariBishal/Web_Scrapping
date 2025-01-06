# Import required libraries
import requests
from bs4 import BeautifulSoup

# Base URL for the API
BASE_URL = "https://jsonplaceholder.typicode.com"

# GET request to fetch posts
def fetch_posts():
    # Send GET request to the posts endpoint
    response = requests.get(f"{BASE_URL}/posts")
    # Check if request was successful
    if response.status_code == 200:
        posts = response.json()
        for post in posts[:5]:  # Display first 5 posts
            print(f"Post ID: {post['id']}, Title: {post['title']}")
    else:
        print("Failed to fetch posts")

# POST request to create a new post
def create_post():
    # Data to be sent in POST request
    new_post = {
        "title": "New Blog Post",
        "body": "This is the content of my new blog post",
        "userId": 1
    }
    # Send POST request with JSON data
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    if response.status_code == 201:
        print(f"Post created successfully with ID: {response.json()['id']}")
    else:
        print("Failed to create post")

# PUT request to update an existing post
def update_post(post_id=1):
    # Updated data
    updated_data = {
        "title": "Updated Title",
        "body": "This post has been updated",
        "userId": 1
    }
    # Send PUT request
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=updated_data)
    if response.status_code == 200:
        print(f"Post {post_id} updated successfully")
    else:
        print("Failed to update post")

# DELETE request to remove a post
def delete_post(post_id=1):
    # Send DELETE request
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    if response.status_code == 200:
        print(f"Post {post_id} deleted successfully")
    else:
        print("Failed to delete post")

# Web scraping example using BeautifulSoup
def scrape_website():
    # URL to scrape
    url = "https://quotes.toscrape.com"
    # Send GET request
    response = requests.get(url)
    if response.status_code == 200:
        # Create BeautifulSoup object
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all quote elements
        quotes = soup.find_all('span', class_='text')
        # Print first 3 quotes
        for quote in quotes[:3]:
            print(quote.text)
    else:
        print("Failed to scrape website")

if __name__ == "__main__":
    print("Fetching posts...")
    fetch_posts()
    
    print("\nCreating new post...")
    create_post()
    
    print("\nUpdating post...")
    update_post()
    
    print("\nDeleting post...")
    delete_post()
    
    print("\nScraping quotes...")
    scrape_website()
