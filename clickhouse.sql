причины медленности запроса:
1) не использовано предварительно where для каждой таблицы
2) использовано join. IN может выполнять поиск по индексу более эффективно, чем JOIN
3 ) использование final. clickhouse final получет последнюю версию для всех записей, даже нам не нужных.

WITH
    today_date AS today(),
    yesterday_date AS today() - 1

SELECT DISTINCT product_id
FROM products
WHERE updated = today_date
AND product_id IN (
    SELECT product_id
    FROM remainders
    FINAL
    WHERE date = yesterday_date
);


****
select product_id
from products
final join remainders
final using(product_id)
where updated=today() and date=today()-1