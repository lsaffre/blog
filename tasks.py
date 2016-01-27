from atelier.tasks import *
env.setup_from_tasks(globals())

env.blogger_project = None  # override 'lino' set in `~/.fabricrc`
env.blogger_url = 'http://luc.lino-framework.org'
env.languages = ['en']
env.blog_root = env.root_dir.child('docs')
env.tolerate_sphinx_warnings = True

# env.use_dirhtml = True

env.revision_control_system = 'git'
