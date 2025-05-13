from setuptools import setup, find_packages

# Define the setup configuration
setup(
    name="SubSentry",  # The name of your tool
    version="1.0.0",  # Tool version
    description="A subdomain takeover scanner",  # Short description
    author="Shresth",  # Replace with your actual name
    packages=find_packages(),  # Automatically finds all the packages in the project
    install_requires=[  # External dependencies
        'requests>=2.25.0',  # For making HTTP requests
        'dnspython>=2.1.0',  # For DNS querying
    ],
    extras_require={  # Optional extra dependencies
        'dev': [  # For development purposes
            'pytest>=6.2.4',  # Testing framework
            'black>=21.9b0',  # Code formatting tool
            'flake8>=3.9.2',  # Linting tool
        ],
    },
    classifiers=[  # Metadata classifiers for your package
        'Programming Language :: Python :: 3',  # Python version compatibility
        'License :: OSI Approved :: MIT License',  # License type (MIT in this case)
        'Operating System :: OS Independent',  # OS compatibility
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
