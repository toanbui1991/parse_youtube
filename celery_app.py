from celery import Celery
from config import config


#setting
broker_url = config.get('celery_app').get('broker_url')
backend_url = config.get('celery_app').get('backend_url')
app = Celery('celery_app', broker=broker_url, backend=backend_url)

@app.task
def add(x, y):
    return x + y

@app.task
def scraper(url):
    import time, re, os
    import pandas as pd
    from selenium.webdriver import Chrome, ChromeOptions
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from bs4 import BeautifulSoup

    #setting
    # curdir = os.getcwd()
    # driver_path = 'C:/Users/buixu/Toan/python_projects/parse_youtube/chromedriver.exe'
    # driver_path = curdir + driver_path

    target_link = url
    options = ChromeOptions()
    options.add_argument('--lang=ko-KR')
    options.add_argument("--no-sandbox")
    # options.add_argument("--headless")
    driver = Chrome(options=options)

    wait = WebDriverWait(driver,15)
    driver.get(target_link)

    #wait for page to load with tag body and roll down to load comments counts
    for _ in range(3):
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(5)
    #find number of comments in the video
    num_comments = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'h2#count yt-formatted-string span')))
    num_comments = num_comments[1]
    num_comments = int(num_comments.text)
    com_per_load = 20
    num_loads = round(num_comments / com_per_load) + 1
    print('num_loads: {}'.format(num_loads))

    #load all comments base on num_loads
    for item in range(num_loads): 
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(5)
    page_source = driver.page_source
    driver.close()


    #parse rendered page_source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')
    title =  soup.select_one('h1.title.style-scope.ytd-video-primary-info-renderer yt-formatted-string')
    comments = soup.select('div.style-scope.ytd-comment-renderer#body')

    data = []
    for comment in comments:
        item = {}
        item['target_link'] = target_link
        item['title'] = title.get_text()
        item['user_id'] = comment.select_one('a.yt-simple-endpoint.style-scope.ytd-comment-renderer').get('href')
        item['user_name'] = comment.select_one('span.style-scope.ytd-comment-renderer').get_text()
        item['comment'] = comment.select_one('div.style-scope.ytd-expander#content').get_text()
        data.append(item)

    data = pd.DataFrame(data)
    url_id = re.search(r'(watch\?v=)(\w+)', url).group(2)
    data.to_csv('./data/comments_{}.csv'.format(url_id))