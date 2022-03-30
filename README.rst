=====================================
make Github pages blog with Pelican
=====================================


usage
=================================

.. code:: sh

   $ pip install --user pelican ghp-import

pipでインストールしたpelicanコマンドのパスを通すために

.. code:: sh

   $ vim .zshenv
   export PATH=$PATH:~/.local/bin

.. code:: sh

   $ mkdir i0z0m.github.io
   $ cd i0z0m.github.io
   $ pelican-quickstart
   $ vim content/pages/about.rst
   $ pelican

theme
=================================

.. code:: sh

   $ git clone https://github.com/laughk/pelican-hss.git
   $ mv pelican-hss pelican-hss-theme
   $ vim pelican-hss-theme/templates/base.html
   hoge.slugをslug=hoge.slugに直す
   $ pelican-themes -i pelican-hss-theme
   $ vim pelicanconf.py
   THEME = “pelican-hss-theme”
   # Uncomment following line if you want document-relative URLs when developing
   #RELATIVE_URLS = True

add favicon

.. code:: python

   FAVICON = 'favicon.ico'
   STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
   EXTRA_PATH_METADATA = {
       'extra/robots.txt': {'path': 'robots.txt'},
       'extra/favicon.ico': {'path': 'favicon.ico'}
   }


host
=================================

.. code:: sh

   $ git init
   $ vim .gitignore
   $ git add *
   $ git commit -m “first commit”

githubでi0z0m.github.ioという名前のリポジトリを作る．
ghp-importを使い，outputディレクトリだけをホスティングする．

.. code:: sh

   $ git remote add origin https://github.com/i0z0m/i0z0m.github.io.git
   $ ghp-import -n -m "コメント" output
   $ git push origin gh-pages:master
