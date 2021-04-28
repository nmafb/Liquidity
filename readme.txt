# Add docker-compose.yml to Docket App
cd "C:\__Meus\_Proj\Olx\Liquidity"
docker-compose up



# Connect to Ppostgres Database com Cli
  psql --host=postgres --username=postgres --dbname=postgres_db

# list Existing tables
  psql \d

# Show data directory
  SHOW data_directory;

# Cant connect to Postgres with PgAdmin
  # List networks
    <cmd line> docker network ls
    <cmd line> docker network inspect liquidity_postgres-compose-network



# Create Table
  create table data_ads(date date, user_id integer, ad_id integer, category_id integer, params varchar(1000));

# Import Data:
\copy data_ads FROM '/src/data/data_ads.csv' DELIMITER ';' CSV;
            
# Run Pyton on virtual environment
