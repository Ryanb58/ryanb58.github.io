title = "Alembic Load Config From Env Vars"
date = 2019-02-25T17:47:00+02:00
tags = [
    "alembic",
    "variables",
    "environment"
]
published = true
+++++

Today, while trying to integrate the python library [Alembic](https://pypi.org/project/alembic/) into a micro-service, I ran into the issue of needing to load the database connection string from a few environmental variables. Needless to say I went ahead and did some googling and compiled this solution:

```python
def get_url():
    """Custom method to get config from the environmental variables.

    Based on: http://allan-simon.github.io/blog/posts/python-alembic-with-environment-variables/
    """
    return "postgres://{}:{}@{}/{}".format(
        os.getenv("DB_USER", "username"),
        os.getenv("DB_PASSWORD", "password"),
        os.getenv("DB_HOST", "database_host"),
        os.getenv("DB_NAME", "database_name"),
    )
```

Then inside the `run_migrations_offline` method I swapped out:
```python
url = config.get_main_option("sqlalchemy.url")
```

for

```python
url = get_url()
```

and

```python
connectable = engine_from_config(
    config.get_section(config.config_ini_section),
    prefix="sqlalchemy.",
    poolclass=pool.NullPool,
)
```

for

```python
connectable = create_engine(get_url())
```

Don't forget the import:

```python
from sqlalchemy import create_engine
```

Enjoy!