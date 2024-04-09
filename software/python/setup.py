from setuptools import setup, find_packages

# Define package metadata
setup(
    name='my_package',  # Name of your package
    version='1.0.0',  # Version number
    author='Your Name',  # Your name
    author_email='your@email.com',  # Your email address
    description='A short description of your package',  # Short description
    long_description='A longer description of your package',  # Long description
    long_description_content_type='text/markdown',  # Type of long description
    url='https://github.com/yourusername/my_package',  # URL of your package's repository
    packages=find_packages(),  # Find all Python packages in the current directory
    classifiers=[  # Classifiers indicating metadata about your package
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.8',  # Minimum Python version required
    install_requires=[  # List of dependencies required by your package
        'numpy>=1.19.5',
        'pandas>=1.3.3',
        'matplotlib>=3.4.3',
    ],
)
