# Hokodo Programming Challenge - Reading List API

A a simple, 2 endpoint JSON api that fetches data from an external source. 

## Getting Started
These instructions will get the project running on your machine

### Prerequisites 
```
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
    
7. Make HTTP GET requests to the ```localhost:8000/books``` and ```localhost:8000/authors``` endpoints. Alternatively,
navigate to these urls in the browser to use Django Rest Framework's built in API Explorer

8. To sort the results from the books endpoint use the ```ordering``` query param. Set the param to the field that you 
wish to order on and prepend it with ```-``` to show the results in descending order

Example urls:
- ```localhost:8000/books?ordering=-title``` will return a list of books ordered by descending alphabetical title order
- ```localhost:8000/books?ordering=published``` will return a list of books in ascending date order
## Project Notes
### Design Decisions
The project has been implemented using Django and Django Rest Framework. DRF in particular was chosen because it 
provides the capability to quickly provision a working REST API with minimal setup and includes useful features like
a web based API explorer.

The requests library has also been used to simplify the construction and execution of HTTP requests to an external service

The application is entirely stateless. Should it need to handle high load/traffic, it can easily be horizontally scaled 
simply by deploying more instances of the application across multiple machines with a load balancer in front of them.
In this instance it may be useful to implement a centralized logging solution

The httpretty library has been used for testing purposes. It allows us to mock http requests to the external service.
Currently it is only used to mock error responses to test the error handling, see Potential Improvements for how we could
utilize this further
### Assumptions
- The API will be publicly available. The project currently implements no method of authentication or authorization,
if it were to be deployed to the internet, it would be accessible by anyone.
- There is no requirement for logging or auditing. 
### Potential Improvements
- To reduce traffic to the external service, it might be useful to implement a caching strategy. It would be relatively
simple with the current implementation to save the books in the reading list to a database and have subsequent requests
served by reading from the database. The cached records in the database could be refreshed after a specified time interval
- The tests currently make live requests to the external service and compare against static values. Should the data change,
the tests will fail. We could improve this by mocking out the requests to the external service

# Hokodo Programming Challenge 2 - Word Frequency Counter
The word frequency calculator can be found in ```hokodo_frequency_challenge.py``` in the root of the project.
## Getting Started
### Prerequisites
```You should have Python 3.x installed on your machine```
### Running The Program
Execute the program using ```python hokodo_frequency_challenge.py```

You will be prompted for an input string - type in your input and hit enter

