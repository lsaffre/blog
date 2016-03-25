from atelier.tasks import ns, setup_from_tasks

setup_from_tasks(globals())

cfg = dict()
cfg.update(tolerate_sphinx_warnings = True)
cfg.update(blog_root='/home/luc/work/blog/')
cfg.update(languages = ['en'])
cfg.update(revision_control_system = 'git')


# env.blogger_project = None  # override 'lino' set in `~/.fabricrc`
# env.blogger_url = 'http://luc.lino-framework.org'
# env.languages = ['en']
# env.blog_root = env.root_dir.child('docs')
# env.tolerate_sphinx_warnings = True

# env.use_dirhtml = True

# env.revision_control_system = 'git'

ns.configure(cfg)
