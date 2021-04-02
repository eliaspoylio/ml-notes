##

SELECT DISTINCT

## Group By, Having & Count

# Query to select prolific commenters and post counts
 Write a query that returns all authors with more than 10,000 posts as well as their post counts. Call the column with post counts NumPosts.
```sql
SELECT author, COUNT(1) AS NumPosts
FROM `bigquery-public-data.hacker_news.comments`
GROUP BY author
HAVING COUNT(1) > 10000
```

```sql
SELECT COUNT(id)
FROM `bigquery-public-data.hacker_news.comments`
WHERE deleted = True
```

```python
# Write your query here and figure out the answer
# Query to determine how many posts were deleted
deleted_posts_query = """
                      SELECT COUNT(1) AS num_deleted_posts
                      FROM `bigquery-public-data.hacker_news.comments`
                      WHERE deleted = True
                      """

# Set up the query
query_job = client.query(deleted_posts_query)

# API request - run the query, and return a pandas DataFrame
deleted_posts = query_job.to_dataframe()

# View results
print(deleted_posts)
```

## Order By

- aggregate

Which countries spend the largest fraction of GDP on education?

To answer this question, consider only the rows in the dataset corresponding to indicator code SE.XPD.TOTL.GD.ZS, and write a query that returns the average value in the value column for each country in the dataset between the years 2010-2017 (including 2010 and 2017 in the average).

Requirements:

    Your results should have the country name rather than the country code. You will have one row for each country.
    The aggregate function for average is AVG(). Use the name avg_ed_spending_pct for the column created by this aggregation.
    Order the results so the countries that spend the largest fraction of GDP on education show up first.

```sql
SELECT country_name, AVG(value) AS avg_ed_spending_pct
FROM `bigquery-public-data.world_bank_intl_education.international_education`
WHERE indicator_code = 'SE.XPD.TOTL.GD.ZS' AND year <= 2017 AND year >= 2010
GROUP BY country_name
ORDER BY avg_ed_spending_pct DESC
```


The last question started by telling you to focus on rows with the code SE.XPD.TOTL.GD.ZS. But how would you find more interesting indicator codes to explore?

There are 1000s of codes in the dataset, so it would be time consuming to review them all. But many codes are available for only a few countries. When browsing the options for different codes, you might restrict yourself to codes that are reported by many countries.

Write a query below that selects the indicator code and indicator name for all codes with at least 175 rows in the year 2016.

Requirements:
- You should have one row for each indicator code.
- The columns in your results should be called `indicator_code`, `indicator_name`, and `num_rows`.
- Only select codes with 175 or more rows in the raw database (exactly 175 rows would be included).
- To get both the `indicator_code` and `indicator_name` in your resulting DataFrame, you need to include both in your **SELECT** statement (in addition to a **COUNT()** aggregation). This requires you to include both in your **GROUP BY** clause.
- Order from results most frequent to least frequent.


```sql
SELECT indicator_code, indicator_name, COUNT(1) AS num_rows
FROM `bigquery-public-data.world_bank_intl_education.international_education`
WHERE year = 2016
GROUP BY indicator_code, indicator_name HAVING COUNT(1) >= 175
ORDER BY num_rows DESC
```

## As With

- common table expression

```python
print([x.table_id for x in client.list_tables(dataset_ref)])
```
```
['taxi_trips']
```

```python
# Construct a reference to the "taxi_trips" table
table_ref = dataset_ref.table("taxi_trips")

# API request - fetch the table
table = client.get_table(table_ref)

# Preview the first five lines of the "taxi_trips" table
client.list_rows(table, max_results=5).to_dataframe()
```

### 3)
```python
# Your code goes here
rides_per_year_query = """
                       SELECT EXTRACT(YEAR FROM trip_start_timestamp) AS year, COUNT(1) AS num_trips
                       FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
                       GROUP BY year
                       ORDER BY year
                       """

# Set up the query (cancel the query if it would use too much of 
# your quota)
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
rides_per_year_query_job = client.query(rides_per_year_query, job_config=safe_config) # Your code goes here

# API request - run the query, and return a pandas DataFrame
rides_per_year_result = rides_per_year_query_job.to_dataframe() # Your code goes here

# View results
print(rides_per_year_result)

# Check your answer
q_3.check()
```

