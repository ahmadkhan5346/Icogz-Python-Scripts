#FB and Insta

#SEREVR
DB_HOST = '216.48.180.31'
# DB_HOST = 'localhost'
DB_USERNAME = 'admin'
DB_PASSWORD = 'paS3w0rd'
DB_PORT = '27017'
DB_NAME = 'ENBD_Social_Public_data'


META_BRAND_LIST = 'meta_brand_list'
YT_BRAND_LIST = 'yt_brand_list'

YT_BRAND = 'yt_brand'
YT_COLLECTION = 'yt_brand'
YT_VIDEO_COLLECTION = 'youtube_brand_video_data_07_02_2024'

FB_PAGE_DATA = 'facebook_page_data_07_02_2024'
FB_PAGE_POST_DATA = 'facebook_page_post_data_07_02_2024'

INSTA_PAGE_DATA = 'instagram_page_data_07_02_2024'
INSTA_PAGE_POST_DATA = 'instagram_page_post_data_07_02_2024'


#Constants
DATE_FORMAT='%Y-%m-%d'
SUPER_API_KEY='api_1dK_S8j0F5ASCHjVEi4hLp7wdtTlGkI50tTX02AjhsXFL_J7GE9tkkc3llRz4KYQ1KhT95686aeCE26a3XiIlxmRmD_jP97cKJaH'


youtube_key = 'AIzaSyCpoVbGmilhoVfMpzS0SBTv9BdwFxQHtZQ'


page_data = {
  'meta': {
    'request_id': 'TLhjvQleq8e4zlySWFuT2JVXXaLS8kE4',
    'schedule_id': '964fff52b4e62bbcfcea356c5a93a2f83b2f10811a753f2709796caef605a5f1',
    'status_code': 'SUCCESS',
    'query': {
      'start_date': None,
      'end_date': None,
      'ds_accounts': [
        'ADCB'
      ],
      'ds_segments': [
        
      ],
      'fields': [
        {
          'id': 'today',
          'field_id': 'today',
          'field_name': 'Today',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.time.date',
          'data_column': 0,
          'visible': True
        },
        {
          'id': 'dataSourceName',
          'field_id': 'dataSourceName',
          'field_name': 'Data source',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.text.value',
          'data_column': 1,
          'visible': True
        },
        {
          'id': 'ig_id',
          'field_id': 'ig_id',
          'field_name': 'Instagram ID',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.text.value',
          'data_column': 2,
          'visible': True
        },
        {
          'id': 'username',
          'field_id': 'username',
          'field_name': 'Username',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.text.value',
          'data_column': 3,
          'visible': True
        },
        {
          'id': 'name',
          'field_id': 'name',
          'field_name': 'Name',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.text.value',
          'data_column': 4,
          'visible': True
        },
        {
          'id': 'biography',
          'field_id': 'biography',
          'field_name': 'Biography',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.text.value',
          'data_column': 5,
          'visible': True
        },
        {
          'id': 'profile_picture_url',
          'field_id': 'profile_picture_url',
          'field_name': 'Profile picture URL',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.text.value',
          'data_column': 6,
          'visible': True
        },
        {
          'id': 'website',
          'field_id': 'website',
          'field_name': 'Website',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.text.url',
          'data_column': 7,
          'visible': True
        },
        {
          'id': 'followers',
          'field_id': 'followers',
          'field_name': 'Profile followers',
          'field_type': 'met',
          'field_split': 'row',
          'data_type': 'int.number.value',
          'data_column': 8,
          'visible': True
        },
        {
          'id': 'follows',
          'field_id': 'follows',
          'field_name': 'Profile follows',
          'field_type': 'met',
          'field_split': 'row',
          'data_type': 'int.number.value',
          'data_column': 9,
          'visible': True
        },
        {
          'id': 'total_post_count',
          'field_id': 'total_post_count',
          'field_name': 'Profile post count',
          'field_type': 'met',
          'field_split': 'row',
          'data_type': 'int.number.value',
          'data_column': 10,
          'visible': True
        }
      ],
      'compare_type': None,
      'compare_show': None,
      'compare_start_date': None,
      'compare_end_date': None,
      'settings': {
        'report_type': 'BusinessDiscoveryAccount',
        'timezone': 'Asia/Dubai',
        'round_metrics_to': 4,
        'no_json_keys': True
      },
      'cache_minutes': None
    },
    'result': {
      'total_columns': 11,
      'total_rows': 2,
      'run_seconds': 1.484,
      'data_sampled': None,
      'cache_used': False,
      'cache_time': None
    },
    'paginate': {
      'prev': None,
      'next': None
    }
  },
  'data': [
    [
      'Today',
      'Data source',
      'Instagram ID',
      'Username',
      'Name',
      'Biography',
      'Profile picture URL',
      'Website',
      'Profile followers',
      'Profile follows',
      'Profile post count'
    ],
    [
      '2024-02-08',
      'Instagram Public Data',
      11473971231,
      'adcb',
      'ADCB بنك أبوظبي التجاري',
      'نرحب بكم في الحساب الرسمي لبنك أبوظبي التجاري\nWelcome to Abu Dhabi Commercial Bank’s official Instagram account',
      'https://scontent-fra3-2.xx.fbcdn.net/v/t51.2885-15/411802562_1088489768992873_5827031017296475604_n.jpg?_nc_cat=1&ccb=1-7&_nc_sid=7d201b&_nc_ohc=G5Rxp7ry0SUAX-E_Fat&_nc_ht=scontent-fra3-2.xx&edm=AL-3X8kEAAAA&oh=00_AfB-iq8M-9XcOyEc-owLdpZxx-FdIPkHPbgvuVioo1RCKw&oe=65C9ACA1',
      'https://adcb.com/',
      40466,
      0,
      498
    ]
  ]
}


