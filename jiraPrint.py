import json
import requests
from atlassian import Jira
from datetime import date
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from pprint import pprint
from requests.auth import HTTPBasicAuth

jiraHost = "atlassian.net"
jiraUsername = ""
jiraPassword = ""

url = jiraHost+"/rest/api/3/search/jql"

auth = HTTPBassicAuth(jiraUsername, jiraPassword)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

jiraSearchJql = 'project = "" AND key = ""'
