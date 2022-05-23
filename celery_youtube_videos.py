"""
This script will loop through list of video_id and send web scraping task to workder
"""
from celery_app import scraper
import time



if __name__ == '__main__':
    
    start = time.time()
    target_urls = [
    'https://www.youtube.com/watch?v=_wlTizkaQx8',
    'https://www.youtube.com/watch?v=3WxTe01PQ3M',
    'https://www.youtube.com/watch?v=NldaLEUrIlM',
    'https://www.youtube.com/watch?v=Xm-Olrg8mfg'
    'https://www.youtube.com/watch?v=FF-vEV2F8LU',
    'https://www.youtube.com/watch?v=BCrqKq5S1as'
    'https://www.youtube.com/watch?v=f48xVaxzG2k',
    'https://www.youtube.com/watch?v=ajp9Kk4i8y0',
    'https://www.youtube.com/watch?v=BbHBYn4AGu4',
    'https://www.youtube.com/watch?v=mFZpRVl3cU0'
    ]
    for url in target_urls:
        scraper.delay(url)
    end = time.time()
    period = end - start
    print('time to finish all tasks: {}'.format(period))