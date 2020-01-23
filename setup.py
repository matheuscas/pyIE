# *-* coding:utf-8 *-*

from setuptools import setup

setup(name='ie',
      version='2.0.0',
      description='Validation of brazilian state registration numbers',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.7',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='inscrição estadual inscricao estadual inscricoes estaduais inscrições estaduais validacao validação',
      url='https://github.com/matheuscas/pyIE',
      author='Matheus Cardoso',
      author_email='matheus.mcas@gmail.com',
      license='MIT',
      packages=['ie'],
          tests_require=['tox'],
      zip_safe=False)