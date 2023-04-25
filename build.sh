cd api/
docker build -t budgetbot-api:latest .
cd ../discord_bot/
docker build -t budgetbot-discordbot:latest .