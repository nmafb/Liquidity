mport os 

# DROP TABLES

ads_table_drop = "DROP TABLE IF EXISTS data_ads;"
replies_table_drop = "DROP TABLE IF EXISTS data_replies;"
segments_table_drop = "DROP TABLE IF EXISTS data_segmentation;"
categories_table_drop = "DROP TABLE IF EXISTS data_categories;"


# TRUNCATE TABLES
ads_table_truncate = "TRUNCATE TABLE data_ads"
replies_table_truncate = "TRUNCATE TABLE data_replies"
segments_table_truncate = "TRUNCATE TABLE data_segmentation"
categories_table_truncate = "TRUNCATE TABLE data_categories"

# CREATE TABLES

ads_table_create = "CREATE TABLE IF NOT EXISTS data_ads ( date date NOT NULL, \
                                                     user_id INT NOT NULL , \
                                                     ad_id INT NOT NULL, \
                                                     category_id INT not null, \
                                                     params varchar);"

replies_table_create = "CREATE TABLE IF NOT EXISTS data_replies ( date date NOT NULL, \
                                                             user_id INT NOT NULL , \
                                                             ad_id INT NOT NULL, \
                                                             mails varchar NULL, \
                                                             phones varchar NULL);"

segments_table_create = "CREATE TABLE IF NOT EXISTS sdata_egments ( user_id INT NOT NULL , \
                                                        segment VARCHAR NOT NULL);"

categories_table_create = "CREATE TABLE IF NOT EXISTS cdata_ategories ( category_id INT not null,\
                                                                   category_name VARCHAR);"

# INSERT RECORDS

ads_table_insert = " INSERT INTO data_ads VALUES(%s, %s, %s, %s, %s);"

replies_table_insert = " INSERT INTO data_replies VALUES(%s, %s, %s, %s, %s);"

categories_table_insert = " INSERT INTO data_categories VALUES(%s, %s);"

segments_table_insert = " INSERT INTO data_segmentation VALUES(%s, %s);"


# FIND LIQUIDITY

user_liquidity_select = " with cte_ad_replies as (\
                            select a.user_id,\
                                    count(distinct b.ad_id) as num_ad_replied\
                            from data_ads a\
                            inner join data_replies as b\
                                on a.user_id = b.user_id\
                                    and a.ad_id = b.ad_id\
                            where b.date - a.date <= 7\
                            and (\
                                    cast(b.mails as int) >= 1\
                                    or\
                                    cast(b.phones as int) >= 1\
                            )\
                    group by a.user_id\
                ), \
                    cte_ads as (\
                select user_id,\
                            count(1) as num_ads\
                    from data_ads\
                    group by user_id\
                    )\
                select a.user_id, A.num_ads, B.num_ad_replied, round(((B.num_ad_replied * 1.0) / A.num_ads) * 100, 2) as Liquidity\
                from cte_ads as a\
                join cte_ad_replies as b\
                on A.user_id = B.user_id\
                    order by 4 desc; "

# QUERY LISTS

create_table_queries = [ads_table_create, segments_table_create, categories_table_create, replies_table_create]
drop_table_queries = [ads_table_drop, replies_table_drop, segments_table_drop, categories_table_drop]
truncate_table_queries = [ads_table_truncate, replies_table_truncate, segments_table_truncate, categories_table_truncate]