from setuptools import setup, find_packages

setup(
    name="aiu-staff/base",  # Название вашего модуля
    version="0.1.4",  # Версия
    packages=find_packages(),  # Автоматически находит все пакеты
    install_requires=[  # Зависимости, если они есть

    ],
    url="https://github.com/aiu-staff/base.git",  # URL вашего репозитория
    author="pauchai",
    author_email="paul.khimyack@gmail.com",
    description="file downloader ",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
