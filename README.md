# Twitter Mentions Retriever
Collects FlixBus mentions using Twitter API.


## Prerequisites
* Unix-like OS (like MacOs or Linux)
* Python3.8+


## Running Service Locally
Use terminal to run commands below
* Clone repository by running `git clone https://github.com/vladbagmet/twitter-mentions-collector.git`
* Go to the cloned repository by running `twitter-mentions-collector`
* Create Python virtual environment `python3.8 -m venv ~/.virtualenvs/twitter-mentions-collector`
* Activate virtual environment `source ~/.virtualenvs/twitter-mentions-collector/bin/activate`
* Install external dependencies `pip install -r requirements.txt`
* Set all environment variables in the list below by running commands like `export AWS_REGION_NAME=us-east-1`
  * AWS_REGION_NAME 
  * AWS_ACCESS_KEY_ID 
  * AWS_SECRET_ACCESS_KEY 
  * BUCKET_NAME 
  * DYNAMODB_TABLE_NAME
  * TWITTER_API_BEARER_TOKEN 
* Run etl job by executing a command `python collect_mentions_etl.py`


## Running ETL Orchestration UI
* Run etl orchestration service using command `prefect orion start`
* Open `http://127.0.0.1:4200 ` in the browser
![prefect-orion-ui]([https://user-images.githubusercontent.com/23407924/150556107-98ccc01b-5c13-4293-9c4b-4ed394a71247.gif](https://user-images.githubusercontent.com/23407924/186283036-a05ce655-6cd4-4ff4-bab0-f567c2a778c4.png))
