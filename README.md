an online shop for scuba diving enthusiasts

TODO: login with a wrong password leads to attribute error:
AttributeError at /login/
'AnonymousUser' object has no attribute '\_meta'
accounts -> forms -> authorize
/home/ldm/.local/share/virtualenvs/scuba-stop-HdR5nuhF/lib/python3.9/site-packages/django/contrib/auth/**init**.py
line 87

TODO: users aren't supposed to set the discount value in their orders

TODO: categories embedded in orders should have category name instead of url
NOTE: this is the expected behavior with hyperlinked relations
SOLUTION: descriptive hyperlinks can be set with slug values

TODO: merge the accounts and shop api routers (possibly not by placing the router in config)
