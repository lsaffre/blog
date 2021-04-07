from setuptools import setup
SETUP_INFO = dict()
SETUP_INFO.update(test_suite='tests')
SETUP_INFO.update(url='https://luc.lino-framework.org')
if __name__ == '__main__':
    setup(**SETUP_INFO)
