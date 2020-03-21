import sys
from setuptools import setup, find_packages
from umr_telegram_driver.__VERSION__ import __VERSION__

if sys.version_info < (3, 7):
    raise Exception("Python 3.7 or higher is required. Your version is %s." % sys.version)

long_description = open('README.md', encoding="utf-8").read()

setup(
    name='umr_telegram_driver',
    packages=find_packages(include=['umr_telegram_driver', 'umr_telegram_driver.*']),
    version=__VERSION__,
    description='UMR Telegram Driver',
    long_description=long_description,
    author='Curtis Jiang',
    url='https://github.com/jqqqqqqqqqq/UnifiedMessageRelay',
    license='MIT',
    python_requires='>=3.7',
    include_package_data=True,
    zip_safe=False,
    keywords=['UMR', 'UnifiedMessageRelay', 'Group chat relay', 'IM', 'messaging', 'Telegram'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Typing :: Typed"
    ],
    install_requires=[
        'aiogram',
        'unified-message-relay',
        'janus'
    ],
    project_urls={
        "Telegram Chat": "https://t.me/s/UnifiedMessageRelayDev",
    }
)
