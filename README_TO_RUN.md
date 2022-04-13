# create virtual env 
    python3 -m venv env 

# install packages
    pip install -r requirements.txt

# run script to create db, user , migrate db
    ./db.sh


# to populate db - copy and paste populate.sql into query tool in pgadmin

# run webservise 
    ./manage.py runserver
    
# visit 0.0.0.0:8000/admin  username=admin password=admin
# once you edit budget and spent amount - status of a shop will change, notifications will be shown in terminal 