```
   year  num_trips
0  2013   27217716
1  2014   37395436
2  2015   32385875
3  2016   31759339
4  2017   24988003
5  2018   20732088
6  2019   16477365
7  2020    3889032
8  2021     302466
```

### 4)

```python
# Your code goes here
rides_per_month_query = """
                       SELECT EXTRACT(MONTH FROM trip_start_timestamp) AS month, COUNT(1) AS num_trips
                       FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
                       WHERE EXTRACT(YEAR FROM trip_start_timestamp) = 2017
                       GROUP BY month
                       ORDER BY month
                       """

# Set up the query
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
rides_per_month_query_job = client.query(rides_per_month_query, job_config=safe_config) # Your code goes here

# API request - run the query, and return a pandas DataFrame
rides_per_month_result = rides_per_month_query_job.to_dataframe() # Your code goes here

# View results
print(rides_per_month_result)

# Check your answer
q_4.check()
```
```
    month  num_trips
0       1    1972071
1       2    1909802
2       3    2362105
3       4    2194702
4       5    2323386
5       6    2324472
6       7    2054299
7       8    2079861
8       9    1950631
9      10    2141197
10     11    1907997
11     12    1767480
```

```python
# Your code goes here
speeds_query = """
               WITH RelevantRides AS
               (
                   SELECT trip_start_timestamp, trip_miles, trip_seconds
                   FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
                   WHERE trip_start_timestamp BETWEEN '2017-01-01' AND '2017-07-01' AND trip_seconds > 0 AND trip_miles > 0
               )
               SELECT EXTRACT(HOUR FROM trip_start_timestamp) AS hour_of_day, COUNT(1) as num_trips, 3600 * SUM(trip_miles) / SUM(trip_seconds) AS avg_mph
               FROM RelevantRides
               GROUP BY hour_of_day
               ORDER BY hour_of_day ASC
               """

# Set up the query
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
speeds_query_job = client.query(speeds_query, job_config=safe_config) # Your code here

# API request - run the query, and return a pandas DataFrame
speeds_result = speeds_query_job.to_dataframe()  # Your code here

# View results
print(speeds_result)

# Check your answer
q_5.check()
```

```
    hour_of_day  num_trips    avg_mph
0             0     320766  20.207924
1             1     266529  18.937621
2             2     210147  18.777070
3             3     159668  20.158048
4             4     122183  26.736014
5             5     119312  30.769172
6             6     182738  24.588313
7             7     358406  17.735967
8             8     541775  15.079892
9             9     565548  16.543882
10           10     525120  18.539614
11           11     594603  18.928379
12           12     622324  17.838745
13           13     630181  17.671089
14           14     622465  16.974239
15           15     640430  15.688418
16           16     701435  14.283888
17           17     756627  12.462955
18           18     768251  13.646810
19           19     701064  16.642882
20           20     598614  19.536777
21           21     552726  20.433874
22           22     501095  19.531374
23           23     399587  19.877046
```

That wasn't correct. Timestamp should have been like below:

```python
speeds_query = """
               WITH RelevantRides AS
               (
                   SELECT EXTRACT(HOUR FROM trip_start_timestamp) AS hour_of_day, 
                          trip_miles, 
                          trip_seconds
                   FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
                   WHERE trip_start_timestamp > '2017-01-01' AND 
                         trip_start_timestamp < '2017-07-01' AND 
                         trip_seconds > 0 AND 
                         trip_miles > 0
               )
               SELECT hour_of_day, 
                      COUNT(1) AS num_trips, 
                      3600 * SUM(trip_miles) / SUM(trip_seconds) AS avg_mph
               FROM RelevantRides
               GROUP BY hour_of_day
               ORDER BY hour_of_day
               """
```