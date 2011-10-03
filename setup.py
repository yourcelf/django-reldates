from distutils.core import setup

setup(
    name='django-reldates',
    version='0.1',
    description='Self-updating smart "time since" dates for django templates',
    author='Charlie DeTar',
    author_email='cfd@media.mit.edu',
    license='MIT',
    url='http://github.com/yourcelf/django-reldates/',
    keywords = ['django', 'templates', 'date', 'format'],
    packages=[
        'reldates',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
