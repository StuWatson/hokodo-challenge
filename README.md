# Hokodo Programming Challenge - Reading List API

A a simple, 2 endpoint JSON api that fetches data from an external source. 

## Getting Started
These instructions will get the project running on your machine

### Prerequisites 
```$xslt
You should have Python 3.x installed on your machine
```
### Installation
1. Clone or download the source code

2. (Optional) Set up and activate a [Python venv](https://docs.python.org/3/library/venv.html) to cleanly manage your dependencies

3. Install the project requirements (in the project root directory)
    - If you would like to run the tests as well as the application, use:
    ```pip install -r dev-requirements.txt```
    - If you would only like to run the application, use:
    ``` pip install -r requirements.txt```

4. Perform the Django migrations - We aren't saving anything to the database at this stage, but we are using Django's built in models
with Django Rest Framework's Serializers to  serialize/deserialize the data. Django requires us to run this step ```python manage.py migrate```

5. Run the Tests with ```python manage.py test```

6. Run the application with
    ```python manage.py runserver```
