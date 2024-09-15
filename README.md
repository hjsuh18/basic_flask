# Set up instructions

## Postgresql
```
# Initalize database cluster
initdb /usr/local/var/postgresql@14a

# Start database server
pg_ctl -D '/usr/local/var/postgresql@14' -l logfile start

# Shut down database server
pg_ctl stop -D /usr/local/var/postgresql@14

# Create a new database
createdb -U postgres basic_flask

# Connect to database. basic_flask is the database name
psql -U postgres -d basic_flask
```

## Flask
```
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```