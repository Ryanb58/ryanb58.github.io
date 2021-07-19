The words `authentication` and `authorization` are often used interchangably. This is wrong. Both are fundamentally different by definition.

**Authentication:** Verify WHO the user is.

Example: Who is the logged in user?

**Authoriation:** Verify the user has the proper permissions to manipulate or retrieve a resource.

Example: Does the logged in user have access to the billing preferences?

From the definitions above you can see that `Authentication` is more about WHO is logged in, whereas `Authorization` is more about WHAT the user has access too. By locking this little detail into your memory, you can reduce your likelyhood of screwing up vital code. 

While you are at it.. maybe add some unittests around that codeblock. Doing so helps keep security methods secure.


Sources:

https://auth0.com/docs/get-started/authentication-and-authorization

