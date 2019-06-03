container: Dockerfile
	cp ../binaries/multiserver ./
	sudo docker build -t server .

run: container
	#sudo docker run -d -e PORT=1600 -p 1600:1600 --net=host multi_server 
	sudo docker run -d -t -e PORT=1700 -p 1700:1700 --net=bridge server 
