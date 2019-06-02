from setuptools import setup, find_packages

setup(
    name='fragprots',
    packages=find_packages(),
    version='0.0.1',
    description='In-silico protein fragmentation.',
    long_description='This script modularizes the bioinformatic task of generating some typical fragments for a given molecule..',
    author=u'Mateusz Krzysztof Łącki',
    author_email='matteo.lacki@gmail.com',
    url='https://github.com/MatteoLacki/fragprots',
    # download_url='https://github.com/MatteoLacki/MassTodonPy/tree/GutenTag',
    keywords=[
        'Proteomics',
        'Mass Spectrometry',
        'Fragmenting Proteins'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'],
    install_requires=[
        # 'numpy',
        # 'matplotlib'
    ],
    extras_require={
        # 'dev': ['ipython', 'sklearn', 'statsmodels']
    }
    # include_package_data=True,
    # package_data={
    #     'data': 'data/annotated_data.csv'
    # }
    # scripts=[
    #     'bin/rta']
)
