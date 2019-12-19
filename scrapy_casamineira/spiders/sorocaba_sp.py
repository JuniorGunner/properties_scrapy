import scrapy
from scrapy import Request
import bs4
from bs4 import BeautifulSoup as bs

class SorocabaSpider(scrapy.Spider):
    name = 'sorocaba_sp'

    start_urls = [
        'https://www.casamineira.com.br/venda/apartamento/sorocaba_sp' # ?pagina=1
    ]

    def parse(self, response):
        # Lê html
        html = response.body
        soup = bs(html, 'html.parser')

        # Anúncios
        anuncios = soup.find('div', {'class': 'property-listing'}).findAll('div', class_ = 'property-item')

        for item in anuncios:
            end = item.find('a', {'class': 'property-location'}).getText().strip().split(',')
            bairro = end[0]
            cidade, uf = end[1].split('-')
            cidade, uf = cidade.strip(), uf.strip()

            # Informações: área, quartos, banheiros, suítes, vagas, preço
            area, quartos, banheiros, suites, vagas = 0, 0, 0, 0, 0
            info = item.find('ul').getText().split()

            #Área
            if('m²' in info):
                area = int(info[info.index('m²')-1])

            # Quarto
            if('quarto' in info):
                quartos = int(info[info.index('quarto')-1])
            elif('quartos' in info):
                quartos = int(info[info.index('quartos')-1])

            # Banheiro
            if('banheiro' in info):
                banheiros = int(info[info.index('banheiro')-1])
            elif('banheiros' in info):
                banheiros = int(info[info.index('banheiros')-1])

            # Suítes
            if('suíte' in info):
                suites = int(info[info.index('suíte')-1])
            elif('suítes' in info):
                suites = int(info[info.index('suítes')-1])

            # Vagas
            if('vaga' in info):
                vagas = int(info[info.index('vaga')-1])
            elif('vagas' in info):
                vagas = int(info[info.index('vagas')-1])

            # Preço
            preco = int(item.find('span', {'class': 'preco'}).getText().split()[1].replace('.', ''))

            yield {
                'neighborhood': bairro,
                'city': cidade,
                'state': uf,
                'area_usable': area,
                'n_bedrooom': quartos,
                'n_bathroom': banheiros,
                'n_suite': suites,
                'n_parking': vagas,
                # 'lat': item.xpath("").extract_first(),
                # 'lon': item.xpath("").extract_first(),
                'price_sale': preco,
                # 'fee_condo': item.xpath("").extract_first()
            }

        next_urls = response.xpath("//ul[@class='pagination']/li/a/@href").extract()
        for url in next_urls:
            yield Request(response.urljoin(url), callback = self.parse)

        # if(next_page is not None):
        #     next_page_link = response.urljoin(next_page)
        #     yield scrapy.Request(url = next_page_link, callback = self.parse)
