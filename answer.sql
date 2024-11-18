-- TYPE YOUR SQL QUERY BELOW

-- PART 1: Create a SQL query that maps out the daily average users before and after the feature change

SELECT 
    DATE(login_timestamp, 'unixepoch') AS date,
    COUNT(DISTINCT user_id) AS daily_active_users,
    IIF(DATE(login_timestamp, 'unixepoch') < '2018-06-02', 'Before', 'After') AS period
FROM login_history
WHERE date BETWEEN '2018-02-03' AND '2019-02-01'
GROUP BY date
ORDER BY date;


-- PART 2: Create a SQL query that indicates the number of status changes by card

SELECT cardID, COUNT(*) as card_changes FROM card_change_history
WHERE DATE(timestamp, 'unixepoch') >= '2018-06-02'
GROUP BY cardID
ORDER BY card_changes DESC;




