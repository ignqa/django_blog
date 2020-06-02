# Django Blog
The implemented features are the next:

* Data models (with admin portal through the ORM).
* Forms
* Share post by email
* Post comments
* Tagging mechanism for the posts
* Template tags and filters
* Sitemap
* RSS feeder for blog suscriptions
* Search engine based on trigrams over PostgreSQL.

# Setup
1. `pip install -r requirements.txt`
2. `python manage.py runserver`
3. Urls are:
    * `http://localhost:8000/blog`
    * `http://localhost:8000/blog/search`
    * `http://localhost:8000/admin`
        * User: `igaznav`
        * Password: `admin123*`