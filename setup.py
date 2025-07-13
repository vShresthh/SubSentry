from setuptools import setup, find_packages

setup(
    name="SubSentry",
    version="1.0.0",
    description="A subdomain takeover scanner + validator",
    author="Shresth",
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.0',
        'dnspython>=2.1.0',
        'pyfiglet>=1.0.2' 
    ],
    extras_require={ 
        'dev': [ 
            'pytest>=6.2.4',  
            'black>=21.9b0',  
            'flake8>=3.9.2',  
        ],
    },
    classifiers=[  
        'Programming Language :: Python :: 3',  
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent', 
    ],
    python_requires='>=3.6',  
)
