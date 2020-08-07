# Django Dynaperm

Ever wanted to check the permissions in Django based on not _just_ whether or not that user has access to the correct Permissions object? What if you wanted to call a couple of different functions to see if they have rights to do so?

## Example


In your `settings.py` file
```

AUTHENTICATION_BACKENDS = (
    ...
    'dynamic_perms.DynamicBackend'
)

...

DYNAMIC_PERMISSIONS = {
    'can_do_stuff': [
        'app_name.perms.can_do_thing',
        'app_name2.permissions.has_access',
    ]
}
```

In code somewhere
```
if request.user.has_perm('can_do_stuff'):
    # Do something for authorized users.
else:
    # Do something for authenticated users.
```
