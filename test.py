import requests
import json

url = "https://f20dfcef729f.ngrok-free.app/graphql"  # ✅ same as Postman

query = """
query GetCallDataTranscribe {
  getCallDataTranscribe(fromDate: null) {
    recordingsS3Url
    s3Uploaded
    entityId
    callId
    entityName
    state
    phone
    city
    country
    status
    description
    securityDeposit
    minRent
    maxRent
    ownerName
    email
    startedYear
    fullTimeWarden
    visitorsAllowed
    website
    entityType
    totalBeds
  }
}
"""

headers = {
    "Content-Type": "application/json",
    "ngrok-skip-browser-warning": "1"
}

response = requests.post(url, json={"query": query}, headers=headers)

print(response.status_code)
print(json.dumps(response.json(), indent=2))
