#!/bin/bash
chmod +x ./containerComparisionCollector.sh
bash ./containerComparisionCollector.sh
for i in {1..30}; 
do
  echo "fazendo o loop numero $i" 
  docker container run puppeteer-robot:latest
  sleep 5
done
killall containerComparisionCollector.sh