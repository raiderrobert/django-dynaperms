from setuptools import setup

setup(
    name='django-dynamic-permissions',
    py_modules=['dynamic_permissions'],
    version='0.1.0',
    description='Check complex logic with has_perm.',
    license='MIT',
    url='https://github.com/raiderrobert/django-dynamic-permissions',
    author='Robert Roskam',
    author_email='raiderrobert@gmail.com',
    install_requires=['django>=1.11'],
    keywords='django urls',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)