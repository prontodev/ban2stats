ban2stats
============

Stats for Fail2Ban (for relational database)

#Overview

   See diagram at https://github.com/prontodev/ban2stats/blob/master/docs/Ban2Stats_diagram.pdf

### Ban2Stats Web Service
   Ban2Stats Web Service is a Django web application and also use Haystack to connect with ElasticSearch.
   It saves attack details to database and sends data to ElasticSearch.

### Ban2Stats Web Page
   A static web page that display Statistics from Ban2Stats Web Service. In the HTML page contains Javascript that will make Ajax calls to Ban2Stats Web Service and then display content on the page.

### Ban2Stats Client
   is a Python script that makes HTTP Request to Ban2Stats web service API. The client is used by Fail2Ban hook.

### ElasticSearch
   ElasticSearch is used to do search and indexing for Ban2Stats Web Service

#Dependencies

### Install following libraries
* geos
* elasticsearch
* python

### For Ban2Stats Web Service, Create an empty virtualenv and install more library using Pip::

    pip install -r ban2stats/ban2stats/setup/requirements.txt

### For Ban2Stats Client

    pip install -r ban2stats/client/requirements.txt

#Configuration

Create local.py under ban2stats/ban2stats/settings/

* database configuration
* ElasticSearch configuration (HAYSTACK_CONNECTIONS)
* BAN2STATS_SERVICE_TOKEN (should match with client's TOKEN)

#Installation

To work with indexing, Ban2Stats Web Service will feed data to ElasticSearch.
For the first time, run follow command to create index for ElasticSearch at Ban2Stats Web Service.

    python manage.py rebuild_index


To update index for ElasticSearch (more details on Haystack):

    python manage.py update_index

And please setup your system cron job to update index (For example for every 10 min):


In ban2stats/client/webservice_client.py

* WEBSERVICE_HOST
* TOKEN (should match with Banstats's BAN2STATS_SERVICE_TOKEN in settings)


In ban2stats/webpage/index.html

* api_host


#Run

### ElasticSearch
   See ElasticSearch documentation.

### Ban2Stats Web Service
   Ban2Stats Web Service is a Django web application. Please see Django document on how to setup production server.
   To run development server run:

       python manage.py runserver


### Ban2Stats Web Page
   You can run this using any static web server.

   if you want to run it using Python

       python -m SimpleHTTPServer 80



