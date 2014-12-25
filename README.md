ban2stats_v2
============

Stats for Fail2Ban (for relational database)

Overview
--------



Installation
------------

#. Install following libraries::

    geos
    elasticsearch
    python


#. Create an empty virtualenv and install more library using Pip::

    pip install -r ban2stats/ban2stats/setup/requirements.txt


Configuration
-------------

    create local.py under ban2stats/ban2stats/settings/
    - database configuration
    - ElasticSearch configuration (HAYSTACK_CONNECTIONS)
    - BAN2STATS_SERVICE_TOKEN (should match with client's TOKEN)

    In ban2stats/client/webservice_client.py
    - WEBSERVICE_HOST
    - TOKEN (should match with Banstats's BAN2STATS_SERVICE_TOKEN in settings)

    In ban2stats/webpage/index.html
    - api_host

Run
---

#. ElasticSearch
   Run ElasticSearch

#. Ban2Stats Web Service
   Run Ban2Stats

#. Ban2Stats Web Page



