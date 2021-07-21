# Flask-API
Flask-API is a simple, small, operable web-style API, where a user (through JSON payload) sends in a number to be multiplied by 1337, returning the result in JSON format.

## How to use
First clone the repository
```
git clone https://github.com/splishie/flask-api.git
```

The api will run locally, to do this, a docker-compose file has been provided in the root directory that will run an instance of the api. To start the api from the root directory, run the following command:
```
docker-compose up
```
Or if you want to run it in detached mode:
```
docker-compose up -d
```

The api can then be accessed through the browser of your choice on the following:
```
localhost:5000
```

## Container
A Dockerfile has been provided for the api if you wish to run it in docker. To build the image, issue the following command:
```
docker build . -t flaskapi:latest
```

## Testing
Basic testing has been included as part of this api. This includes unit testing.

### Unit Testing
Unit Testing is performed through pytest on 4 separate tests. To execute unit testing, execute the following command from the root directory while the **api is running**
```
cd tests/
pytest -v tests.py
```
## Tasks
**You can use a tool such as [Postman](https://www.postman.com/) to verify these tasks without the need of [pytest](https://docs.pytest.org/en/6.2.x/)**
### A health endpoint which returns an appropriate response code
```python
@api.route('/health')
def health():
    return "Success"
```
*  As a running webpage defaults to a 200 response, there is no need to specify a 200 response on the health endpoint, hence it will only show "Success"

### A simple elite 'math' endpoint using multiplication to multiply the posted number (in JSON payload) by 1337 and return the result in JSON
* Max limit on returned value is 10,000,000
    ```python
    if result > limit:
        return "Returned value higher than 10,000,000", 400
    return jsonify({"result": result})
    ```
    * This shows that if the multiplied result is greater than 10,000,000, it will show an error and return a 400 response code, if it's less, it will proceed to show the result of the multiplication and return a 200 response code
* 200 response code is returned for successful processing and return
    * As mentioned before, on success, the webpage will default to a 200 response so there is no need to specify the response code
* Non-200 response code is returned for unsuccessful processing
    ```python
    if 'num' not in req_data:
        return "Invalid JSON", 400
    ```
    ```python
    except:
        return "Input value not an integer", 400
    ```
    * If the input value is either an invalid JSON or not an integer, it will return its designated message and give a 400 response error
    

