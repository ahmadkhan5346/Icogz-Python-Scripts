import requests, datetime, pymongo, re, logging, json
from config import DB_USERNAME,DB_HOST,DB_NAME,DB_PASSWORD,DB_PORT,DATE_FORMAT, FB_PAGE_DATA, FB_PAGE_POST_DATA, META_BRAND_LIST

#enable Logging
# my_logger = logging.getLogger('FB II CRON')
# my_logger.setLevel(logging.INFO)

# # logging.basicConfig(filename="platform_location.log", format='%(levelname)s:: %(asctime)s - %(message)s', level=logging.INFO)
# handler = graypy.GELFUDPHandler('216.48.185.47', 12201)
# handler.setLevel(logging.INFO)
# # create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# # add formatter to ch
# handler.setFormatter(formatter)
# my_logger.addHandler(handler)

# my_logger.info(f"FB Script Execution Started")
logging.basicConfig(filename="facebook_new.log", format='%(asctime)s :: %(levelname)s :: %(message)s', level=logging.INFO)


myclient = pymongo.MongoClient(f"mongodb://{DB_HOST}:{DB_PORT}/",username=DB_USERNAME,password=DB_PASSWORD)
# print("myclient--------------------", myclient)
logging.info("Mongo Connection Set")


current_date = datetime.datetime.today().strftime(DATE_FORMAT)
api_date = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime(DATE_FORMAT)

start_date = api_date
end_date = api_date
page_id_list = []
try:
    mydb = myclient[DB_NAME] #databasename
    # fb_page_data = mydb["facebook_page_data_20231010"] #collectionname
    fb_page_data = mydb[FB_PAGE_DATA] #collectionname
    # fb_page_post_data = mydb["facebook_page_post_data_20231010"] #collectionname
    fb_page_post_data = mydb[FB_PAGE_POST_DATA] #collectionname

    # col = mydb["brand_list"]
    col = mydb[META_BRAND_LIST]
    print(f"{col =}")
    data = col.find({'fetch': True},{'_id': 1, 'Brand': 1, 'Facebook': 1})
except Exception as e:
    print("No record found!")
    logging.error("FB No record found!")
    exit()

facebook_profiles = []
# print(f"{data =}")
for line in data:
    print('inside ', line)
    url = line.get('Facebook') or None 
    # print(f"{url =}")
    if url:
        username = None
        url = line['Facebook']
        url_parts = url.split('/')
        username = url_parts[3]
        
        if username.find('?') > -1:
            if username.find('profile.php') > -1:
                username = re.sub(r"\D","", username)
            elif username.find('share.php') > -1:
                username = None
                logging.warning(f"Profile URL Empty :: Brand: {line['Brand']} :: URL: {line['Facebook']}")
            else:
                username = username.split('?')[0]
        
        if username:
            each_profile = {'username': username, 'link': line['Facebook'], '_id': line['_id']}
            facebook_profiles.append(each_profile)

    else:
        logging.warning(f"Profile URL Empty :: Brand: {line['Brand']} :: URL: {url}")

#Remove Duplicate Username
facebook_profiles = { x['username']:x for x in facebook_profiles }.values()

# print(facebook_profiles)

