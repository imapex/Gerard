
#Create and name the container on your local system
sudo docker run -d -p 4040 --name gerard brbester/gerard:dev 5000

#to stop
sudo docker stop gerard

#to restart later
sudo docker start gerard

#to view startup and logs
sudo docker logs gerard

#to expose port 4040 (ngrok localhost to monitor)
sudo docker port gerard 4040

#to copy at
sudo docker cp /app/at.txt gerard:/app/at.txt


#to connect to CLI on container
sudo docker exec -i -t gerard /bin/ash


#from gerard container CLI to start webhook receiver on port :5000
python ngrokwebhook.py
python receive.py


