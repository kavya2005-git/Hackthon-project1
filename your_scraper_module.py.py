# from bs4 import BeautifulSoup as bs
# import requests
# from newspaper import Article
# import nltk
# import os
# news_text=requests.get('https://www.thehindu.com/')
# soup=bs(news_text.content,'lxml')
# sections=soup.find_all('div',class_='element')
# os.makedirs('scrape',exist_ok=True)
# with open('scrape/news.txt','w',encoding='utf-8') as f:
#     for index, section in enumerate(sections):
#         h3=section.find('h3')
#         if h3:
#             a=h3.find('a')
#             if a:
#                 if 'href'in a.attrs:
#                     url=a['href']
#                 if not url:
#                         print('section not found')
#                 else:
#                         article=Article(url)
#                         article.download()
#                         article.parse()
#                         article.nlp()
#                         f.write(f'Title:,{article.title}\n')
#                         f.write(f'Authors:,{article.authors}\n')
#                         f.write(f'published date:,{article.publish_date}\n')
#                         f.write(f'summary:,{article.summary}\n')
#                         f.write(f'\n')
# print("file saved")    

from bs4 import BeautifulSoup as bs
import requests
from newspaper import Article
import json

def scrape_news():
    # Fetch the webpage
    news_text = requests.get('https://www.thehindu.com/')
    soup = bs(news_text.content, 'lxml')

    # Find all sections with the specified class
    sections = soup.find_all('div', class_='element')

    # List to store the news articles
    news_data = []

    # Iterate through sections and process articles
    for index, section in enumerate(sections):
        h3 = section.find('h3')
        if h3:
            a = h3.find('a')
            if a and 'href' in a.attrs:
                url = a['href']
                if not url:
                    print('Section not found')
                else:
                    try:
                        article = Article(url)
                        article.download()
                        article.parse()
                        article.nlp()
                        # Append the article data to the list with an id field
                        news_data.append({
                            'article': index + 1,  # Add an id field (1-based index)
                            'Title': article.title,
                            'Authors': article.authors,
                            'Published Date': str(article.publish_date),
                            'Summary': article.summary
                        })
                    except Exception as e:
                        print(f"Error processing article at {url}: {e}")

    # Return the news data as a JSON object
    return json.dumps(news_data, indent=4)

# Call the function and print the JSON response
if __name__ == "__main__":
    news_json = scrape_news()
    print(news_json)