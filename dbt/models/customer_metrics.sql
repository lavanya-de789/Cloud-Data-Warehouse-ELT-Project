select

city,

avg(spend) avg_spend,

count(*) total_customers

from {{ref('staging')}}

group by city
