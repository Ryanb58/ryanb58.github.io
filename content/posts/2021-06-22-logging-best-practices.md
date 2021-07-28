title = "Logging Best Practices"
date = 2021-06-22T00:00:00+02:00
tags = [
    "logging",
    "elk",
    "python",
    "django",
    "logs",
    "log"
]
published = true
+++++

Here are just a few bullet points I've gathered over my career about logging.

#### Log to STDOUT/STDERR

Stop following all the online tutorials for your framework that configure your application to store logs directly in files. This is a rookie mistake and makes running your application so much more difficult than it needs to be. Instead, give your ops team better lives by sending your logs to `stdout/stderr`. This allows OPs to decide how to process and send off logs. They might choose to write them to disk, perform some cleanup data processing, or simply send logs to an external system. By logging directly to stdout/stderr you give them the choice.

"A twelve-factor app never concerns itself with routing or storage of its output stream." - [12 Factor App](https://12factor.net/logs)

#### Format Your Logs

You don't know how important good, standard formatting can be until you have to sift through multiple log files across different machines. Define a standard formatter and enjoy. I personally like the idea of all logs being provided as JSON dicts. Doing so makes parsing so much easier by LogStash. I also, don't have to worry as much about log format changes.

#### Centralize your logs(i.e. DevOps)

This can't be understated. As the software grows so do the sources of your logs. Moving around amongst EC2 instances that log directly to ephemeral storage is a pain. Especially if one of those instances is terminated by autoscaling, which you needed the logs from to help with a customer support ticket. You'll thank me for this tip one day.

I recommend setting up an ELK stack for this action, or perhaps use a paid tool like DataDog.

#### Auto vs Programmer Generated Logs

The importance of having both auto generated logs and programmer logs can't be pushed enough. Auto-generated logs give you insights into everyday events such as GET and POST events to certain api endpoint, meanwhile programmer logs give you the insight into who did what when. The combination of these two types of logs are instrumental to addressing customer service needs. 

#### Date-Time Formats

Spitting out date-time values as human-readable seems like a good idea, until you are tasked with parsing through the logs using a date-time range. Use the unambiguous format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601). You'll pat yourself on the back for doing this one, as it makes navigating your logs much easier.

#### Add Logging Context

It's difficult to navigate logs when they have no context. These are three must haves for any SAAS application.

- Tenant ID  - Know the active tenant.
- User ID    - Know the user performing the action.
- Request ID - Usually provided by your Load Balancer. Look at the `X-REQUEST-ID` header. Allows you to see all the logs associated with a single request.

#### Conclusion

At the end of the day, I hope you take logging a bit more seriously. Your customers and users deserve it. Till next time. Peace
