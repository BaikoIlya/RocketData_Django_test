from decimal import Decimal
from random import randrange

from sales_structure.celery import app

from .models import SaleObject


@app.task
def beat_debt_rise():
    for sale_object in SaleObject.objects.all():
        if sale_object.parent:
            sale_object.debt += Decimal(randrange(5, 501))
            sale_object.save()


@app.task
def beat_debt_decrease():
    """
    Будем считать что предоплата не возможна, поэтому Задолженность
    не может быть отрицательной.
    """
    for sale_object in SaleObject.objects.all():
        if sale_object.parent:
            if Decimal(randrange(100, 10001)) > sale_object.debt:
                sale_object.debt = Decimal(0)
            else:
                sale_object.debt -= Decimal(randrange(100, 10001))
            sale_object.save()
