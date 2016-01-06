from setuptools import setup, find_packages

setup(
    name='tunobase-core',
    version='1.1.31',
    description='Unomena Base Django Application',
    long_description=open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read(),
    author='Unomena',
    author_email='dev@unomena.com',
    license='BSD',
    url='http://git.unomena.net/unomena/tunobase',
    packages=find_packages(),
    dependency_links=[
        'http://github.com/unomena/django-photologue/tarball/2.8.praekelt#egg=django-photologue-2.8.praekelt',
        'http://github.com/unomena/django-redactor/tarball/0.0.2#egg=redactor-0.0.2',
    ],
    install_requires=[
        'South',
        'redactor==0.0.2',
        'django-photologue==2.8.praekelt',
        'django-preferences',
        'python-memcached',
        'celery>=3.1.19',
        'django-celery>=3.1.17',
        'django-honeypot',
        'Pillow',
        'google-api-python-client==1.2',
        'flufl.password==1.2.1',
        'requests>=2.7.0',
        'unidecode',
    ],
    tests_require=[
        'django-setuptest>=0.1.2',
        'pysqlite>=2.5',
        'pycurl'
    ],
    test_suite="setuptest.setuptest.SetupTestSuite",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
