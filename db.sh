#! /bin/bash
echo "Run postrgesql"
docker rm -f budget
docker run --name budget \
-p 5432:5432 \
-e POSTGRES_PASSWORD=root \
-e POSTGRES_USER=root \
-e POSTGRES_DB=budget \
-d postgres

sleep 10
# -d postgres


#! /bin/bash

echo "create tables"
python3 manage.py makemigrations 
python3 manage.py migrate

echo "create superuser"

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@budhet.com', 'admin')" | python manage.py shell

