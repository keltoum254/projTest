set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
# python manage.py createsuperuser --noinput
python manage.py makemigrations
python manage.py migrate