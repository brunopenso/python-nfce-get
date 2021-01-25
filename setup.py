import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nfceget", # Replace with your own username
    version="1.0.5",
    author="Bruno Penso",
    description="Pacote para recuperar uma NFCE (nota fiscal consumidor eletronica) e transformar em json.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brunopenso/python-nfce-get",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
