# 🏡 Scrapy + BeautifulSoup Real Estate Scraper 

This project is a robust web scraper designed to collect and store property sales values and other pertinent details about properties. 

🕸️ Data is scraped from [Casamineira](https://www.casamineira.com.br/), a leading real estate website.

Developed with Python 3.x, this project makes use of powerful libraries and tools, including:
- Scrapy 🕷️
- BeautifulSoup 🍲

## 🛠️ Getting Started 

These instructions will get you a copy of the project up and running on your local machine.

### 🔧 Prerequisites

Ensure you have Python 3.x installed on your system. You can download it [here](https://www.python.org/downloads/).

### 💻 Installation and Setup

1. **Create a Virtual Environment** 

   Start by creating a new virtual environment to isolate the dependencies for this project.

   ```
    $ python -m venv env
    $ source env/bin/activate
   ```
2. Install dependencies:
  ```
    $ pip install -r requirements.txt
  ```

3. 🚀 Running the Scraper:
  ```
    $ scrapy crawl myspider
  ```
This will initiate the scraper, and data will begin being collected from Casamineira!

Happy data hunting! 📊

+++
# Scrapy + BeautifulSoup Project

Scrapy project develop to collect and store property sales value and other relevant informations about the property itself.

Information scraped from [Casamineira](https://www.casamineira.com.br/).

This project was developed in [Python 3.x](https://www.python.org/) with:

* [Scrapy](https://scrapy.org/);
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/);

### Instructions

1. Create and activate virtual enviroment:
  ```
  $ python -m venv env
  $ source env/bin/activate
  ```

2. Install dependencies:
  ```
  $ pip install -r requirements.txt
  ```

3. Run spider:
  ```
  $ scrapy crawl myspider
  ```

#### License
[MIT](https://choosealicense.com/licenses/mit/)
