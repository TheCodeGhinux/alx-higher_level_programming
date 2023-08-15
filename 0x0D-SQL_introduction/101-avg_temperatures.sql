-- displays the average temperature (Fahrenheit) by
-- city ordered by temperature (descending).
ELECT city, avg(value) AS avg_temp
FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
