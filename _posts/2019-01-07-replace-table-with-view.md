---
title: "Replace a Table With View"
date: 2019-01-07T10:51:38-05:00
tags:
  - sql
  - mysql
  - database
---

This weekend while on dev support, an issue came to our attention that
customers were still able to see `soft deleted` data in some parts of the app.
Instead of going through all the code and updating each query to return only
existing data though, I went directly to the source and replaced the table with
a view.

#### Pros/Cons:

Pros:
 - Easily revertible change.
 - Apply once, fixes all current queries.
 - Views can still have INSERT, UPDATE, and DELETE statements run against them.
 - Good practice from a database design standpoint.

Cons:
 - Someone has to have access to the prod db to do it.
 - Can confuse other developers who are not familiar with views.
 - Depend on the indexes of the table below. You can not put an index on a view.

#### This is how I did it:

1) Rename the table.

``` SQL
RENAME TABLE chapters TO chapters_all;
```

2) Create a simple view that filters out deleted data.

```SQL
CREATE VIEW `chapters` AS
    SELECT
        `chapters_all`.`id` AS `id`,
        `chapters_all`.`school` AS `school`,
        `chapters_all`.`removed` AS `removed`,
        etc...
    FROM
        `chapters_all`
    WHERE
        (`chapters_all`.`removed` = 0)
```

Hope this helps!