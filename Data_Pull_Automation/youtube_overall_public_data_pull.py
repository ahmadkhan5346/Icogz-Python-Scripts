# Sample Python code for user authorization

import os

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

from oauth2client.client import GoogleCredentials
from oauth2client import GOOGLE_TOKEN_URI
import datetime, pymongo, logging, json

from config import DB_USERNAME, DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, YT_BRAND_LIST, YT_BRAND, YT_VIDEO_COLLECTION, META_BRAND_LIST

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "creds/arjun_client_secrent_yt.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
REDIRECT_URI = 'http://localhost'


def get_authenticated_service():
    if os.path.exists("./creds/arjun_creds.json"):
        with open("./creds/arjun_creds.json", "rb") as token:
            creds = json.load(token)

        access_token = creds['token']
        token_expiry = creds['expiry']
        token_uri = GOOGLE_TOKEN_URI
        user_agent = 'Python client library'
        revoke_uri = None
        credentials = GoogleCredentials(
            access_token,
            creds['client_id'],
            creds['client_secret'],
            creds['refresh_token'],
            token_expiry,
            token_uri,
            user_agent,
            revoke_uri=revoke_uri)
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRETS_FILE, scopes=SCOPES, redirect_uri=REDIRECT_URI)
        auth_uri = flow.authorization_url()
        print("Go to URL in browser: ", auth_uri)
        code = input('Enter URL Decoded authorization code: ')
        flow.fetch_token(code=code)
        credentials = flow.credentials
        print(flow.credentials.to_json())
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


def channels_list_by_username(service, **kwargs):
    results = service.channels().list(**kwargs).execute()

    print('This channel\'s ID is %s. Its title is %s, and it has %s views.' %
          (results['items'][0]['id'],
           results['items'][0]['snippet']['title'],
           results['items'][0]['statistics']['viewCount']))


def get_my_uploads_list(service, channel):
    # Retrieve the contentDetails part of the channel resource for the
    # authenticated user's channel.
    channels_response = service.channels().list(
        id=channel_id,
        part='contentDetails'
    ).execute()

    for channel in channels_response['items']:
        # From the API response, extract the playlist ID that identifies the list
        # of videos uploaded to the authenticated user's channel.
        return channel['contentDetails']['relatedPlaylists']['uploads']

    return None


def list_my_uploaded_videos(service, uploads_playlist_id):
    # Retrieve the list of videos uploaded to the authenticated user's channel.
    try:
        playlistitems_list_request = service.playlistItems().list(
            playlistId=uploads_playlist_id,
            part='snippet',
            maxResults=50
        )
    except Exception as e:
            logging.exception(f"Playlist fetching failed because of exception with exepction {e}") 

#   print( 'Videos in list %s' % uploads_playlist_id)
    temp_data = []
    while playlistitems_list_request:
        try:
            playlistitems_list_response = playlistitems_list_request.execute()
        except Exception as e:
            playlistitems_list_response = {'items':[]}
            logging.exception(f"DATA fetching failed because of exception") 

        # Print information about each video.
        for playlist_item in playlistitems_list_response['items']:
            title = playlist_item['snippet']['title']
            video_id = playlist_item['snippet']['resourceId']['videoId']
            try:
                ratings = service.videos().list(id=video_id, part="snippet,statistics").execute()
            except Exception as e:
                logging.exception(f"Rating fetching failed because of exception") 
                
            try:
                ratings_data = ratings['items'][0]['statistics']
            except Exception as e:
                logging.exception(f"No Ratings Found")
                ratings_data = {}
            
            temp_dict = { 
                'channel_id': playlist_item['snippet']['channelId'],
                'title': title, 
                'description': playlist_item['snippet']['description'], 
                'video_id':video_id,
                'published_at': playlist_item['snippet']['publishedAt'], 
                #'ratings': ratings['items'][0]['statistics'],
                'view_count': ratings_data.get('viewCount') or 0,
                'like_count': ratings_data.get('likeCount') or 0,
                'favorite_count': ratings_data.get('favoriteCount') or 0,
                'comment_count': ratings_data.get('commentCount') or 0
            }
            temp_data.append(temp_dict)

        if len(temp_data) > 250:
            playlistitems_list_request = False
        else:
            playlistitems_list_request = service.playlistItems().list_next(playlistitems_list_request, playlistitems_list_response)
        
    return temp_data


