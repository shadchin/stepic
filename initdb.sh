mysql -uroot -e "DROP DATABASE ask;"
mysql -uroot -e "CREATE DATABASE ask;"
mysql -uroot -e "GRANT ALL ON ask.* TO 'root'@'localhost';"
