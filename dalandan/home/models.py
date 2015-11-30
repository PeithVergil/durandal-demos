from django.db import models
from django.utils.translation import ugettext_lazy as _


class Todo(models.Model):

    title = models.CharField(_('title'), max_length=200)

    STATUS_DONE = 1

    STATUS_CHOICES = (
        (STATUS_DONE, _('Done')),
    )

    status = models.SmallIntegerField(_('status'), choices=STATUS_CHOICES)

    # Date the todo was created.
    date_created = models.DateTimeField(auto_now_add=True)

    # Date the todo was updated.
    date_updated = models.DateTimeField(auto_now=True)

    @property
    def done(self):
        """
        Check if the todo is done or not.
        """
        return self.status == self.STATUS_DONE
