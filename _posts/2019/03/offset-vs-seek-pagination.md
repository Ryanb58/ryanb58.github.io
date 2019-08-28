---
title: "Offset vs Seek/Keyset Pagination"
date: 2019-03-13T13:08:51-04:00
draft: false
toc: false
images:
tags:
  - sql
  - pagination
---

Today I was focused on defining the standards for pagination on a new product and decided to dialog with a coworker. Below is the idea I threw out:

> Any list of items I return from the API will be in this format:
```Javascript
{
  results: [],
  next: null,
}
```
>
> The only thing that would identify the result as a part of pagination.. would be the value of the “next” key. If it is `null` then there would be NO more items beyond the ones I have already returned. IFF there are more items.. I would return something like.. next: 2 Thus identifying that there is a page=2 of items more for the client. And depending on page=2's results… it’s next field would identify if there is a page=3 more of results.. etc..
>
> What do you think? I feel like I am at a point that making these pagination standards will be critical for the future of other api endpoints..

This sparked my coworker to respond:

> I really like the standard of using `total`, `limit`, and `skip`.
> With only using `next` you don’t know how many items or pages there are.
> Using total, limit, and skip really lends itself to handling pagination on the client — where the user can pick how many results to display per page.

Talk about good points. However, their exists similarities between our designs.
If I was to go implement either of these, they would both end up being an implementation of the offset method. Whether the offsets where to be statically stored on the server or defined by the frontend was the only difference.
Therefore, both of these ideas are implementation preferences defining how the offsets should be handled and NOT differences in the underlying concept of how we would load the data.

This flipped a switch in my brain that reminded me of an issue I faced at an previous job. One day we had customers start to call-in and complain about the time it took to load files(listings) beyond the 10th page. The offset method was used to display the metadata to the user and this ended up being a side effect.

Taking all this into account I thought there had to be a better way.

## What is Offset Pagination?

Perhaps you have seen SQL Query similar to this before:

```SQL
SELECT id, firstname, lastname, created, updated
FROM contacts
ORDER BY id
LIMIT 0, 10
```

The query above grabs the first 10 records. Similarly, to get the 10 records on page 4 we would execute the following:

```SQL
SELECT id, firstname, lastname, created, updated
FROM contacts
ORDER BY id
LIMIT 30, 10
```

## Problems with Offset Pagination:

 - The higher the offset the [slower the query](https://stackoverflow.com/a/4502426). [Source 2](https://explainextended.com/2009/10/23/mysql-order-by-limit-performance-late-row-lookups/)

 - One must calculate the amount of pages based off the total amount of records.

 - Must scan an index to count the number of rows.

 - [Complicated solutions to speed up results on pages farther back.](http://www.4guysfromrolla.com/webtech/042606-1.shtml)

 - Even with an index, we scan the index, to a sort on the data, then select the items we want to return. The first two steps are obviously a waste as we will be manipulating data that is not relevant to the results we want to return.

 There MUST be a better way! And there is. Introducing seek pagination.

## Seek/Keyset Pagination

The seek method is based on filtering out the data from the previous pages. We do this by having the client send the ID of the last record listed. We take that ID and place it in the WHERE clause providing us with only relevant data. Obviously this implementation requires your data to be [deterministically sortable](http://www.unicode.org/notes/tn9/tn9-1.html).

  "Don't touch what you don't need" - [Youtube](https://youtu.be/GzMaN-IX7wQ?t=655)

An example SQL statement follows:

```SQL
SELECT id, firstname, lastname
FROM contacts
WHERE id < 10
ORDER BY id DESC
LIMIT 10;
```

Therefore from a REST perspective the results would appear as so:

```Javascript
{
  "results": [
    {id: 1, ... },
    {id: 2, ... }
    {id: 3, ... }
    ...
    {id: 10, ... }
  ]
}
```

And when the user wanted to get the next page of items, they simply tack on the `last_id` from the previous pagination result.

```
GET /api/contacts?last_id=10
```

Resulting:

```Javascript
{
  "results": [
    {id: 11, ... },
    {id: 12, ... }
    {id: 13, ... }
    ...
    {id: 20, ... }
  ]
}
```

For more information about seek/keyset please visit the following sources.

Sources:

https://blog.jooq.org/2013/10/26/faster-sql-paging-with-jooq-using-the-seek-method/

https://use-the-index-luke.com/sql/partial-results/fetch-next-page

https://stackoverflow.com/a/3215973

https://stackoverflow.com/a/4502426

https://www.citusdata.com/blog/2016/03/30/five-ways-to-paginate/

https://blog.jooq.org/2016/08/10/why-most-programmers-get-pagination-wrong/

https://www.youtube.com/watch?v=GzMaN-IX7wQ

http://www.unicode.org/notes/tn9/tn9-1.html