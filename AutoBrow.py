import time
import matplotlib.pyplot as plt
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Automatically start Chrome and navigate to the webpage
driver = webdriver.Chrome()
driver.get("https://www.ctvnews.ca/")

# Wait for the page to load (you can adjust the sleep time)
time.sleep(6)

# Create a list of XPaths for the elements you want to analyze
xpaths = [
    "/html/body/div[2]/div/div[6]/div/div[4]/div/div[1]/div/section/div/div[1]/article/div/div[2]/h3/a",
    "/html/body/div[2]/div/div[6]/div/div[4]/div/div[1]/div/section/div/div[2]/article[1]/div/div[2]/h3/a"
]

# Initialize empty lists to store sentiment scores and news text
sentiments = []
news_texts = []

# Loop through the XPaths to analyze each element
for i, xpath in enumerate(xpaths):
    # Get the text using the specified XPath
    text_element = driver.find_element(By.XPATH, xpath)
    news_text = text_element.text

    # Determine the sentiment of the text
    sentiment_scores = analyzer.polarity_scores(news_text)

    # Get the sentiment score
    compound_score = sentiment_scores['compound']

    # Store the sentiment score in the list
    sentiments.append(compound_score)

    # Store the news text in the list
    news_texts.append(news_text)

    # Print the result in the console
    print(f"Element {i+1} - Sentiment Score: {compound_score:.2f} - Text: {news_text}")

# Close the web browser
driver.quit()

# Create a bar graph to visualize sentiments
labels = ['Element 1', 'Element 2']
width = 0.4
fig, ax = plt.subplots(figsize=(8, 6))

# Create bars for each sentiment score
bars = ax.bar(labels, sentiments, width, color=['red', 'blue'])

for bar, score in zip(bars, sentiments):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02, f"{score:.2f}", ha='center')

plt.title('Sentiment Analysis of News Text')
plt.ylabel('Sentiment Score')

# Show the graph
plt.show()
