from setuptools import setup, find_packages

setup(
    name = "shutil_extra",
    version = "0.0.1",
    keywords = ("pip", "shutil extra", "dir tree"),
    description = "A successful sign for python setup",
    long_description_content_type = 'text/markdown',
    long_description = open('README.md', encoding='UTF8').read(),
    license = "MIT Licence",
    url = "http://python4office.cn/upload-pip/",
    author = "novawei",
    author_email = "913252732@qq.com",
    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = [],
)