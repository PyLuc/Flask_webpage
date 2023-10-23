A simple resume template based on Flask and Docker.\

To fill the folder with certificates run the command 
$docker compose run --rm  certbot certonly --webroot --webroot-path /var/www/certbot/ -d <domain>
