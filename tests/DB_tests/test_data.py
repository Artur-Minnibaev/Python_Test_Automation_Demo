from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@127.0.0.1/postgres", echo=True, pool_size=6, max_overflow=10
)
connection = engine.connect()

select_all_query = connection.se
select_all_results = connection.execute(select_all_query)

print(select_all_results.fetchall())