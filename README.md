# CronWard

CronWard is a service designed for monitoring cron jobs. It tracks incoming HTTP requests and email messages ("pings") from your cron jobs and scheduled tasks ("checks"). If a ping fails to arrive on time, CronWard triggers alerts to notify you.

CronWard includes a web-based dashboard, an API, over 25 integrations for notifications, monthly email reporting, WebAuthn 2FA support, and team management capabilities such as projects, team members, and read-only access.

The core technologies are:

* Python 3.10+
* Django 5.1
* PostgreSQL or MySQL

CronWard is distributed under the BSD 3-clause license.

Screenshots:

The "My Checks" dashboard displays the status of all your cron jobs, updating in real-time.

![Screenshot of My Checks page](/static/img/my_checks.png?raw=true "My Checks Page")

Each check offers configurable Period and Grace Time settings. The Period represents the expected time between pings, while Grace Time determines how long to wait before issuing an alert if a job is delayed.

![Screenshot of Period/Grace dialog](/static/img/period_grace.png?raw=true "Period/Grace Dialog")

You can also set the expected schedules using cron expressions. CronWard utilizes the [cronsim](https://github.com/cuu508/cronsim) library to parse and assess cron expressions.

![Screenshot of Cron dialog](/static/img/cron.png?raw=true "Cron Dialog")

The Check Details page features a live-updating event log.

![Screenshot of Check Details page](/static/img/check_details.png?raw=true "Check Details Page")

CronWard offers status badges that are publicly accessible but difficult to guess. These badges can be incorporated into your READMEs, dashboards, or status pages.

![Screenshot of Badges page](/static/img/badges.png?raw=true "Status Badges")


## Setting Up for Development

To configure the CronWard development environment:

* Begin by installing the necessary dependencies on Debian/Ubuntu: 
```sh
sudo apt update sudo apt install -y gcc python3-dev python3-venv libpq-dev libcurl4-openssl-dev libssl-dev 
```

* Create a directory for the project code and set up a virtual environment. You can choose a different location if desired: 
```sh
mkdir -p ~/webapps cd ~/webapps 
```

* Set up the virtual environment. Virtualenv provides pip, which will be used shortly to install the required packages:
```sh
python3 -m venv hc-venv source hc-venv/bin/activate pip3 install wheel # ensure wheel is installed in the venv 
```

* Clone the project repository: 
```sh
git clone https://github.com/CronWard/CronWard.git
```

* Install the necessary packages, including Django, within the virtual environment: 
```sh 
pip install -r CronWard/requirements.txt 
```

* For macOS users: Reinstall pycurl using the following method (this assumes OpenSSL was installed via brew): 
```sh 
export PYCURL_VERSION=`cat requirements.txt | grep pycurl | cut -d '=' -f3` export OPENSSL_LOCATION=`brew --prefix openssl` export PYCURL_SSL_LIBRARY=openssl export LDFLAGS=-L$OPENSSL_LOCATION/lib export CPPFLAGS=-I$OPENSSL_LOCATION/include pip uninstall -y pycurl pip install pycurl==$PYCURL_VERSION --compile --no-cache-dir 
```

* Create database tables and a superuser account:

  ```sh
  cd ~/webapps/CronWard
  ./manage.py migrate
  ./manage.py createsuperuser
  ```

  With the default configuration, CronWard stores data in a SQLite file
  `hc.sqlite` in the checkout directory (`~/webapps/CronWard`).

* Run tests:

  ```sh
  ./manage.py test
  ```

* Run development server:

  ```sh
  ./manage.py runserver
  ```

The site should now be running at `http://localhost:8000`.
To access Django administration site, log in as a superuser, then
visit `http://localhost:8000/admin/