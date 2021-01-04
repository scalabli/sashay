from setuptools import setup

setup(
    name="Sashay",
    version='2.5.7dev',
    description="An all in one automatic tool installer.",
    long_description="Coming soon!.",
    author="Gerrishon Sirere.",
    author_email="gerryshon254@gmail.com",
    url="https://github.com/chouette254/Sashay",
    license="GPLv3+",
    py_modules=['Sashay'],
    install_requires=[
        'Click',
        'pygit2==0.24'
    ],
    entry_points='''
        [console_scripts]
        gitcen=gitcen:main
    ''',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.6'
    )
)
