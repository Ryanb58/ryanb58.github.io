title = "Minimum Requirements for a SAAS Platform"
date = 2020-07-21T17:47:00+02:00
tags = [
    "requirements",
    "saas",
    "minimum",
    "checklist"
]
published = true
+++++

Below is a list of minimum requirements I believe are vital to the success of a SAAS platform(Note that this isn't the word product)

- Authentication Strategy(Email, Username, Social, etc..)
- Multi-Tenant Setup
- Database Migrations
- Queuing Mechanism(RabbitMQ, Redis, etc..)
- Caching(Redis, Memcache, etc..)
- Configuration Management
- Search Tools(Elasticsearch, Algolia)
- Unit Tests
- Integration Tests
- Deployment Strategy
- Dockerfied Development
- Dashboard for Statistics(Grafana, Redash, etc..)
- Hosting Provider

Always try to think through these items before digging into the code. I have found that by doing so you significantly reduce the problems you will run into when trying to scale your product and team.

Originally Posted on [dev.to](https://dev.to/mrbrazel/minimum-requirements-for-a-saas-platform-102d)