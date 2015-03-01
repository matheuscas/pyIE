# *-* coding:utf-8 *-*

from setuptools import setup

setup(name='ie',
      version='1.0.8',
      description='Validation of brazilian state registration numbers',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='inscrição estadual inscricao estadual inscricoes estaduais inscrições estaduais validacao validação',
      url='https://github.com/matheuscas/pyIE',
      author='Matheus Cardoso',
      author_email='matheus.mcas@gmail.com',
      license='MIT',
      packages=['ie'],
          test_suite='nose.collector',
          tests_require=['nose'],
      zip_safe=False)