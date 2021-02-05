from distutils.core import setup


setup(
  name = 'akmath',        
  packages = ['akmath'],   
  version = '1.0',      
  license='MIT',        :      https://help.github.com/articles/licensing-a-repository
description = 'liabrary to check Armgstrong,prime,palindrome numbera and palindrome String',   
  author = 'Abhijeet Khatri',                   
  author_email = 'abhijeetkhatri@gmail.com',      
  url = 'https://github.com/user/reponame',   
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    
  keywords = ['math', 'armgstrong', 'palindrome','prime'],   
  install_requires=[            
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)