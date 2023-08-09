from setuptools import setup, find_packages
from setuptools.command.install import install
from generate_nodes_init_file import generate_nodes_import_statements

class CustomInstallCommand(install):
    def run(self):
        # Place your custom logic here
        # e.g., download additional resources, compile code, etc.
        generate_nodes_import_statements()
        install.run(self)


setup(
    name="flojoy_nodes",
    packages=find_packages(exclude=["tests"]),
    package_data={"flojoy_nodes": ["__init__.py", "*/**/*.py"]},
    version="0.0.1",
    license="MIT",
    description="Python client library for Flojoy nodes.",
    author="flojoy",
    author_email="jack.parmer@proton.me",
    url="https://github.com/flojoy-ai/nodes",
    download_url="https://github.com/flojoy-ai/nodes/archive/refs/heads/main.zip",
    cmdclass={"install": CustomInstallCommand},
    keywords=[
        "data-acquisition",
        "lab-automation",
        "low-code",
        "python",
        "scheduler",
        "topic",
    ],
    python_requires=">=3.10",
    install_requires=[
        "flojoy",
        "numpy",
        "scipy",
        "pandas",
        "pytest",
        "plotly==5.8.2",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)
