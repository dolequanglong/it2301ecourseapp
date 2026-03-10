import pymysql
import sys

# Giả lập module MySQLdb bằng pymysql
pymysql.version_info = (2, 2, 1, 'final', 0) # Đánh lừa Django rằng đây là bản 2.2.1
pymysql.install_as_MySQLdb()