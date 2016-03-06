mysql -uroot -e "CREATE DATABASE ask;"
mysql -uroot -e "CREATE USER 'root'@'localhost' IDENTIFIED BY '';"
mysql -uroot -e "GRANT ALL ON ask.* TO 'root'@'localhost';"
