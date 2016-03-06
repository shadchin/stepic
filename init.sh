if [ -f /etc/nginx/sites-enabled/default ]
then
sudo rm  /etc/nginx/sites-enabled/default
fi
if [ ! -f /etc/nginx/sites-enabled/test.conf ]
then
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
fi
sudo /etc/init.d/nginx restart

if [ ! -f /etc/gunicorn.d/test ]
then
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/ask
fi
sudo /etc/init.d/gunicorn restart
