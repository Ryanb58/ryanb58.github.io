title = "A Simple Incident Report Template For Startups"
date = 2021-07-22T17:47:00+02:00
tags = [
    "incident",
    "report",
    "template",
    "startups"
]
published = true
+++++

Everyone should have a way to log incidents and track customer experience flaws. Below is a template I have implemented at a few start ups. Enjoy!

## Document:

### Customer:
This is where the customer name goes.

### Environment:
Dev/QAS/Production

### Severity Level:
SEV3/SEV2/SEV3

| Severity |                Description                |                                                                 Examples                                                                |   |   |
|:--------:|:-----------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------:|---|---|
| 1        | A critical incident with very high impact | A customer-facing service, like the app is down for ALL customers Confidentiality or privacy is breached Customer data loss             |   |   |
| 2        | A major incident with significant impact  | A customer-facing service is unavailable for a subset of customers Core functionality (e.g. sso, integration) is significantly impacted |   |   |
| 3        | A minor incident with low impact          | A minor inconvenience to customers, workaround available Usable performance degradation                                                 |   |   |

### Event Time Frame:
**First Notified:** YYYY-MM-DD HH:MM AM/PM EST - When was the first alert/notification from a user received.
**Start:** YYYY-MM-DD HH:MM AM/PM EST - When did the issue start occurring. To the best of your knowledge.
**End:** YYYY-MM-DD HH:MM AM/PM EST - Time till the issue was resolved from the customer's perspective.
**Total Time:** 1 Hour - Total amount of time. Difference between Start and End.

### Describe Issue:
What problem is being faced?

### Temporary Solution:
How did you fix the issue in the meantime?

### People Involved:
List of all the people involved.

### Investigation:
Details about the investigation. Story. Commands ran, servers looked at.. etc..

### Root Cause:
What actually caused the issue?

### Permanent Solution:
What fix/process are you going to put in place to prevent this type of issue again?

### Other Notes:
Anything else you think is relevant to this incident.


## How It's Used:

I usually create a shared folder named `Incident Reports` and place the template in a file named `_TEMPLATE----YYYY-MM-dd-CustomerName-SEV#-Total-Time`. This forces the template to the top of the sorted list of files. Then, when an incident occurs, we simple make a copy of the template and start filling it out with all the details, replacing all placeholders. 

## Sources:

https://www.atlassian.com/incident-management/kpis/severity-levels