post_data = {
  'meta': {
    'request_id': 'hSwlZ_vdLkpDMbFa97eByDHbRh7_42qS',
    'schedule_id': '947d42f9eee5214f287d9c07391003aeafd9eb1cc94f1268146a7d0e17dcb6a0',
    'status_code': 'SUCCESS',
    'query': {
      'start_date': '2023-11-28',
      'end_date': '2023-11-30',
      'ds_accounts': [
        'ADCB'
      ],
      'ds_segments': [
        
      ],
      'fields': [
        {
          'id': 'dataSourceName',
          'field_id': 'dataSourceName',
          'field_name': 'Data source',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.text.value',
          'data_column': 0,
          'visible': True
        },
        {
          'id': 'post_id',
          'field_id': 'post_id',
          'field_name': 'Post ID',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.text.value',
          'data_column': 1,
          'visible': True
        },
        {
          'id': 'post_timestamp',
          'field_id': 'post_timestamp',
          'field_name': 'Post created',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.time.datetime',
          'data_column': 2,
          'visible': True
        },
        {
          'id': 'post_type',
          'field_id': 'post_type',
          'field_name': 'Post type',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.text.value',
          'data_column': 3,
          'visible': True
        },
        {
          'id': 'post_media_url',
          'field_id': 'post_media_url',
          'field_name': 'Post media URL',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.text.url',
          'data_column': 4,
          'visible': True
        },
        {
          'id': 'post_permalink',
          'field_id': 'post_permalink',
          'field_name': 'Link to post',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.text.url',
          'data_column': 5,
          'visible': True
        },
        {
          'id': 'post_caption',
          'field_id': 'post_caption',
          'field_name': 'Post caption',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.text.value',
          'data_column': 6,
          'visible': True
        },
        {
          'id': 'ig_id',
          'field_id': 'ig_id',
          'field_name': 'Instagram ID',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.text.value',
          'data_column': 7,
          'visible': True
        },
        {
          'id': 'username',
          'field_id': 'username',
          'field_name': 'Username',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.text.value',
          'data_column': 8,
          'visible': True
        },
        {
          'id': 'name',
          'field_id': 'name',
          'field_name': 'Name',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.text.value',
          'data_column': 9,
          'visible': True
        },
        {
          'id': 'biography',
          'field_id': 'biography',
          'field_name': 'Biography',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.text.value',
          'data_column': 10,
          'visible': True
        },
        {
          'id': 'profile_picture_url',
          'field_id': 'profile_picture_url',
          'field_name': 'Profile picture URL',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.text.value',
          'data_column': 11,
          'visible': True
        },
        {
          'id': 'website',
          'field_id': 'website',
          'field_name': 'Website',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.text.url',
          'data_column': 12,
          'visible': True
        },
        {
          'id': 'year',
          'field_id': 'year',
          'field_name': 'Year',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.time.year',
          'data_column': 13,
          'visible': True
        },
        {
          'id': 'yearOfWeek',
          'field_id': 'yearOfWeek',
          'field_name': 'Year of week',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.time.year',
          'data_column': 14,
          'visible': True
        },
        {
          'id': 'yearOfWeekIso',
          'field_id': 'yearOfWeekIso',
          'field_name': 'Year of week',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.time.year',
          'data_column': 15,
          'visible': True
        },
        {
          'id': 'yearMonth',
          'field_id': 'yearMonth',
          'field_name': 'Year & month',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.time.yearmonth',
          'data_column': 16,
          'visible': True
        },
        {
          'id': 'month',
          'field_id': 'month',
          'field_name': 'Month',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.time.month',
          'data_column': 17,
          'visible': True
        },
        {
          'id': 'yearWeek',
          'field_id': 'yearWeek',
          'field_name': 'Year & week',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.time.yearweek',
          'data_column': 18,
          'visible': True
        },
        {
          'id': 'yearWeekIso',
          'field_id': 'yearWeekIso',
          'field_name': 'Year & week',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.time.yearweekiso',
          'data_column': 19,
          'visible': True
        },
        {
          'id': 'week',
          'field_id': 'week',
          'field_name': 'Week',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.time.week',
          'data_column': 20,
          'visible': True
        },
        {
          'id': 'weekIso',
          'field_id': 'weekIso',
          'field_name': 'Week',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.time.weekiso',
          'data_column': 21,
          'visible': True
        },
        {
          'id': 'dayOfMonth',
          'field_id': 'dayOfMonth',
          'field_name': 'Day of month',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.time.dayofmonth',
          'data_column': 22,
          'visible': True
        },
        {
          'id': 'dayOfWeekName',
          'field_id': 'dayOfWeekName',
          'field_name': 'Day of week',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.time.dayofweek',
          'data_column': 23,
          'visible': True
        },
        {
          'id': 'dayOfWeekNameIso',
          'field_id': 'dayOfWeekNameIso',
          'field_name': 'Day of week',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.time.dayofweekiso',
          'data_column': 24,
          'visible': True
        },
        {
          'id': 'date',
          'field_id': 'date',
          'field_name': 'Date',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.time.date',
          'data_column': 25,
          'visible': True
        },
        {
          'id': 'today',
          'field_id': 'today',
          'field_name': 'Today',
          'field_type': 'dim',
          'field_split': 'row',
          'data_type': 'string.time.date',
          'data_column': 26,
          'visible': True
        },
        {
          'id': 'likes_per_post',
          'field_id': 'likes_per_post',
          'field_name': 'Likes per post',
          'field_type': 'met',
          'field_split': 'row',
          'data_type': 'float.number.value',
          'data_column': 27,
          'visible': True
        },
        {
          'id': 'comments_per_post',
          'field_id': 'comments_per_post',
          'field_name': 'Comments per post',
          'field_type': 'met',
          'field_split': 'row',
          'data_type': 'float.number.value',
          'data_column': 28,
          'visible': True
        },
        {
          'id': 'posts',
          'field_id': 'posts',
          'field_name': 'Posts',
          'field_type': 'met',
          'field_split': 'row',
          'data_type': 'int.number.value',
          'data_column': 29,
          'visible': True
        },
        {
          'id': 'post_comments',
          'field_id': 'post_comments',
          'field_name': 'Comments',
          'field_type': 'met',
          'field_split': 'row',
          'data_type': 'int.number.value',
          'data_column': 30,
          'visible': True
        },
        {
          'id': 'post_likes',
          'field_id': 'post_likes',
          'field_name': 'Likes',
          'field_type': 'met',
          'field_split': 'row',
          'data_type': 'int.number.value',
          'data_column': 31,
          'visible': True
        }
      ],
      'compare_type': None,
      'compare_show': None,
      'compare_start_date': None,
      'compare_end_date': None,
      'settings': {
        'report_type': 'BusinessDiscoveryMedia',
        'timezone': 'Asia/Dubai',
        'round_metrics_to': 4,
        'no_json_keys': True
      },
      'cache_minutes': None
    },
    'result': {
      'total_columns': 32,
      'total_rows': 6,
      'run_seconds': 1.666,
      'data_sampled': None,
      'cache_used': False,
      'cache_time': None
    },
    'paginate': {
      'prev': None,
      'next': None
    }
  },
  'data': [
    [
      'Data source',
      'Post ID',
      'Post created',
      'Post type',
      'Post media URL',
      'Link to post',
      'Post caption',
      'Instagram ID',
      'Username',
      'Name',
      'Biography',
      'Profile picture URL',
      'Website',
      'Year',
      'Year of week',
      'Year of week',
      'Year & month',
      'Month',
      'Year & week',
      'Year & week',
      'Week',
      'Week',
      'Day of month',
      'Day of week',
      'Day of week',
      'Date',
      'Today',
      'Likes per post',
      'Comments per post',
      'Posts',
      'Comments',
      'Likes'
    ],
    [
      'Instagram Public Data',
      '17943269846639353',
      '2023-11-29 19:21:17',
      'VIDEO',
      'https://scontent-fra3-2.cdninstagram.com/o1/v/t16/f1/m82/2042F5B4223C2D6B1263D071698FD7A1_video_dashinit.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6InZ0c192b2RfdXJsZ2VuLmNsaXBzLnVua25vd24tQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSJ9&_nc_ht=scontent-fra3-2.cdninstagram.com&_nc_cat=104&vs=1079807346712111_3184365984&_nc_vs=HBksFQIYT2lnX3hwdl9yZWVsc19wZXJtYW5lbnRfcHJvZC8yMDQyRjVCNDIyM0MyRDZCMTI2M0QwNzE2OThGRDdBMV92aWRlb19kYXNoaW5pdC5tcDQVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dQNEZRQmdNaWdZcEpjb0FBUGRjTWpyX1VPTnRicV9FQUFBRhUCAsgBACgAGAAbAYgHdXNlX29pbAExFQAAJrqNmIjvjIhAFQIoAkMzLBdAXtcKPXCj1xgSZGFzaF9iYXNlbGluZV8xX3YxEQB1AAA%3D&ccb=9-4&oh=00_AfCHHGKty2MTp33AfmyY-g1ANFBeG_T5t1YrjWe5WJfIUg&oe=65C660F0&_nc_sid=1d576d&_nc_rid=3ade3766cb',
      'https://www.instagram.com/reel/C0PBfOmJj-0/',
      'أعلن #بنك_أبوظبي_التجاري عن انضمامه إلى التحالف المصرفي لخفض صافي الانبعاثات الكربونية إلى الصفر الذي أطلقته الأمم المتحدة، والذي يجمع تحت مظلته أكثر من 130 مؤسسة مصرفية عالمية يصل إجمالي حجم أصولها إلى 74 تريليون دولار أمريكي، بهدف تمويل الجهود للانتقال إلى الحياد المناخي بحلول عام 2050 والحد من ظاهرة الاحتباس الحراري إلى 1.5 درجة مئوية.\n \n#ADCB has joined the Net Zero Banking Alliance (NZBA), a group of over 130 global banks with USD 74 trillion in total assets committed to financing climate action to transition to net zero greenhouse gas (GHG) emissions by 2050 in line with limiting global warming to 1.5°C. #ADCBnetzero\n\n#uae #الإمارات',
      11473971231,
      'adcb',
      'ADCB بنك أبوظبي التجاري',
      'نرحب بكم في الحساب الرسمي لبنك أبوظبي التجاري\nWelcome to Abu Dhabi Commercial Bank’s official Instagram account',
      'https://scontent-fra3-2.xx.fbcdn.net/v/t51.2885-15/411802562_1088489768992873_5827031017296475604_n.jpg?_nc_cat=1&ccb=1-7&_nc_sid=7d201b&_nc_ohc=G5Rxp7ry0SUAX-0Ynj2&_nc_ht=scontent-fra3-2.xx&edm=AL-3X8kEAAAA&oh=00_AfDs_MD8MSGyk3xwUKuLr3nmlm8WVn1GuOP5iETJkHanWg&oe=65C9ACA1',
      'https://adcb.com/',
      '2023',
      '2023',
      '2023',
      '2023|11',
      '11',
      '2023|48',
      '2023|48',
      '48',
      '48',
      '29',
      '3 Wednesday',
      '3 Wednesday',
      '2023-11-29',
      '2024-02-08',
      74,
      4,
      1,
      4,
      74
    ],
    [
      'Instagram Public Data',
      '17958202190688237',
      '2023-11-28 09:47:19',
      'VIDEO',
      'https://scontent-fra3-2.cdninstagram.com/o1/v/t16/f1/m82/EB40DFE80F8838E4382A19593BE3F99E_video_dashinit.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6InZ0c192b2RfdXJsZ2VuLmNsaXBzLnVua25vd24tQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSJ9&_nc_ht=scontent-fra3-2.cdninstagram.com&_nc_cat=103&vs=598769702338566_1509508174&_nc_vs=HBksFQIYT2lnX3hwdl9yZWVsc19wZXJtYW5lbnRfcHJvZC9FQjQwREZFODBGODgzOEU0MzgyQTE5NTkzQkUzRjk5RV92aWRlb19kYXNoaW5pdC5tcDQVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dMQ2RNaGpOZjF6b2pZTUZBQ2pzcklFbmR2UlZicV9FQUFBRhUCAsgBACgAGAAbAYgHdXNlX29pbAExFQAAJtqGroOnq%2Fk%2FFQIoAkMzLBdATwAAAAAAABgSZGFzaF9iYXNlbGluZV8xX3YxEQB1AAA%3D&ccb=9-4&oh=00_AfC7xQHmY1jO1Y3pbXeyEpyab620JCt1MfM6yS09wYvACw&oe=65C6298F&_nc_sid=1d576d&_nc_rid=ba02421110',
      'https://www.instagram.com/reel/C0La57upMX2/',
      'عميقة جذورنا...عالية طموحاتنا.\n \nمجموعة #بنك_أبوظبي_التجاري تحتفل باليوم الوطني الثاني والخمسين لدولة #الإمارات العربية المتحدة. كل عام وإماراتنا بألف خير.\n \nStrong Foundations…Soaring Ambitions.\n#ADCB Group proudly celebrates the 52nd National Day of the #UnitedArabEmirates.',
      11473971231,
      'adcb',
      'ADCB بنك أبوظبي التجاري',
      'نرحب بكم في الحساب الرسمي لبنك أبوظبي التجاري\nWelcome to Abu Dhabi Commercial Bank’s official Instagram account',
      'https://scontent-fra3-2.xx.fbcdn.net/v/t51.2885-15/411802562_1088489768992873_5827031017296475604_n.jpg?_nc_cat=1&ccb=1-7&_nc_sid=7d201b&_nc_ohc=G5Rxp7ry0SUAX-0Ynj2&_nc_ht=scontent-fra3-2.xx&edm=AL-3X8kEAAAA&oh=00_AfDs_MD8MSGyk3xwUKuLr3nmlm8WVn1GuOP5iETJkHanWg&oe=65C9ACA1',
      'https://adcb.com/',
      '2023',
      '2023',
      '2023',
      '2023|11',
      '11',
      '2023|48',
      '2023|48',
      '48',
      '48',
      '28',
      '2 Tuesday',
      '2 Tuesday',
      '2023-11-28',
      '2024-02-08',
      205,
      14,
      1,
      14,
      205
    ],
    [
      'Instagram Public Data',
      '17983426031601946',
      '2023-11-29 14:13:45',
      'VIDEO',
      'https://scontent-fra3-2.cdninstagram.com/o1/v/t16/f1/m82/544B0253BCAA439B5BA7A041D6EC1B88_video_dashinit.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6InZ0c192b2RfdXJsZ2VuLmNsaXBzLnVua25vd24tQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSJ9&_nc_ht=scontent-fra3-2.cdninstagram.com&_nc_cat=106&vs=222444427541059_1073243068&_nc_vs=HBksFQIYT2lnX3hwdl9yZWVsc19wZXJtYW5lbnRfcHJvZC81NDRCMDI1M0JDQUE0MzlCNUJBN0EwNDFENkVDMUI4OF92aWRlb19kYXNoaW5pdC5tcDQVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dNV3JQUmhXQlhGUkhyQUVBTVJJNWRxYzlhNGJicV9FQUFBRhUCAsgBACgAGAAbAYgHdXNlX29pbAExFQAAJuq7m8fZ%2Bq5AFQIoAkMzLBdALgAAAAAAABgSZGFzaF9iYXNlbGluZV8xX3YxEQB1AAA%3D&ccb=9-4&oh=00_AfBS-q9-fUiuw4sDQAcNW3AZg-nhfXpDF14NBujCOH7peQ&oe=65C639CA&_nc_sid=1d576d&_nc_rid=18088bf728',
      'https://www.instagram.com/reel/C0OcxwRpxY1/',
      'تهانينا ا. حسين الرابح لمبلغ 1,000,000 درهم في السحب الشهري لحساب توفير المليونير الإسلامي، و محمد المنصوري الرابح لمبلغ 500,000 درهم في السحب الشهري لحساب توفير المليونير الإماراتي. هل ترغب في أن تكون المليونير القادم؟ سجّل عبر\u200f\u200e\u200f\nadcbislamic.com/save-ar\nأو حمٓل تطبيق حياك الآن\n \nCongratulations to A. HUSSAIN for winning AED 1,000,000 in our monthly grand prize Millionaire Destiny Savings Account and MOHAMMED ALMANSOORI for winning AED 500,000 in our monthly grand prize Emirati Millionaire Savings Account draw. Want to be the next millionaire?\nApply through adcbislamic.com/save or download the Hayyak app now\u200e\n\n#uae #الإمارات\n#adcb #بنك_أبوظبي_التجاري',
      11473971231,
      'adcb',
      'ADCB بنك أبوظبي التجاري',
      'نرحب بكم في الحساب الرسمي لبنك أبوظبي التجاري\nWelcome to Abu Dhabi Commercial Bank’s official Instagram account',
      'https://scontent-fra3-2.xx.fbcdn.net/v/t51.2885-15/411802562_1088489768992873_5827031017296475604_n.jpg?_nc_cat=1&ccb=1-7&_nc_sid=7d201b&_nc_ohc=G5Rxp7ry0SUAX-0Ynj2&_nc_ht=scontent-fra3-2.xx&edm=AL-3X8kEAAAA&oh=00_AfDs_MD8MSGyk3xwUKuLr3nmlm8WVn1GuOP5iETJkHanWg&oe=65C9ACA1',
      'https://adcb.com/',
      '2023',
      '2023',
      '2023',
      '2023|11',
      '11',
      '2023|48',
      '2023|48',
      '48',
      '48',
      '29',
      '3 Wednesday',
      '3 Wednesday',
      '2023-11-29',
      '2024-02-08',
      33,
      6,
      1,
      6,
      33
    ],
    [
      'Instagram Public Data',
      '18015858313832334',
      '2023-11-30 16:40:06',
      'IMAGE',
      'https://scontent-fra3-1.cdninstagram.com/v/t51.29350-15/405218890_730812108443787_5564875392587692654_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=18de74&_nc_ohc=5XEsvj_Tg6wAX8UXQ2h&_nc_ht=scontent-fra3-1.cdninstagram.com&edm=AL-3X8kEAAAA&oh=00_AfBDCMhfnmpxuaDU8ZmGX72TEBPYihFRbkQ-VEXmUxMe6g&oe=65C90A21',
      'https://www.instagram.com/p/C0RUCFkokr7/',
      'بنك أبوظبي التجاري يحتفي بذكرى يوم الشهيد بحضور الرئيس التنفيذي لمجموعة بنك أبوظبي التجاري ومجموعة من موظفي البنك',
      11473971231,
      'adcb',
      'ADCB بنك أبوظبي التجاري',
      'نرحب بكم في الحساب الرسمي لبنك أبوظبي التجاري\nWelcome to Abu Dhabi Commercial Bank’s official Instagram account',
      'https://scontent-fra3-2.xx.fbcdn.net/v/t51.2885-15/411802562_1088489768992873_5827031017296475604_n.jpg?_nc_cat=1&ccb=1-7&_nc_sid=7d201b&_nc_ohc=G5Rxp7ry0SUAX-0Ynj2&_nc_ht=scontent-fra3-2.xx&edm=AL-3X8kEAAAA&oh=00_AfDs_MD8MSGyk3xwUKuLr3nmlm8WVn1GuOP5iETJkHanWg&oe=65C9ACA1',
      'https://adcb.com/',
      '2023',
      '2023',
      '2023',
      '2023|11',
      '11',
      '2023|48',
      '2023|48',
      '48',
      '48',
      '30',
      '4 Thursday',
      '4 Thursday',
      '2023-11-30',
      '2024-02-08',
      351,
      1,
      1,
      1,
      351
    ],
    [
      'Instagram Public Data',
      '18039638521528026',
      '2023-11-30 11:38:17',
      'VIDEO',
      'https://scontent-fra3-2.cdninstagram.com/o1/v/t16/f1/m82/484A0E9E1D6518316443D891A01F3DA4_video_dashinit.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6InZ0c192b2RfdXJsZ2VuLmNsaXBzLnVua25vd24tQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSJ9&_nc_ht=scontent-fra3-2.cdninstagram.com&_nc_cat=111&vs=748045320675647_2297884393&_nc_vs=HBksFQIYT2lnX3hwdl9yZWVsc19wZXJtYW5lbnRfcHJvZC80ODRBMEU5RTFENjUxODMxNjQ0M0Q4OTFBMDFGM0RBNF92aWRlb19kYXNoaW5pdC5tcDQVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dLaUNEeGljUC1JaXNLMEdBSHhtbldWZEh1ZzVicV9FQUFBRhUCAsgBACgAGAAbAYgHdXNlX29pbAExFQAAJo786ajihoBAFQIoAkMzLBdAJvXCj1wo9hgSZGFzaF9iYXNlbGluZV8xX3YxEQB1AAA%3D&ccb=9-4&oh=00_AfA0TWY6u-JKOo6yKQxKSK3X3-5y0NRV9gwo1o4CIj3HXg&oe=65C673F6&_nc_sid=1d576d&_nc_rid=7b381c3d34',
      'https://www.instagram.com/reel/C0QxYpJIB92/',
      '\u200eشهداؤنا الأبرار بذلوا أرواحهم فداء لتراب الوطن. لنقف جميعاً إعتزازا و فخرا بتضحياتهم. #نفخر_بتضحياتكم\n \nToday we pause to remember, with solemn respect, those who have fallen so we can stand tall. #Proud_of_your_sacrifices \n \n#UAE #الإمارات\n#adcb #بنك_ابوظبي_التجاري',
      11473971231,
      'adcb',
      'ADCB بنك أبوظبي التجاري',
      'نرحب بكم في الحساب الرسمي لبنك أبوظبي التجاري\nWelcome to Abu Dhabi Commercial Bank’s official Instagram account',
      'https://scontent-fra3-2.xx.fbcdn.net/v/t51.2885-15/411802562_1088489768992873_5827031017296475604_n.jpg?_nc_cat=1&ccb=1-7&_nc_sid=7d201b&_nc_ohc=G5Rxp7ry0SUAX-0Ynj2&_nc_ht=scontent-fra3-2.xx&edm=AL-3X8kEAAAA&oh=00_AfDs_MD8MSGyk3xwUKuLr3nmlm8WVn1GuOP5iETJkHanWg&oe=65C9ACA1',
      'https://adcb.com/',
      '2023',
      '2023',
      '2023',
      '2023|11',
      '11',
      '2023|48',
      '2023|48',
      '48',
      '48',
      '30',
      '4 Thursday',
      '4 Thursday',
      '2023-11-30',
      '2024-02-08',
      58,
      3,
      1,
      3,
      58
    ]
  ]
}
