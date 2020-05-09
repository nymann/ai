import setuptools

setuptools.setup(
    name="simple_neural_net",
    version="0.0.1",
    author="Kristian Nymann Jakobsen",
    author_email="kristian@nymann.dev",
    description="simple neural network.",
    url="https://github.com/nymann/ai",
    packages=setuptools.find_packages(),
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    extras_require={
        'lint': [
            "pylint",
            "coverage"
        ]
    },
    entry_points={
        'console_scripts': [
            'snn=console_scripts.__main__:main',
            'snn-train=console_scripts.__main__:train',
            'snn-solve=console_scripts.__main__:solve',
        ]
    },
)