# How to use
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
Unit Testing is performed through pytest on 4 separate tests. To execute unit testing, execute the following command from the root directory while the api is running!
```
pytest -v
```
