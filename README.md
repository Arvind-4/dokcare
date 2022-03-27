# Health Care Website

Vist the [Website](https://healthcarewebsite.herokuapp.com/).

Here's a list of the packages we will use to accomplish this:

-   Django (Async)
-   HTML5
-   CSS3
-   Javascript
-   Gunicorn
-   Uvicorn
-   Cockroach DB
-   whitenoise
-   Vite
-   and more .

## Code 

### Install Virtualenv 
```
python3.9 -m pip install virtualenv
cd ~/Dev
mkdir health_website
cd health_website
python3.9 -m virtualenv .
```
### Activate the Virtualenv
```

source bin/activate
```

### Install Dependencies
```
cd /path/to/folder/health_website
git clone https://github.com/Arvind-4/HealthCare.git .
poetry install
```

### Run Frontend
```
cd ~/Dev/health_website/frontend
npm i
npm run production
```

### Run the Backend
```
cd ~/Dev/health_website/web
python manage.py runserver 
```
### Change Log
[Logs](https://github.com/Arvind-4/HealthCare/commits)
