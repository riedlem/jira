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

jiraSearchJql = 'project = "" AND key = ""'

url = jiraHost+"/rest/api/3/search/jql"

auth = HTTPBassicAuth(jiraUsername, jiraPassword)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

query = {
  'jql': jiraSearchJql,
  'fields': '*all'
}

response = requests.request(
  "GET",
  url,
  headers=headers,
  params=query,
  auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
