#!/usr/bin/env python3

"""
simple flask based blog
docker and python play :)
"""

__author__ = "Piotr Szczepanski"
__version__ = "0.1.0"
__license__ = "MIT"


from piotr_flask_blog import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
