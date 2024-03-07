# MiniSeries of tutorials and my personal learning notes on Django

_By [Diego Jacobo Martínez](https://github.com/Djmr5)_

## Table of Contents

1. [Introduction](#introduction)
2. [Django](#django)
3. [PostgreSQL Database Setup](#postgresql-database-setup)

## Introduction

Django is a high-level Python Web framework that encourages rapid and clean development, as well as pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free, open source and has a thriving community.

This framework is based on the MVC (Model-View-Controller) pattern, but it is not a strict implementation of it. It is a framework that follows the DRY (Don't Repeat Yourself) principle, which means that it avoids repeating code, and it is also based on the principle of convention over configuration, which means that it is not necessary to configure everything, since it already has a default configuration. Based on the "batteries included" principle, it has a large number of libraries that facilitate the development of web applications.

The contents of this repository aim to be a series of tutorials and my personal learning notes on Django. To help others and myself to learn this framework. In this project I will be coding ways of implementing a Django application using PostgreSQL as a database with multiple schemas.

## Django

## PostgreSQL Database Setup

It's recommended to create a new user for the database, and a new schema for each application. This way you can have multiple applications using the same database. __Remember to give authorization to the user to access the database and the schemas.__

```sql
CREATE USER diego WITH PASSWORD 'Mypass123';
GRANT ALL PRIVILEGES ON DATABASE django TO diego;
```

```sql
CREATE SCHEMA IF NOT EXISTS django AUTHORIZATION diego;
CREATE SCHEMA IF NOT EXISTS hr AUTHORIZATION diego;
CREATE SCHEMA IF NOT EXISTS sales AUTHORIZATION diego;
```

## Django Configuration

### Create different databases for each schema & a database router

```python
# core/settings.py
DATABASE_ROUTERS = ('core.db_router.DBRouter',)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "OPTIONS": {"options": "-c search_path=django,public"},
        "HOST": os.environ.get("POSTGRESQL_HOST"),
        "PORT": os.environ.get("POSTGRESQL_PORT"),
        "NAME": os.environ.get("POSTGRESQL_NAME"),
        "USER": os.environ.get("POSTGRESQL_USER"),
        "PASSWORD": os.environ.get("POSTGRESQL_PASS"),
    },
    "hr": {
        "ENGINE": "django.db.backends.postgresql",
        "OPTIONS": {"options": "-c search_path=hr,public"},
        "HOST": os.environ.get("POSTGRESQL_HOST"),
        "PORT": os.environ.get("POSTGRESQL_PORT"),
        "NAME": os.environ.get("POSTGRESQL_NAME"),
        "USER": os.environ.get("POSTGRESQL_USER"),
        "PASSWORD": os.environ.get("POSTGRESQL_PASS"),
    },
    "sales": {
        "ENGINE": "django.db.backends.postgresql",
        "OPTIONS": {"options": "-c search_path=sales,public"},
        "HOST": os.environ.get("POSTGRESQL_HOST"),
        "PORT": os.environ.get("POSTGRESQL_PORT"),
        "NAME": os.environ.get("POSTGRESQL_NAME"),
        "USER": os.environ.get("POSTGRESQL_USER"),
        "PASSWORD": os.environ.get("POSTGRESQL_PASS"),
    },
}
```

*Note:* Maybe it's possible to create a field in the model Meta class to specify the schema, but I haven't tried it yet.

```python
# core/db_router.py
from hr.models import Employee
from sales.models import Sale

HR_MODELS = [Employee]
SALES_MODELS = [Sale]

class DBRouter(object):

    def db_for_read(self, model, **hints):
        if model in HR_MODELS:
            return 'hr'
        elif model in SALES_MODELS:
            return 'sales'
        return None

    def db_for_write(self, model, **hints):
        if model in HR_MODELS:
            return 'hr'
        elif model in SALES_MODELS:
            return 'sales'
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db in ('hr', 'sales'):
            if app_label == 'hr' and db == 'hr':
                return True
            elif app_label == 'sales' and db == 'sales':
                return True
            # Allow migration for other databases that might not be explicitly mentioned
            return False
        # Allow migration for the default database or any other database not explicitly mentioned
        return True
```

## Migrations

Using the command `python manage.py migrate` may not successfully apply the migrations for all the databases. So it's better to create the migrations for each database separately.

```bash
python manage.py migrate --database=default
python manage.py migrate --database=hr
python manage.py migrate --database=sales
```

## Considerations

As for now, Django don't support multi-schema and there are lots of issues open on the topic. So, this is a workaround to use multiple schemas with Django.

1. An issue that I found is that you should stick to using foreign keys only within the same schema (Application). If you try to use a foreign key from one schema to another, you will get an error. So, if you need to use foreign keys between schemas, might be better to 

