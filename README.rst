django-reldates
===================================================

A filter for Django templates which does self updating dates that are relative to the current time.  For short times, it does "time since" style dates (e.g. "3 minutes ago"), but for longer times, it does something more comprehensible (such as "thursday, 3pm" or "jan 3, 2008").  Where javascript is not available, it simply prints the date in `%Y-%m-%d %H:%M:%S` form.

Includes a single template filter, "reldate", which expects a date in either
string or datetime.datetime form.

Usage::

    {% load reldates %}

    {{ mymodel.date|reldate }}

Examples:

+---------------------+-----------------+
+ Time since          | Example Output  |
+=====================+=================+
| < 1 min             | just now        |
+---------------------+-----------------+
| 1 min to 59 min     | 3 minutes ago   |
+---------------------+-----------------+
| 60 min to 24 hours  | 6 hours ago     |
+---------------------+-----------------+
| 24 hours to 7 days  | thursday, 3pm   |
+---------------------+-----------------+
| 7 days to 6 months  | jan 3           |
+---------------------+-----------------+
| > 6 months          | jan 3, 2008     |
+---------------------+-----------------+

Related
-------
https://docs.djangoproject.com/en/dev/ref/templates/builtins/#timesince

