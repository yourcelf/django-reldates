import datetime, time

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def reldate(date):
    if isinstance(date, basestring):
        date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    return mark_safe("""<span class='reldate d%(milliseconds)s'>%(noscript)s</span>
    <script type='text/javascript'>
        (function() {
            var months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"],
                weekdays = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"],
                pm = ["am", "pm"];
            function setDate() {
                var el = $(".reldate.d%(milliseconds)s"),
                    date = new Date(%(milliseconds)s),
                    now = new Date(),
                    diff = (now.getTime() - date.getTime()) / 1000 / 60., // in minutes
                    disp, hours, mins;
                if (diff > 24 * 60 * 180) {
                    disp = months[date.getMonth()] + " " + date.getDate() + ", " + date.getYear();
                } else if (diff > 24 * 60 * 7) {
                    disp = months[date.getMonth()] + " " + date.getDate();
                } else if (diff > 24 * 60 * 1) {
                    disp = weekdays[date.getDay()] + ", " + (date.getHours() %% 12) + pm[parseInt(date.getHours() / 12)];
                } else if (diff > 60) {
                    hours = parseInt(diff / 60);
                    disp = hours + " " + (hours > 1 ? "hours" : "hour") + " ago";
                } else if (diff > 1) {
                    mins = parseInt(diff);
                    disp = mins + " " + (mins > 1 ? "minutes" : "minute") + " ago";
                } else {
                    disp = "just now"
                }
                el.html(disp);
            }
            setDate();
            setInterval(setDate, 1000 * 60);
        })();
    </script>
    """ % {
        'milliseconds': int(time.mktime(date.timetuple()) * 1000),
        'noscript': date.strftime("%Y-%m-%d %H:%M:%S"),
    })
reldate.is_safe = True
