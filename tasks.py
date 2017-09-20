from atelier.invlib.ns import ns
ns.setup_from_tasks(globals())

cfg = dict()
cfg.update(tolerate_sphinx_warnings=False)
cfg.update(blog_root='/home/luc/work/blog/')
cfg.update(languages=['en'])
cfg.update(revision_control_system='git')

ns.configure(cfg)
