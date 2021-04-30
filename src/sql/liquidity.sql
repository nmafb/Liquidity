with cte_ad_replies as (
	select 
			a.user_id, 
			count(distinct b.ad_id) as num_ad_replied
		from data_ads a
		inner join data_replies b on a.user_id = b.user_id and a.ad_id = b.ad_id
		where b.date - a.date <= 7 and (mails >= 1 or phones >= 1)
		group by a.user_id
), cte_ads as (
	select user_id, count(1) as num_ads from data_ads group by user_id
)
select a.user_id, A.num_ads, B.num_ad_replied, round(((B.num_ad_replied * 1.0) / A.num_ads) * 100, 2) as Liquidity
from cte_ads a
	inner join cte_ad_replies b on a.user_id = b.user_id