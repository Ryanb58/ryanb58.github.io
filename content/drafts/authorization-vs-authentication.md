The words `authentication` and `authorization` are often used interchangably. This is wrong. Both are fundamentally different by definition.

**Authentication:** The act of verifying WHO is the user.

Example: Who is the logged in user?

**Authoriation:** Ensures the user has the proper permissions to retrieve or manipulate a resource.

Example: Does the logged in user have access to the billing preferences?

From the definitions above you can see that `Authentication` is more about WHO is logged in, whereas `Authorization` is more about WHAT the user has access too. By locking this little detail, you can reduce your likelyhood of screwing up vital code. 

Another great idea.. would be writing tests around your authentication code to ensure other devs don't abuse it.


Sources:

https://auth0.com/docs/get-started/authentication-and-authorization

