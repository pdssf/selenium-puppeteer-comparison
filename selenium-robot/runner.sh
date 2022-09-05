#!/bin/bash
chmod +x ./containerComparisionCollector.sh
./containerComparisionCollector.sh &
for i in {1..30}; 
do
  echo "fazendo o loop numero $i" 
  docker container run selenium-robot:latest
  sleep 5
done
killall containerComparisionCollector.sh