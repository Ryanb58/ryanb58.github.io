title = "How to Encrypt an Existing RDS Instance at REST"
date = 2021-08-28T17:47:00+02:00
tags = [
    "aws",
    "rds",
    "encryption",
    "unencrypted"
]
published = true
+++++

Make sure that anything connected to your database is using an DNS entry to connect. If they connect directly to the AWS Endpoint, then you will have to manually update your application to connect to a "new" endpoint after it is created.

1. Create a snapshot of the database.
1. Clone the snapshot and enable "encryption".
1. Restore the snapshot to an instance of similar configuration. Make sure you check your VPC, subnets, security groups, Parameter group, and Option groups.
1. Update the DNS entry to point to the new instance.
1. Stop the unencrypted instance.
1. Verify the application still works.
1. Delete the stopped unencrypted instances.

Enjoy!
