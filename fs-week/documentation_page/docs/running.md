# How to run the model as a separate service

This app is designed to be run inside Flask. The machine learning models are running in `service_1.py` and `service_2.py`. The main app is inside `app.py`.
 If you run any of the apps in a different port, check the python files and modify them accordingly.

To run the apps use:

```bash
FLASK_ENV=development FLASK_APP=service_1.py flask run --port 5005
```

```bash
FLASK_ENV=development FLASK_APP=service_2.py flask run --port 5004
```

```bash
FLASK_ENV=development FLASK_APP=app.py flask run --port 5002
```

Now you can navigate to [127.0.0.1:5002](127.0.0.1:5002) and use your app. The main `app.py` calls `service_1.py` to first classify if an input image is valid or not, ie is bees/ants or a "random" image. If it passes the first classification of being valid, `service_2.py` does the predictions.

At the top fo the Flask apps there are a few configuration variables. They are mostly about the paths to find the files we need and the name of the files (for example the weights of the best performing model). Modify those if you change the project structure.
