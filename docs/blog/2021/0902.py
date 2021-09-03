import lino
lino.startup('lino_book.projects.apc.settings.demo')
from django.utils import translation
from lino.api.doctest import *
from django.db.models import Q

from django.db.models import Sum
from lino_xl.lib.ledger.choicelists import TradeTypes
from lino_xl.lib.vat.choicelists import VatRegimes, VatAreas
intracom_regimes = set([
    r for r in VatRegimes.get_list_items() if r.vat_area == VatAreas.eu])
ap = rt.models.ledger.AccountingPeriod.objects.get(ref="2014-02")
qs = rt.models.contacts.Partner.objects.all()
qs = qs.filter(vat_id__isnull=False)
# qs = qs.exclude(vat_id__startswith="BE")
qs = qs.order_by('vat_id')
qs = qs.annotate(vataccountinvoice_base=Sum('vat_vataccountinvoice_set_by_partner__total_base'))
flt1 = Q(
    vat_vataccountinvoice_set_by_partner__journal__trade_type=TradeTypes.sales,
    vat_vataccountinvoice_set_by_partner__accounting_period=ap,
    vat_vataccountinvoice_set_by_partner__vat_regime__in=intracom_regimes,
    vataccountinvoice_base__gte=0)
if dd.is_installed("sales"):
    qs = qs.annotate(vatproductinvoice_base=Sum('sales_vatproductinvoice_set_by_partner__total_base'))
    flt2 = Q(
        sales_vatproductinvoice_set_by_partner__journal__trade_type=TradeTypes.sales,
        sales_vatproductinvoice_set_by_partner__accounting_period=ap,
        sales_vatproductinvoice_set_by_partner__vat_regime__in=intracom_regimes,
        vatproductinvoice_base__gte=0)
    qs = qs.filter(flt1 | flt2)
else:
    qs = qs.filter(flt1)
qs = qs.distinct()

for p in qs:
    print(p, p.vat_id, p.vatproductinvoice_base)
    # print(p, p.vat_id, p.vatproductinvoice_base, p.vataccountinvoice_base)
