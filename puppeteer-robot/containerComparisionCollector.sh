#!/bin/bash
docker stats --no-stream | awk 'NR==1' > ./stats.csv
while true 
do
    docker stats --no-stream | awk 'NR==2' >> ./stats.csv
    sleep 1
done