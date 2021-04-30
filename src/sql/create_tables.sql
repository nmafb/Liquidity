CREATE TABLE data_ads
(
    date date,    
    user_id integer,
    ad_id integer,
    category_id integer,
    params character varying 
)  ;



CREATE TABLE data_categories
(
    category_id integer,
    category_name character varying 
) ;


CREATE TABLE data_replies
(
    date date,
    user_id integer,
    ad_id integer,
    mails integer,
    phones integer
) ;


CREATE TABLE data_segmentation
(
    user_id integer,
    segment integer
) ;








