title = "Quick Postgres Database Backup"
date = 2022-01-06T17:47:00+02:00
tags = [
    "aws",
    "postgres",
    "sql",
    "database",
    "clone",
    "backup"
]
published = true
+++++

Sometimes when working with databases you need a backup. One you can switch to quickly in case things go wrong. I find this particularly helpful when testing out data migrations.

Here are a few SQL commands I use to accomplish this.

## Look at Database Size

```
SELECT pg_size_pretty(pg_database_size('sitepixel'));
```

## Copy A Database

```
CREATE DATABASE sitepixel_backup1
WITH TEMPLATE sitepixel;
```

## View Active Connections

```
SELECT pid, usename, client_addr
FROM pg_stat_activity
WHERE datname ='sitepixel';
```

## Terminate Active Connections

```
SELECT
   pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE
   pg_stat_activity.datname = 'sitepixel'
AND pid <> pg_backend_pid()
```
