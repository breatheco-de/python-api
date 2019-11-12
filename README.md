# Breathecode Python APIs

## Description

An extendable API microservices framework for Breathecode APIs, written in Python3/Flask.

## Endpoints

### Slack (/api/slack)

The academy slack channel has a command in the format `/bc <command> <parameter>`. When triggered, it will access this api.

#### Command: Student
takes an `email` parameter and will return specific fields about the student from the student API. 

Command: `/bc student joey@gmail.com`
Response:
```json
{
    "full_name": "Joey Smith",
    "cohorts": [
        "MDC-X"
    ],
    "github_username": "jsmithy",
    "status": "active",
    "financial_status": "unknown",
    "phone": "954-555-121",
    "student_external_profile": "https://www.blah.com/jsmithy"
}
```
