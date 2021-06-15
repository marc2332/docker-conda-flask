## About
This image runs a web server with [Flask](https://flask.palletsprojects.com/en/2.0.x/), which is installed with conda.

- Host port: 80
- Flask port: 5000
- Container name: web_server
- Image name: conda-flask

## Usage

- Build the image:
    ```shell
    docker build -t conda-flask .
    ```

- Run the container:
    ```shell
    docker run -dp 80:5000 --name web_server conda-flask
    ```

- Visit [localhost](http://localhost).

- Stop the container:
    ```shell
    docker container stop web_server 
    ```

- Remove the container:
    ```shell
    docker container rm web_server 
    ```