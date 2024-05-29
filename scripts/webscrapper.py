
import os
import requests
from bs4 import BeautifulSoup
import re

base_url = 'https://www.royalenfield.com'  # Replace with the website URL you want to scrape
output_dir = 'scraped_data'  # Directory to store the scraped data
os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist
urls = ['/in/en/forms/book-a-test-ride/', '/in/en/locate-us/dealers/', '/in/en/motorcycles/shotgun-650/', '/in/en/motorcycles/new-himalayan/', '/in/en/motorcycles/bullet-350/', '/in/en/motorcycles/super-meteor-650/', '/in/en/motorcycles/hunter-350/', '/in/en/motorcycles/scram411/', '/in/en/motorcycles/classic-350/', '/in/en/motorcycles/meteor/', '/in/en/motorcycles/interceptor/', '/in/en/motorcycles/continental-gt/', '/in/en/locate-us/dealers/', '/in/en/locate-us/service-centres/', '/in/en/gma/', '/in/en/locate-us/garagecafe/', '/in/en/locate-us/pre-owned/', '/in/en/support/genuine-part-distributor/', '/in/en/rides-calendar/', '/in/en/gma/shotgun-650/', '/in/en/gma/all-new-himalayan/', '/in/en/gma/all-new-bullet-350/', '/in/en/gma/super-meteor-650/', '/in/en/gma/hunter-350/', '/in/en/gma/scram411/', '/in/en/gma/classic-350/', '/in/en/gma/meteor/', '/in/en/gma/bullet/', '/in/en/gma/himalayan/', '/in/en/gma/interceptor/', '/in/en/gma/continental-gt/', '/in/en/gma/classic-uce/', '/in/en/gma/protection/', '/in/en/gma/seats/', '/in/en/gma/bodywork/', '/in/en/gma/luggage/', '/in/en/gma/engine/', '/in/en/gma/security-and-maintenance/', '/in/en/gma/controls/', '/in/en/gma/wheels/', '/in/en/gma/electrical/', 'https://www.royalenfield.com/flipbook/', 'https://store.royalenfield.com/riding-gear/gloves', 'https://store.royalenfield.com/riding-gear/helmet', 'https://store.royalenfield.com/lifestyle-apparel/shoes', 'https://store.royalenfield.com/riding-gear/riding-jackets', 'https://store.royalenfield.com/catalogsearch/result/?q=mlg', 'https://store.royalenfield.com/lifestyle-apparel/t-shirt', 'https://store.royalenfield.com/lifestyle-apparel/shirt', 'https://store.royalenfield.com/lifestyle-accessories/face-mask', 'https://store.royalenfield.com/lifestyle-accessories/bags', 'https://store.royalenfield.com/lifestyle-accessories/belts', 'https://store.royalenfield.com/lifestyle-accessories/headgear', 'https://store.royalenfield.com/lifestyle-accessories/wallets', '/in/en/our-world/forum/', '/in/en/our-world/trip-stories/', '/in/en/our-world/since-1901/', '/in/en/our-world/media/', 'https://careers.royalenfield.com/us/en/home', '/in/en/our-world/wallpaper/', '/in/en/customworld/', '/in/en/our-world/campaigns/', '/in/en/our-world/gallery/photos/', '/in/en/our-world/gallery/videos/', '/in/en/support/contact-us/', '/in/en/support/', '/in/en/support/road-side-assistance/', '/in/en/support/owners-manual/', '/in/en/support/digital-quickstart/', '/in/en/legal/private-import-policy/', '/in/en/legal/privacy-policy/', '/in/en/legal/terms-and-conditions/', '/in/en/legal/cookie-policy/', '/in/en/finance/', '/in/hi/finance/']

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    print(f'Failed to fetch {url}')
    return None

def extract_image_urls(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img', src=True)
    img_urls = [img['src'] if img['src'].startswith('http') else base_url + img['src'] for img in img_tags]
    return img_urls

def save_to_md(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def scrape_page(url):
    html_content = fetch_html(url)
    if html_content:
        img_urls = extract_image_urls(html_content, base_url)
        soup = BeautifulSoup(html_content, 'html.parser')
        # Extract data from the page
        text_content = soup.find('body').get_text(separator='\n')  # Get all text from the body of the page
        # Save data to .md file
        page_name = os.path.basename(url)
        filename = os.path.join(output_dir, f'{page_name}.md')
        content_with_imgs = f'# Website Scraped from {base_url}\n\n## Text Content\n\n{text_content}\n\n## Image URLs\n\n'
        for i, img_url in enumerate(img_urls, 1):
            content_with_imgs += f'{i}. image_url: {img_url}\n'
        save_to_md(content_with_imgs, filename)
        print(f'Data saved to {filename}')
def scrape_sitemap(base_url):
    for url in urls:
        if url[0] == '/':
            url = base_url + url
        scrape_page(url)

scrape_sitemap(base_url)
