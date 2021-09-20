# Health Care Website

Here's a list of the packages we will use to accomplish this:

-   Django
-   HTML5
-   CSS3
-   Javascript
-   Gunicorn
-   dj-database-url
-   psycopg2
-   whitenoise
-   and more .

## Code 

### Install Virtualenv 
```
pip install virtualenv
cd /path/to/folder
mkdir health_website
cd health_website
virtualenv .
```
### Activate the Virtualenv
```
source scripts/activate
```
### Install Dependencies
```
cd /path/to/folder/health_website
mkdir src
cd src 
git clone https://github.com/Arvind-4/HealthCare.git .
pip install -r requirements.txt
```
### Run the Code
```
cd /path/to/folder/health_website/src
./run.sh
```
### Create Super User
```
cd /path/to/folder/health_website/src
./superuser.sh
```
