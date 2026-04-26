from pathlib import Path

from setuptools import find_packages, setup


README = Path(__file__).with_name("README.md").read_text(encoding="utf-8")


setup(
    name="ai_sop_toolkit",
    version="1.3.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "ai_sop_toolkit": ["templates/*.tpl", "templates/*.md"],
    },
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "ai-sop=ai_sop_toolkit.cli:main",
        ],
    },
    author="Wang Peiquan",
    description="A CLI toolkit for bootstrapping an AI Agent Team development SOP.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/perry121108-dotcom/fluffy-palm-tree.git",
    license="MIT",
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
)
