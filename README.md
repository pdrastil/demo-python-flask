# Flask demo application 
A Flask demo application that outputs current date, time, IP address and CPU load.

## Dependencies
To host the application install following packages

```sh
$ sudo apt-get -y update
$ sudo apt-get -y install python3 python3-venv python3-dev
$ sudo apt-get -y install git nginx
```

## Deployment
To deploy this application to your server run following commands:

```sh
$ git clone https://github.com/pdrastil/flask-demo
$ cd flask-demo
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip3 install -r requirements.txt
```

## Production web server
When you run the server with `flask run`, you are using a web server that comes with Flask.
This server is very useful during development, but it isn't good choise for a production use.
Instead of a Flask developent server I've decided to go with `gunicorn`, which is also a pure
Python web server, but unlike Flask's, it is a robust production server that is used by a lot
of people, while at the same time it's very easy to use.

To start web application under gunicorn you can use following command:
```sh
(venv) $ pip3 install gunicorn
(venv) $ gunicorn -b localhost:8080 -w 4 app:app
```

The `-b` option tells gunicorn where to listen for requests, which I set to internal network
interface at port 8080. It is usually a good idea to run Python web applications without
external access, and then have a very fast web server such as `nginx` that is optimized to serve
static files accepting all requests from clients. This fast web server will serve static files
directly, and forward any requests intended for the application to the internal server.

The `-w` option configures how many *workers* gunicorn will run. Having four workers allows the
application to handle up to four clients concurrently, which for a web application is usually
enough to handle a decent amount of clients, since not all of them are constantnly requesting content.

The `app:app` argument tells gunicorn how to laod the application instance. The name before
the colon is the module name, and the name after the colon is the entrypoint to of the application.

## Process supervisor
While setup is very simple, running the server from the command-line is actually not a good solution
for production. What we want is to have server running in background, and have it under constant monitoring,
because if for any reason server crashes and exits, we want to make sure new server is automatically started
in its place. Also we want to make sure that if machine is rebooted, the server will automatically start upon
boot. We are going to use `supervisor` package to do this.

```sh
$ pip3 install supervisor
```

The supervisor utility uses configuration files that tell it what programs to monitor and how to restart them when
necassary. Configuration files must be stored in `/etc/supervisor/conf.d`. Here is example configuration for this
web application.

```conf
[program:flask-demo]
command=/home/ubuntu/flask-demo/venv/bin/gunicorn -b localhost:8080 -w 4 app:app
directory=/home/ubuntu/flask-demo
user=ubuntu
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
```

After creation of configuration just reload supervisor to import new service

```sh
$ sudo supervisorctl reload
```
