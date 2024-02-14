from appy.pod.renderer import Renderer

tpl = 'test.odt'
context = {'commercial': 'open source'}
target = 'tmp.odt'
Renderer(tpl, context, target).run()
