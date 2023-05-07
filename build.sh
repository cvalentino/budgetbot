# Update requirements.txt for modules
pipreqs --force --mode no-pin --savepath ./discord_bot/requirements.txt ./discord_bot
pipreqs --force --mode no-pin --savepath ./api/requirements.txt ./api/flask_app

# Manual requirements.txt additions
echo "gunicorn" >> ./api/requirements.txt

# build docker images
cd api/
docker build -t budgetbot-api:latest .
cd ../discord_bot/
docker build -t budgetbot-discordbot:latest .

# sync with registry
docker tag budgetbot-api:latest registry.digitalocean.com/cvalentino/budgetbot-api:latest
docker push registry.digitalocean.com/cvalentino/budgetbot-api:latest
docker tag budgetbot-discordbot:latest registry.digitalocean.com/cvalentino/budgetbot-discordbot:latest
docker push registry.digitalocean.com/cvalentino/budgetbot-discordbot:latest