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

1) Create a snapshot of the database.
2) Clone the snapshot and enable "encryption".
3) Restore the snapshot to an instance of similar configuration. Make sure you check your VPC, subnets, security groups, Parameter group, and Option groups.
4) Update the DNS entry to point to the new instance.
5) Stop the unencrypted instance.
6) Verify the application still works.
7) Delete the stopped unencrypted instances.

Enjoy!
