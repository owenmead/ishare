from django.db import models
from django.contrib.auth.models import User

class ItemContainer(models.Model):
    name = models.CharField(max_length=50)
    items = models.ManyToManyField("Item")

    owner = models.ForeignKey(User, related_name='owner')
    sharedWith = models.ManyToManyField(User, blank=True)

    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User)

    class Meta:
        ordering = ["name"]

    def is_available(self):
        for history in self.history_set.order_by('-date')[:1]:
            # If last action was returned, then it's available
            return history.action == 'R'
        # No history, so it is available
        return True

    def __unicode__(self):
        return self.name

HISTORY_ACTIONS = (
    ('B', 'Borrowed'),
    ('R', 'Returned'),
)
HISTORY_CONDITION = (
    (7, 'Brand New'),
    (6, 'Great'),
    (5, 'Very Good'),
    (4, 'Good'),
    (3, 'Fair'),
    (2, 'Poor'),
    (1, 'Aweful')
)
class History(models.Model):
    action = models.CharField(max_length=1, choices=HISTORY_ACTIONS)
    condition = models.PositiveSmallIntegerField(choices=HISTORY_CONDITION)

    date = models.DateTimeField(auto_now_add=True)

    borrower = models.ForeignKey(User)

    # Owner can be infered through the item
    item = models.ForeignKey(Item)

    def __unicode__(self):
        return "%s %s %s on %s : %s Condition" % (
            self.borrower.first_name,
            self.get_action_display(),
            self.item.name,
            self.date.strftime("%a %B %d, %Y - %I:%M%p"),
            self.get_condition_display(),
        )
