---
title: "Useful SQL Queries - PostgreSQL Dialect"
date: 2019-03-13T13:08:51-04:00
last_modified_at: 2019-03-13T13:08:51-04:00
tags:
  - sql
  - postgres
---

Below is a recording of the commands I utilize to help me understand and navigate unknown databases designs.


## Connect to Postgres server via pgcli(python)

```
>>> pgcli -h host -U username -d database
```

## View databases on server

```
# \l
```

## View information about a specific table

```
# DESCRIBE tablename;
```

Or 

```
 # \d tablename
```

## Constrains

This is nice if you want to see `on_delete` and `on_update` cascade settings between tables.

```
# SELECT * FROM information_schema.REFERENTIAL_CONSTRAINTS;
```

## Print the amount of time it takes to execute queries

```
# \timing
```

## Want to see more than a blank cell for null values? Set a default.

```
# \pset null [NULL]
```

## Watch like `watch` on linux...(rerun a query)

```
# SELECT count(*) from accounts;
# \watch
```

## Recall old queries

```
CTRL + r
```

## Look for unused indexes

```
SELECT *
    FROM pg_stat_user_tables
    WHERE schemaname='public'
    ORDER BY seq_scan DESC;
```

## Get execution plan of query

```
EXPLAIN ANALYZE SELECT * FROM accounts;
```

Look for seq scans. Try to reduce these. Use indexes as much as possible. Careful though, the more indexes the slower the writes.

## Avoid COUNT(*) and prefer COUNT(1)

```
SELECT COUNT(1) FROM accounts;
```

As `count(*)` tells the db server to get all the columns before counting the results. This is a waste of CPU cycles. Instead we are telling the server to only grab the first column via `count(1)`.

## Do not use `LEFT JOIN ON null id`

Found this tidbit when I saw a left join in a query and was like WTF?

Instead of using 

```
LEFT JOIN ON null id
```

Use

```
NOT EXISTS
```

As it is optimized for performance for finding things that don't exist. 

[Source](https://marmelab.com/blog/2019/02/13/how-to-improve-postgres-performances.html) 

## Slow queries and nothing identified with an explain?

Look at the health of the table.

```
SELECT n_live_tup, n_dead_tup from pg_stat_user_tables where relname = ‘tablename’;
```

If there are significantly more dead rows than live rows then data is going unused and is probably in the way of your lookups. Solution? Perform a vacuum on the table in question.

```
VACUUM tablename;
```

