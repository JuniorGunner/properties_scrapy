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
  $ pip install requirements.txt
  ```

3. Run spider:
  ```
  scrapy crawl myspider
  ```

#### License
[MIT](https://choosealicense.com/licenses/mit/)
