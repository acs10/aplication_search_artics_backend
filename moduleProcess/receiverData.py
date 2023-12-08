import requests
from bs4 import BeautifulSoup

class GoogleScholarScraper:
    def __init__(self, query):
        self.query = query
        self.interest = ""
        self.language = "lang_pt" # Idioma da pesquisa: lang_pt = português, lang_es = espanhol, lang_en = inglês
        self.sort_by_date = "0" # Ordenar por data: 0 ou 1
        self.period_start = "" # Ano inicial
        self.period_end = "" # Ano final
        self.start_position = 0
        self.num_per_page = 10
        self.page_number = 1

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/94.0.4606.81"
        }

    def scrape_google_scholar(self):
        while True:
            print(f"--- Page {self.page_number} ---")
            print(f"Showing results {self.start_position + 1} - {self.start_position + self.num_per_page}")
            url = f"https://scholar.google.com/scholar?start={self.start_position}&q={self.query}+{self.interest}&hl=pt-BR&lr={self.language}&scisbd={self.sort_by_date}&as_ylo={self.period_start}&as_yhi={self.period_end}&as_sdt=0,5"

            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.text, "html.parser")

            articles = soup.find_all("div", {"class": "gs_r"})

            if not articles:
                print("No more results")
                break

            articles_list = []

            for article in articles:
                title_tag = article.find("h3", {"class": "gs_rt"})
                title = title_tag.text if title_tag else "No title available"

                authors_tag = article.find("div", {"class": "gs_a"})
                authors = authors_tag.text if authors_tag else "No authors available"

                link_tag = title_tag.find("a") if title_tag else None
                link = link_tag.get("href") if link_tag else "No link available"

                description_tag = article.find("div", {"class": "gs_rs"})
                description = description_tag.text.strip() if description_tag else "No description available"

                articles_list.append({
                    "title": title,
                    "authors": authors,
                    "link": link,
                    "description": description
                })

            articles_list.sort(key=lambda article: article["title"])

            for article in articles_list:
                print(f"Title: {article['title']}\nAuthors: {article['authors']}\nLink: {article['link']}\nDescription: {article['description']}\n")

            self.page_number += 1
            self.start_position += self.num_per_page

            option = input("Do you want to continue? (y/n): ")
            if option.lower() != "y":
                break
        return articles_list

# scraper = GoogleScholarScraper("machine learning")
# scraper.scrape_google_scholar()
