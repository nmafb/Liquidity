# Add docker-compose.yml to Docket App
  cd "C:\__Meus\_Proj\Olx\Liquidity"
  docker-compose up

# Connect to Ppostgres Database com Cli
  # On Dockers "postgres" running image, execute "cli" to connect to 
  psql --host=postgres --username=postgres --dbname=postgres_db

# list Existing tables
  psql \d

# Show data directory
  SHOW data_directory;

# Create Table
  create table data_ads(date date, user_id integer, ad_id integer, category_id integer, params varchar(1000));

# Import Data:
  \copy data_ads FROM '/data_ads.csv' DELIMITER ';' CSV;

            
# Install Virtual environment
  pip install virtualenv

# Create python virtual Environment
 ->cd to project  
   python -m venv python-venv 
  
   -> # cd to project\python-venv\Scripts
       start activate
 
      -> # on new opened command prompt window, go to requirements folder
          pip install -r requirements.txt 

# check Postgres IP
  -> docker inspect postgres



