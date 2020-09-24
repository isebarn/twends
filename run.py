import argparse
import twitter
from ORM import Operations
import sys
from datetime import datetime
from pprint import pprint
import requests
import os
sys.path.append(".")


consumer_key =  os.environ.get('CONSUMER_KEY')
consumer_secret =  os.environ.get('CONSUMER_SECRET')
access_key =  os.environ.get('ACCESS_KEY')
access_secret =  os.environ.get('ACCESS_SECRET')


api = twitter.Api(access_token_key=access_key,
                  access_token_secret=access_secret,
                  consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  sleep_on_rate_limit=True)


def args():
  parser = argparse.ArgumentParser(description='Fetch twitter trends.')
  parser.add_argument('--count', default=10, type=int, help='Number of trends per place saved')
  return parser.parse_args()

if __name__ == '__main__':
  args = args()

  for location in Operations.QueryLocation():
    trends = api.GetTrendsWoeid(location.Id)
    data = {}
    data['location'] = location.Id
    data['time'] = datetime.now()
    data['trends'] = [
      {
      'place': idx,
      'value': value.__dict__['_json']['name'],
      'volume': value.__dict__['_json']['tweet_volume']
      }
      for idx, value in enumerate(trends[0:args.count])]

    Operations.SaveRun(data)
