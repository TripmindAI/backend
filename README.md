# Back-end
## How to run and test locally
Install & update all dependencies
```bash
pip install -r requirements.txt

```
Run uvicorn server on your local machine.
```bash
uvicorn src.main:app --reload
```

## Commit and Push
Whenever you're ready to push your commits, don't forget update python dependencies `requirement.txt`
```bash
pip freeze > requirements.txt
```

Add `/doc` at the end of url then you can test backend apis.

## Database Migration
The project database migrations are managed by [alembic](https://alembic.sqlalchemy.org/en/latest/). 

Whenever you edit `src/db/models.py` database schema file, use the following command to apply your migration your edition.

```bash
alembic revision --autogenerate -m "message"

```
Alembic will generate a migration file for you.

Please replace the message with a brief description of what this migration is for. 

Please review your migration carefully in case any errors or unexpected issues.

Finally, use the following command to apply your migraion to database.

```bash
alembic upgrade head
```

## Get the test token

https://manage.auth0.com/dashboard/us/tripmindai/apis/65e3b879e5f3ceca8ed7e227/test