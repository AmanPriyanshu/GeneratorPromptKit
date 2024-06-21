from setuptools import setup, find_packages

setup(
    name='generator-prompt-kit',
    version='1.0.0',
    packages=find_packages(),
    description='A Python Library for Automated Generator Prompting and Dataset Generation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/AmanPriyanshu/GeneratorPromptKit',
    author='Aman Priyanshu and Supriti Vijay',
    author_email='amanpriyanshusms2001@gmail.com',
    license='MIT',
    install_requires=[
        'numpy==2.0.0',
        'openai==1.34.0',
        'pandas==2.2.2',
        'tqdm==4.66.4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='llm llms llm-training dataset-generation automated-prompt-engineering prompt-engineering diverse-data data-science data dataset synthetic-dataset-generation synthetic-data augmentation data-augmentation',
)
