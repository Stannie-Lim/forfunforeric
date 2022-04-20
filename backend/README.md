1. sudo pip3 install virtualenv (sorry eric idk how to do this on windows)
2. virtualenv env # this creates the virtual env in a folder called `env`
3. source env/bin/activate # this starts the virtual env
4. python3 -m pip install Flask flask_cors # install the Flask and flask_cors dependency
5. flask run
6. this is running on http://127.0.0.1:5000. your frontend api calls should start with `http://127.0.0.1:5000`