if __name__ == '__main__':
    #enable Logging
    logging.basicConfig(filename="yoututbe.log", format='%(asctime)s %(message)s', level=logging.INFO)
    
    # When running locally, disable OAuthlib's HTTPs verification. When
    # running in production *do not* leave this option enabled.
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    service = get_authenticated_service()
    
    
    current_date = datetime.datetime.today().strftime('%Y-%m-%d')
    api_date = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    
    # myclient = pymongo.MongoClient("mongodb://216.48.180.31:27017/",username='admin',password='paS3w0rd')
    myclient = pymongo.MongoClient(f"mongodb://{DB_HOST}:{DB_PORT}/",username = DB_USERNAME,password = DB_PASSWORD)

    try:
        
        # mydb = myclient["bfsi_youtube_data_28112023"] #databasename
        mydb = myclient[DB_NAME] #databasename
        
        # yt_collection = mydb["youtube_brand"] #collectionname
        yt_collection = mydb[YT_BRAND] #collectionname
        
        # yt_video_collection = mydb["youtube_brand_video_data"] #collectionname
        yt_video_collection = mydb[YT_VIDEO_COLLECTION] #collectionname

        # col = mydb["yt_brand_list"]
        col = mydb[META_BRAND_LIST]
        
        
        x = col.find({"fetch":True}, {'_id': 0, 'Brand': 1, 'YouTube':1})
    except Exception as e:
        print("No record found!")
        
        
    for line_item in x:
        # print(line_item)
        # continue
        if line_item.get('YouTube'):
            temp_checker = line_item['YouTube'].split('/')
            if temp_checker[3] == 'c' or temp_checker[3] == 'channel':
                if '?' in temp_checker[4]:
                    channel_id =  temp_checker[4].split("?")[0]
                else:
                    channel_id =  temp_checker[4]
                    
                try:    
                    channel = service.channels().list(id=channel_id, part='contentDetails,snippet,statistics').execute()
                except Exception as e:
                    print(f"Channel Fetching Failed for:: {line_item['YouTube']}")
            
            elif temp_checker[3] == 'user':
                channel_id = temp_checker[4]
                try:
                    channel = service.channels().list(forUsername=channel_id, part='contentDetails,snippet,statistics').execute()
                except Exception as e:
                    print(f"Channel Fetching Failed for:: {line_item['YouTube']}")
                    
            elif temp_checker[3] == 'watch':
                logging.info(f"Wrong URL :: DATE: {api_date} :: PROFILE: {line_item['Brand']} URL:: {line_item['YouTube']}")
                
            else:
                channel_id = temp_checker[3]
                try:
                    channel = service.channels().list(forUsername=channel_id, part='contentDetails,snippet,statistics').execute()
                except Exception as e:
                    print(f"Channel Fetching Failed for:: {line_item['YouTube']}")
            
            logging.info(f"Data Fetching for channel :: {channel_id} :: DATE: {api_date} :: PROFILE: {line_item['Brand']}")
            
            if channel.get('items'):
                channel_id = channel.get('items')[0].get('id')
            else:
                channel_id = None
                logging.info(f"No Data Found for channel :: {channel_id} :: DATE: {api_date} :: PROFILE: {line_item['Brand']}")

            query = {"channel_id": channel_id,'date': api_date}
            doc_count = yt_collection.count_documents(query)

            if doc_count == 0: #no old Data
                if channel_id:
                    uploads_playlist_id = channel['items'][0]['contentDetails']['relatedPlaylists']['uploads']
                    if uploads_playlist_id:
                        all_videos_data = list_my_uploaded_videos(service, uploads_playlist_id)
                
                    view_count = 0
                    like_count = 0
                    favorite_count = 0
                    comment_count = 0
                    for each_video in all_videos_data:
                        each_video['date'] = api_date
                        each_video['created_at'] = datetime.datetime.now(), 
                        each_video['modified_at'] = datetime.datetime.now(),
                        view_count = view_count + int(each_video['view_count'])
                        like_count = like_count + int(each_video['like_count'])
                        favorite_count = favorite_count + int(each_video['favorite_count'])
                        comment_count = comment_count + int(each_video['comment_count'])
                    
                    main_insert_data = {
                        'brand': channel['items'][0]['snippet']['title'],
                        'channel_id': channel_id,
                        'channel_title': channel['items'][0]['snippet']['title'],
                        'channel_description': channel['items'][0]['snippet']['description'],
                        'channel_pubished_at': channel['items'][0]['snippet']['publishedAt'],
                        'channel_username': channel['items'][0]['snippet'].get('customUrl') or None,
                        'total_view_count': channel['items'][0]['statistics']['viewCount'],
                        'total_subscriber_count': channel['items'][0]['statistics']['subscriberCount'],
                        'total_video_count': channel['items'][0]['statistics']['videoCount'],
                        'last_10_video_view_count': view_count,
                        'last_10_video_like_count': like_count,
                        'last_10_video_favorite_count': favorite_count,
                        'last_10_video_comment_count': comment_count,
                        'created_at': datetime.datetime.now(), 
                        'modified_at': datetime.datetime.now(),
                        'date': api_date,
                        'yt_url': line_item['YouTube']
                    }

                    yt_collection.insert_one(main_insert_data)
                    if len(all_videos_data):
                        yt_video_collection.insert_many(all_videos_data)
                
        
    
    # channels_list_by_username(service,part='snippet,contentDetails,statistics',forUsername='things2do')
