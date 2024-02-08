import requests, datetime, pymongo, re, logging, json,graypy, sys
from config import DB_USERNAME, DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DATE_FORMAT, SUPER_API_KEY, META_BRAND_LIST, INSTA_PAGE_DATA, INSTA_PAGE_POST_DATA

#enable Logging
# my_logger = logging.getLogger('IG II CRON')
# my_logger.setLevel(logging.INFO)

logging.basicConfig(filename="ig_new.log", format='%(levelname)s:: %(asctime)s - %(message)s', level=logging.INFO)
# handler = graypy.GELFUDPHandler('216.48.185.47', 12201)
# handler.setLevel(logging.INFO)
# # create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# # add formatter to ch
# handler.setFormatter(formatter)
# my_logger.addHandler(handler)

logging.info(f"Insta Script Execution Started")

myclient = pymongo.MongoClient(f"mongodb://{DB_HOST}:{DB_PORT}/",username=DB_USERNAME,password=DB_PASSWORD)

current_date = datetime.datetime.today().strftime(DATE_FORMAT)
api_date = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime(DATE_FORMAT)

start_date = api_date
end_date = api_date

try:
    mydb = myclient[DB_NAME] #databasename
    # fb_page_data = mydb["instagram_page_data"] #collectionname
    insta_page_data = mydb[INSTA_PAGE_DATA] #collectionname
    insta_page_post_data = mydb[INSTA_PAGE_POST_DATA] #collectionname

    # col = mydb["brand_list"]
    col = mydb[META_BRAND_LIST]
    where = {'fetch':True}
    project = {'_id': 1, 'Brand': 1, 'Instagram': 1}
    data = col.find(where, project)
except Exception as e:
    print("No record found!")
    logging.error("Insta No record found!")
    sys.exit()

instagram_profiles = []
for line in data:
    url = line.get('Instagram') or None
    if url:
        username = None
        url = line['Instagram']
        url_parts = url.split('/')
        username = url_parts[3]
        
        if username.find('?') > -1:
            if username.find('profile.php') > -1:
                username = re.sub(r"\D","", username)
            elif username.find('share.php') > -1:
                username = None
                logging.warning(f"Profile URL Empty :: Brand: {line['Brand']} :: URL: {line['Instagram']}")
            else:
                username = username.split('?')[0]
        
        if username:
            each_profile = {'username': username, 'link': line['Instagram'], '_id': line['_id']}
            instagram_profiles.append(each_profile)

    else:
        logging.warning(f"Profile URL Empty :: Brand: {line['Brand']} :: URL: {url}")

#Remove Duplicate Username
instagram_profiles = { x['username']:x for x in instagram_profiles }.values()

for each_fb_profile in instagram_profiles:
    username = each_fb_profile['username']
    link = each_fb_profile['link']
    brand_id = each_fb_profile['_id']
    
    #Page Data Request
    
    page_data_json_config = {
        "ds_id": "IGPD2",
        "ds_accounts": username,
        "ds_user": "473260313847019",
        "start_date":"2023-11-25",
        "end_date":"2023-11-30",
        "fields": "today,dataSourceName,ig_id,username,name,biography,profile_picture_url,website,followers,follows,total_post_count",
        "settings": { "report_type": "BusinessDiscoveryAccount", "timezone":"Asia/Dubai" },
        "max_rows": 100000,
        "api_key": SUPER_API_KEY
    }
    
    page_data_url = 'https://api.supermetrics.com/enterprise/v2/query/data/json?json=' + json.dumps(page_data_json_config)
    response = requests.get(page_data_url, timeout=600)
    
    if response.status_code == 200:
        data = response.json()
        print('=======.........=======', data)
        exit()
        
        if data['data']:
            keys = data['data'][0]
            del data['data'][0]
            
            keys = [x.lower().replace(' ','_').replace('(','').replace(')','').replace(':','') for x in keys]

            final_data = []
            total_data =  {
                "likes_per_post": 0,
                "comments_per_post": 0,
                "comments": 0,
                "likes": 0,
                "total_posts": 0
            }
            
            for each_data in data['data']:
                temp = dict(zip(keys, each_data))
                temp['brand_id'] = brand_id
                temp['date'] = api_date
                temp['created_at'] = datetime.datetime.now()
                temp['modified_at'] = datetime.datetime.now()
                temp['post_totals'] = total_data
                
                final_data.append(temp)
            
            #Insert Data in Mongo
            insta_page_data.insert_many(final_data)

        else:
            logging.warning(f"Page Repose Empty from Supermetrics :: username: {username} :: Facebook Link: {link} :: SuperMetric URL: {page_data_url}")
    else:
        logging.error(f"Page Repose Error from Supermetrics :: username: {username} :: Facebook Link: {link} :: SuperMetric URL: {page_data_url} :: Reponse Code: {response.status_code} :: Reponse: {response.text}")
        
    #Page Post Data
    page_post_data_json_config = {
        "ds_id": "IGPD2",
        "ds_accounts": username,
        "ds_user": "473260313847019",
        "start_date":"2023-09-01",
        "end_date":"2023-11-30",
        "fields": "dataSourceName,post_id,post_timestamp,post_type,post_media_url,post_permalink,post_caption,ig_id,username,name,biography,profile_picture_url,website,year,yearOfWeek,yearOfWeekIso,yearMonth,month,yearWeek,yearWeekIso,week,weekIso,dayOfMonth,dayOfWeekName,dayOfWeekNameIso,date,today,likes_per_post,comments_per_post,posts,post_comments,post_likes",
        "settings": {
            "report_type": "BusinessDiscoveryMedia", "timezone":"Asia/Dubai"
        },
        "max_rows": 1000,
        "api_key": SUPER_API_KEY
    }
    
    page_data_url = 'https://api.supermetrics.com/enterprise/v2/query/data/json?json=' + json.dumps(page_post_data_json_config)

    response = requests.get(page_data_url, timeout=600)

    if response.status_code == 200:
        data = response.json()
        
        if data['data']:
            keys = data['data'][0]
            del data['data'][0]
            
            keys = [x.lower().replace(' ','_').replace('&','and').replace('-','_').replace('(','').replace(')','').replace(':','') for x in keys]

            final_data = []
            
            total_data = {
                "likes_per_post": 0,
                "comments_per_post": 0,
                "comments": 0,
                "likes": 0
            }
            
            for each_data in data['data']:
                temp = dict(zip(keys, each_data))
                temp['brand_id'] = brand_id
                temp['date'] = api_date
                temp['created_at'] = datetime.datetime.now()
                temp['modified_at'] = datetime.datetime.now()
                for key in total_data:
                    total_data[key] = total_data[key] + (temp[key] or 0)
                
                final_data.append(temp)
            
            total_data['total_posts'] = len(final_data)
                
            #Inserting Data in Mongo
            insta_page_post_data.insert_many(final_data)
            
            #update Main Collection Data to include total_counts
            insta_query = { "brand_id": brand_id, "date": api_date }
            total_data_key = { "$set": { "post_totals": total_data } }
            insta_page_data.update_one(insta_query, total_data_key)
            
        else:
            logging.warning(f"Page Post Repose Empty from Supermetrics :: username: {username} :: Instagram Link: {link} :: SuperMetric URL: {page_data_url}")
    else:
        logging.error(f"Page Post Repose Error from Supermetrics :: username: {username} :: Instagram Link: {link} :: SuperMetric URL: {page_data_url} :: Reponse Code: {response.status_code} :: Reponse: {response.text}")
        
logging.info(f"Insta Script Execution Ended")
