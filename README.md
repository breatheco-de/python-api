# Breathecode Python APIs

## Endpoints

### Slack (/api/slack)

The academy slack channel has a command in the format `/bc <command> <parameter>`. When triggered, it will access this api.

#### Student
takes an `email` parameter and will return specific fields about the student from the student API. 

Command: `/bc student joey@gmail.com`
Response:
```json
{
    "full_name": "Joey Smith",
    "cohorts_taken": [
        "MDC-X"
    ],
    "github_username": "jsmithy",
    "status": "Active"
    "finantial_status": "unknown",
    "email": "joey@gmail.com",
    "phone": "954-555-121",
    "student_external_profile": "https://www.blah.com/jsmithy"
}
```
