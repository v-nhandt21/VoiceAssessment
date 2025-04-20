# Update domain in App.tsx

nvm use 18
npm run build

sudo scp -r build /var/www/voice-assessment/frontend
sudo systemctl restart nginx