for each_fb_profile in facebook_profiles:
    username = each_fb_profile['username']
    link = each_fb_profile['link']
    brand_id = each_fb_profile['_id']
    
    #Page Data Request
    page_data_json_config = {
        "ds_id": "FBPD",
        "ds_accounts": username,
        "ds_user": "amarjit@insitedigi.com",
        "start_date":"2023-09-01",
        "end_date":"2023-11-30",
        "fields": "username,name,category,description,general_info,about,company_overview,link,website,phone,page_id,awards,founded,products,mission,location_name,location_country,location_country_code,location_city,location_city_id,location_region,location_state,location_region_id,location_latitude,location_longitude,is_published,is_verified,is_community_page,can_post,fan_count,followers_count,talking_about_count,checkins",
        "settings": {"report_type": "Page"},
        "max_rows": 100000,
        "api_key": "api_1dK_S8j0F5ASCHjVEi4hLp7wdtTlGkI50tTX02AjhsXFL_J7GE9tkkc3llRz4KYQ1KhT95686aeCE26a3XiIlxmRmD_jP97cKJaH"
    }
    
    page_data_url = 'https://api.supermetrics.com/enterprise/v2/query/data/json?json=' + json.dumps(page_data_json_config)
    print("page_data_url=========111===",page_data_url)
    
    response = requests.get(page_data_url, timeout=600)
    
    if response.status_code == 200:
        data = response.json()
        
        if data['data']:
            keys = data['data'][0]
            del data['data'][0]
            
            keys = [x.lower().replace(' ','_').replace('(','').replace(')','').replace(':','') for x in keys]

            final_data = []
            total_data = {
                "likes": 0,
                "reactions_love": 0,
                "reactions_wow": 0,
                "reactions_haha": 0,
                "reactions_sad": 0,
                "reactions_angry": 0,
                "reactions_thankful": 0,
                "reactions_pride": 0,
                "reactions": 0,
                "comments": 0,
                "post_shares": 0,
                "likes_per_post": 0,
                "reactions_per_post": 0,
                "comments_per_post": 0,
	            "shares_per_post": 0,
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
            fb_page_data.insert_many(final_data)
        else:
            logging.warning(f"Page Repose Empty from Supermetrics :: username: {username} :: Facebook Link: {link} :: SuperMetric URL: {page_data_url}")
    else:
        logging.error(f"Page Repose Error from Supermetrics :: username: {username} :: Facebook Link: {link} :: SuperMetric URL: {page_data_url} :: Reponse Code: {response.status_code} :: Reponse: {response.text}")
    
    start_date = datetime.date(2023, 9, 1)
    end_date = datetime.date(2023, 11, 30)

    current_month = start_date.month
    
    while start_date <= end_date:
        
        end_date_s = start_date.replace(day=1) + datetime.timedelta(days=32)
        end_date_s = end_date_s.replace(day=1) - datetime.timedelta(days=1)    
        #Page Post Data
        
        page_post_data_json_config = {
            "ds_id": "FBPD",
            "ds_accounts": username,
            "ds_user": "amarjit@insitedigi.com",
            "start_date":str(start_date),
            "end_date":str(end_date_s),
            # Old
            # "fields": "created_time,created_date,link,post_id,status_type,type,permalink_url,from_id,from_name,story,caption,message,post_link,source,application_name,story_tags,place,full_picture,application_link,application_category,dataSourceName,posts,likes_count,reactions_love,reactions_wow,reactions_haha,reactions_sad,reactions_angry,reactions_thankful,reactions_pride,reactions_count,comments_count,shares_count,likesPerPost,reactionsPerPost,commentsPerPost,sharesPerPost",
            # "fields": "created_time,created_date,post_id,likes_count,comments_count,commentsPerPost",
            # New
            # "fields": "created_time,created_date,post_id,posts,reactions_love,reactions_wow,reactions_haha,reactions_sad,reactions_angry,reactions_thankful,reactions_pride,reactions_count,shares_count,likesPerPost,reactionsPerPost,sharesPerPost,likes_count,comments_count,commentsPerPost",
            "fields": "created_time,created_date,link,post_id,status_type,type,permalink_url,from_id,from_name,story,caption,message,post_link,source,application_name,story_tags,place,full_picture,application_link,application_category,dataSourceName,posts,likes_count,reactions_love,reactions_wow,reactions_haha,reactions_sad,reactions_angry,reactions_thankful,reactions_pride,reactions_count,comments_count,shares_count,likesPerPost,reactionsPerPost,commentsPerPost,sharesPerPost",
            "settings": {
            
                "report_type":"PagePosts","timezone":"Asia/Dubai"
            },
            "max_rows": 100000,
            "api_key": "api_1dK_S8j0F5ASCHjVEi4hLp7wdtTlGkI50tTX02AjhsXFL_J7GE9tkkc3llRz4KYQ1KhT95686aeCE26a3XiIlxmRmD_jP97cKJaH"
        }
        
        # print(page_post_data_json_config)
        page_data_url = 'https://api.supermetrics.com/enterprise/v2/query/data/json?json=' + json.dumps(page_post_data_json_config)
        print("post_data_url==========1111122=========", page_data_url)
        
        response = requests.get(page_data_url, timeout=600)
        
        if response.status_code == 200:
            data = response.json()
            # print('data======================>', data)
            
            if data['data']:
                keys = data['data'][0]
                del data['data'][0]
                
                keys = [x.lower().replace(' ','_').replace('(','').replace(')','').replace(':','') for x in keys]
                print('kyes================',keys)

                final_data = []
                
                total_data = {
                    "likes": 0,
                    "reactions_love": 0,
                    "reactions_wow": 0,
                    "reactions_haha": 0,
                    "reactions_sad": 0,
                    "reactions_angry": 0,
                    "reactions_thankful": 0,
                    "reactions_pride": 0,
                    "reactions": 0,
                    "comments": 0,
                    "post_shares": 0,
                    "likes_per_post": 0,
                    "reactions_per_post": 0,
                    "comments_per_post": 0,
                    "shares_per_post": 0
                }
                
                for each_data in data['data']:
                    print('each==================', each_data)
                    temp = dict(zip(keys, each_data))
                    # print('temp===================', temp)
                    temp['brand_id'] = brand_id
                    temp['date'] = api_date
                    temp['created_at'] = datetime.datetime.now()
                    temp['modified_at'] = datetime.datetime.now()
                    for key in total_data:
                        # print("=============", type(total_data[key]),"=====", type(temp.get(key, 0)),"==",temp.get(key, 0))
                        total_data[key] = total_data[key] + temp.get(key, 0) if type(temp.get(key, 0))=='int' else 0
                    
                    final_data.append(temp)
                page_id_list.append(final_data[0].get('page_id'))
                total_data['total_posts'] = len(final_data)
                    
                #Inserting Data in Mongo
                fb_page_post_data.insert_many(final_data)
                
                #update Main Collection Data to include total_counts
                myquery = { "brand_id": brand_id, "date": api_date }
                total_data_key = { "$set": { "post_totals": total_data } }
                fb_page_data.update_one(myquery, total_data_key)
                
            else:
                logging.warning(f"Page Post Repose Empty from Supermetrics :: username: {username} :: Facebook Link: {link} :: SuperMetric URL: {page_data_url}")
        else:
            logging.error(f"Page Post Repose Error from Supermetrics :: username: {username} :: Facebook Link: {link} :: SuperMetric URL: {page_data_url} :: Reponse Code: {response.status_code} :: Reponse: {response.text}")
        # Update the start_date to the next month
        if start_date.month == 12:
            start_date = start_date.replace(year=start_date.year + 1, month=1)
        else:
            start_date = start_date.replace(month=start_date.month + 1)
logging.info("FB Script Execution Ended")
print("page_id", page_id_list)
