import json
import requests
from atlassian import Jira
from datetime import date
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from pprint import pprint
from requests.auth import HTTPBasicAuth

jiraSearchJql = 'project = "" AND key = ""'
