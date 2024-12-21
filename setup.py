from setuptools import setup, find_packages

setup(
    name="resume-analyzer",
    version="0.1.0",
    description="A Python package to extract key information from resumes.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/resume-analyzer",  # Replace with your repository URL
    packages=find_packages(),
    install_requires=[
        "pdfminer.six",
        "nltk",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
