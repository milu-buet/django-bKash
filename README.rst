=====
bKash_payment
=====

bKash_payment is a simple Django app to conduct Web-based bKash payment. 

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Installation:

	pip install django-bKash

2. Add "bKash_payment" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'bKash_payment',
    )

3. Include the bKash_payment URLconf in your project urls.py like this::

    url(r'^bKash_payment/', include('bKash_payment.urls')),

4. Run `python manage.py migrate` to create the bKash payment related table.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to get necessary access.

6. Visit http://127.0.0.1:8000/bKash_payment/ to manage the bkash payment.