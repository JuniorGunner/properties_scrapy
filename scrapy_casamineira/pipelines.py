# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2

class ScrapyCasamineiraPipeline(object):
    def open_spider(self, spider):
        hostname = 'avaliei-dev.cftkhaxsfvvo.sa-east-1.rds.amazonaws.com' # Dev Database
        username = 'avaliei'
        password = 'AvalieiDev123'
        database = 'avaliei_dev'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        try:
            # state
            uf = item['state'].strip()
            # get state id
            query = "SELECT id FROM db_property.state WHERE uf LIKE'%{0}%'".format(uf)
            self.cur.execute(query)
            state_id = self.cur.fetchone()[0]

            # city
            city_name = item['city'].strip()
            query = "INSERT INTO db_property.city(name, state_id) VALUES ('{0}',{1}) \
                    ON CONFLICT (name) DO NOTHING".format(city_name, state_id)
            self.cur.execute(query)
            # get city id
            query = "SELECT id FROM db_property.city WHERE name LIKE '%{0}%' AND state_id={1}".format(city_name, state_id)
            self.cur.execute(query)
            city_id = self.cur.fetchone()[0]

            # type
            type_name = item['type'].strip()
            query = "INSERT INTO db_property.property_type(name) VALUES ('{0}') \
                    ON CONFLICT (name) DO NOTHING".format(type_name)
            # get type id
            query = "SELECT id FROM db_property.property_type WHERE name LIKE '%{0}%'".format(type_name)
            self.cur.execute(query)
            type_id = self.cur.fetchone()[0]

            # source
            source_name = "casamineira"
            query = "SELECT id FROM db_property.source WHERE name LIKE '%{0}%'".format(source_name)
            self.cur.execute(query)
            source_id = self.cur.fetchone()[0]

            # property
            property_webid = item['id']

            query_insert = "INSERT INTO db_property.property("
            query_values = " VALUES ("
            query_conflict = ""

            if item['id'] :
                query_insert = query_insert + "property_webid, "
                query_values = query_values + "'{0}', ".format(item['id'])
                query_conflict = " ON CONFLICT (property_webid) DO NOTHING"
            if source_id:
                query_insert = query_insert + "source_id, "
                query_values = query_values + "{0}, ".format(source_id)
            if type_id:
                query_insert = query_insert + "type_id, "
                query_values = query_values + "{0}, ".format(type_id)
            if city_id:
                query_insert = query_insert + "city_id, "
                query_values = query_values + "'{0}', ".format(city_id)
            if item['neighborhood']:
                query_insert = query_insert + "neighborhood, "
                query_values = query_values + "'{0}', ".format(item['neighborhood'])
            # if item['rua']:
            #     query_insert = query_insert + "address_str, "
            #     query_values = query_values + "'{0}', ".format(item['rua'])
            # if item['numero']:
            #     query_insert = query_insert + "address_num, "
            #     query_values = query_values + "{0}, ".format(*item['numero'])
            # if item['area_terreno']:
            #     query_insert = query_insert + "area_total, "
            #     query_values = query_values + "{0}, ".format(*item['area_terreno'])
            if item['area_usable']:
                query_insert = query_insert + "area_usable, "
                query_values = query_values + "{0}, ".format(item['area_usable'])
            if item['n_bedroom']:
                query_insert = query_insert + "n_bedroom, "
                query_values = query_values + "{0}, ".format(item['n_bedroom'])
            if item['n_bathroom']:
                query_insert = query_insert + "n_bathroom, "
                query_values = query_values + "{0}, ".format(item['n_bathroom'])
            if item['n_suite']:
                query_insert = query_insert + "n_suite, "
                query_values = query_values + "{0}, ".format(item['n_suite'])
            if item['n_parking']:
                query_insert = query_insert + "n_parking, "
                query_values = query_values + "{0}, ".format(item['n_parking'])
            if item['lat']:
                query_insert = query_insert + "latitude, "
                query_values = query_values + "{0}, ".format(item['lat'])
            if item['lon']:
                query_insert = query_insert + "longitude, "
                query_values = query_values + "{0}, ".format(item['lon'])

            query_insert = query_insert.rstrip(", ") + ")"
            query_values = query_values.rstrip(", ") + ")"

            query = query_insert + query_values + query_conflict
            self.cur.execute(query)

            query = "SELECT id FROM db_property.property WHERE property_webid='{0}'".format(property_webid)
            self.cur.execute(query)
            property_id = self.cur.fetchone()[0]

            # advertisement
            if item['price_sale']:
                price_sale = item['price_sale']
            # elif item['transacao2'] == 'SALE':
            #     price_sale = item['preco2']
            else:
                price_sale = None

            # if item['transacao1'] == 'RENTAL':
            #     price_rental = item['preco1']
            # elif item['transacao2'] == 'RENTAL':
            #     price_rental = item['preco2']
            # else:
            #     price_rental = None

            query_insert = "INSERT INTO db_property.advertisement("
            query_values = " VALUES ("
            query_conflict = " ON CONFLICT (property_id, date_creation, date_update) DO NOTHING"

            if property_id :
                query_insert = query_insert + "property_id, "
                query_values = query_values + "{0}, ".format(property_id)
            # if item['datacriacao'] :
            if True:
                query_insert = query_insert + "date_creation, "
                query_values = query_values + "NOW()::TIMESTAMP, "
            # if item['dataatualizacao'] :
            if True:
                query_insert = query_insert + "date_update, "
                query_values = query_values + "NOW()::TIMESTAMP, "
            # if price_rental :
            #     query_insert = query_insert + "price_rental, "
            #     query_values = query_values + "{0}, ".format(price_rental)
            if price_sale :
                query_insert = query_insert + "price_sale, "
                query_values = query_values + "{0}, ".format(price_sale)
            # if item['publisher_id'] :
            #     query_insert = query_insert + "user_advertisement_id, "
            #     query_values = query_values + "'{0}', ".format(item['publisher_id'])
            # if item['pictures'] :
            #     query_insert = query_insert + "pictures, "
            #     query_values = query_values + "'{0}', ".format(*item['pictures'])
            # if item['fee_condo'] :
            #     query_insert = query_insert + "fee_condo, "
            #     query_values = query_values + "{0}, ".format(item['fee_condo'])

            query_insert = query_insert.rstrip(", ") + ")"
            query_values = query_values.rstrip(", ") + ")"

            query = query_insert +  query_values + query_conflict
            # print('\n\n', query, '\n\n')
            self.cur.execute(query)

        except psycopg2.ProgrammingError as e:
            self.connection.rollback()
            print('ProgrammingError: ', e.pgerror, sep='\n')
            try:
                self.cur.close()
                self.cur = self.connection.cursor()
            except:
                self.connection.close()
                self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

            self.cur = self.connection.cursor()

        except psycopg2.InterfaceError as e:
            # self.connection.rollback()
            print('InterfaceError: ', e.pgerror, sep='\n')
            # self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
            # self.cur = self.connection.cursor()
            try:
                self.cur.close()
                self.cur = self.connection.cursor()
            except:
                self.connection.close()
                self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

            self.cur = self.connection.cursor()

        except psycopg2.IntegrityError as e:
            self.connection.rollback()
            print('IntegrityError: ', e.pgerror, sep='\n')

        except psycopg2.InternalError as e:
            self.connection.rollback()
            print('InternalError: ', e.pgerror, sep='\n')
            try:
                self.cur.close()
                self.cur = self.connection.cursor()
            except:
                self.connection.close()
                self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

            self.cur = self.connection.cursor()

        else:
            self.connection.commit()
            return item
