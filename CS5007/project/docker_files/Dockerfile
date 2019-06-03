#Download base image ubuntu 18.04
FROM ubuntu:18.04

# Copy the test data into /opt/
COPY ./test_data/ /opt/test_data/

# Copy the server binary in
COPY ./multiserver /opt/

CMD ["sh", "-c", "/opt/multiserver /opt/test_data/ ${PORT}"]
