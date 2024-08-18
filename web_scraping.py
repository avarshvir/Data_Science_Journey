mport pandas as pd
import requests
from bs4 import BeautifulSoup

# Make HTTP Request to the URL
URL = "https://www.scaler.com/topics/data-structures/"
page = requests.get(URL)

# Extract HTML content of the URL
soup = BeautifulSoup(page.content, "html.parser")

# In the next step, you need to find the required data by the id in the HTML code. # As you can see in the below diagram, our required data is encompassed in id = # __next
results = soup.find(id="__next")

# As you can see in the above diagram, each module is part of a class and in the next step, we need to scrape the content of this class

module_details = results.find_all("div", class_="hub-content-list_module_box__mJbDp")
scraped_data = []

# Similarly, we need to find HTML tags for each content we want to parse and store. For our use case, the next loop will parse the module title, number, and chapter details.

# Scraping module information - title and module number
for the module in module_details:
    module_title = module.find("h2", class_="hub-content-list_module__title__yWq1o p-l-xs no-mgn-b")
    module_number = module.find("span", class_="hub-content-list_module__order__teUvv p-l-xs")

    # Scraping chapter details
    chapters_details = module.find_all("div", class_="row space-between module-list_chapter_box__gyTaS")
    module_data = [module_title.text, module_number.text]

    # Iterating through each chapter and parse title, minutes to complete, and URL
    for chapter in chapters_details:
        chapter_name = chapter.find("div", class_="row flex-ac module-list_no_hover_effect__v9df5")
        chapter_minutes = chapter.find("div", class_="module-list_chapter__info__Vtrxq")
        chapter_url = chapter.find("div", class_="row cursor").find("a", href=True)['href']
        chapter_data = [chapter_name.text, chapter_minutes.text, "https://www.scalar.com" + chapter_url]
        scraped_data.append(module_data + chapter_data)

# Let's store this data now in a data frame and save it as a CSV file

col_names = ["Module Title", "Module Number", "Chapter Title", "Chapter Minutes to Read", "Chapter URL"]
df = pd.DataFrame(scraped_data, columns=col_names)
df.to_csv("Your Local Path")
df.head()
