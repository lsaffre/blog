from unipath import Path

from lino.utils.pythontest import TestCase


class LinoTestCase(TestCase):
    django_settings_module = "lino.projects.docs.settings.demo"
    project_root = Path(__file__).parent.parent


class BlogTests(LinoTestCase):
    def test_all(self):
        self.run_simple_doctests("""
        docs/blog/2013/0316.rst
        docs/blog/2013/0507.rst
        # docs/blog/2013/0508.rst
        # docs/blog/2013/0513.rst
        # docs/blog/2013/0622.rst
        # docs/blog/2013/0714.rst
        docs/blog/2013/0716.rst
        # docs/blog/2013/0719.rst
        # docs/blog/2013/0807.rst
        # docs/blog/2013/0821.rst
        # docs/blog/2013/1210.rst
        docs/blog/2013/1211.rst
        docs/blog/2014/0108.rst
        docs/blog/2014/0605.rst
        docs/blog/2014/0902.rst
        """)

    def one(self):
        """
        this does not start with "test_" and is not called automatically.
        used to call explicitly a single case::

          $ python setup.py test -s tests.BlogTest.one

        """
        self.run_simple_doctests("""
        docs/blog/2014/0902.rst
        """)


