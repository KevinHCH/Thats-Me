FROM postgres:12 

ENV POSTGRES_PASSWORD=1234

# Copiará este archivo al container y lo ejecutará
COPY ./app/schema.sql /docker-entrypoint-initdb.d/

#EXPOSE 5432
