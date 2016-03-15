from lino import startup
startup('lino_welfare.projects.std.settings.demo')
from django.conf import settings
settings.SITE.appy_params.update(raiseOnError=True)
from lino.api import rt
Excerpt = rt.modules.excerpts.Excerpt
ses = rt.login('robin')
# qs = Excerpt.objects.filter(build_time__isnull=True)
qs = Excerpt.objects.all()
# for obj in qs:
if True:
    obj = Excerpt.objects.get(pk=4)
    print "Gonna print #", obj.pk
    ses.run(obj.do_clear_cache)
    # dd.logger.info("20150526 rendering %s", obj)
    rv = ses.run(obj.do_print)
    print(rv)


