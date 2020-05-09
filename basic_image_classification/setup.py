import setuptools

setuptools.setup(
    name="basic_image_classification",
    version="0.0.1",
    author="Kristian Nymann Jakobsen",
    author_email="kristian@nymann.dev",
    description="Basic image classification.",
    url="https://github.com/nymann/ai",
    packages=setuptools.find_packages(),
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["tensorflow", "matplotlib"],
    extras_require={
        'lint': [
            "pylint",
            "coverage"
        ]
    },
    entry_points={
        'console_scripts': [
            'bic=console_scripts.__main__:main',
            'bic-train=console_scripts.__main__:train',
            'bic-solve=console_scripts.__main__:solve',
        ]
    },
)