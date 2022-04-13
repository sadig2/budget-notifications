

from uuid import uuid4

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class T_Shop(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=255, null=False)
    online = models.BooleanField(default=False)


class T_Budget(models.Model):
    shop_id = models.ForeignKey('T_Shop', on_delete=models.CASCADE)
    month = models.DateTimeField()
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_spent = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = (("shop_id", "month"),)


# constructor to save initial state of amounts, to decide whether to send notification again or not 
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.notification_50 = True if self.budget_amount > self.amount_spent >= self.budget_amount//2  else False
        self.notification_100 = True if self.budget_amount <= self.amount_spent else False


    # set status on edit of budget
    def save(self) -> None:
        shop = self.shop_id
        if self.amount_spent > self.budget_amount:
            shop.online = False
        else:
            shop.online = True
        shop.save()
        return super().save()


# signal for notifications
@receiver(post_save, sender = T_Budget)
def post_notify(sender, instance, *args, **kwargs):
    budget = instance.budget_amount
    spent = instance.amount_spent
    if  budget > spent >= budget//2 and not instance.notification_50:
        print(f'{instance.shop_id.name} shop exceeded 50 percent')
    if budget <= spent and not instance.notification_100:
        print(f'{instance.shop_id.name} shop exceeded 100 percent and will go offline')

