# Dokcare:

Welcome to **Dokcare**, your one-stop solution for healthcare appointments. Join us at Dokcare and take the first step towards better health.

## Screenshots:

<img src="https://github.com/Arvind-4/dokcare/blob/main/.github/static/homepage.png?raw=true" alt="Home Page" />

## 📦 Tech Stack:

- [Django](https://www.djangoproject.com) - Django makes it easier to build better web apps more quickly and with less code.
- [Solid Js](https://www.solidjs.com/)  - A Reactive JavaScript Library.
- [Vite](https://vitejs.dev/)  - Next Generation Frontend Tooling.
- [CockroachDB](https://www.cockroachlabs.com/)  - A distributed SQL database designed for speed, scale, and survival.


Deployed on [Vercel](https://vercel.com/). <br/>
Click Here for [Live Preview.](https://dokcare.vercel.app/)



## Deploy Now:
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Arvind-4/dokcare/)

## Getting Started: 

- Clone Repo 

```bash
cd /path/to/folder
mkdir dokcare
cd dokcare
git clone https://github.com/Arvind-4/dokcare.git .
```  

- Create a Virtual Environment

```bash
cd dokcare
python3.9 -m venv .
source bin/activate
```

**For Windows use:** `.\Scripts\activate`

- Install Dependencies

```bash
pip install -r requirements.txt
```

Add Your Environment variable to `.env`.
 Refer `.sample.env` file.

- Make Migrations

```bash
cd /path/to/folder/dokcare
python manage.py makemigrations
python manage.py migrate
```

- Build Frontend

```bash
cd /path/to/folder/dokcare
npm run i
npm run production
```

- Run Dev Server

```bash
python manage.py runserver localhost:8000
```

Open [localhost:8000](http://localhost:8000/) in Browser.
