function arrayToCSV(arr) {
    const array = [Object.keys(arr[0])].concat(arr)
    return array.map(row => {
        return Object.values(row).map(value => {
            return typeof value === 'string' ? JSON.stringify(value) : value
        }).toString()
    }).join('\n')
 }
 
 
 
 
 let temp = db.getCollection("youtube_brand_video_data_20231211").aggregate([
    {
        $lookup: {
            from: "yt_brand_20231211",
            localField: "channel_id",
            foreignField: "channel_id",
            as: "channel_data"
        }
    },
    {
        $unwind: "$channel_data"
    },
    {
        $project: {
            _id: 0,
            channel_id: "$channel_id",
            video_title: "$title",
            video_description: "$description",
            video_id: "$video_id",
            video_published_at: "$published_at",
            video_view_count: "$view_count",
            video_like_count: "$like_count",
            video_favorite_count: "$favorite_count",
            video_comment_count: "$comment_count",
            channel_brand_name: '$channel_data.brand',
            channel_username: "$channel_data.channel_username",
            channel_total_view_count: "$channel_data.total_view_count",
            channel_total_subscriber_count: "$channel_data.total_subscriber_count",
            channel_total_video_count: "$channel_data.total_video_count"
        }
    }
 ]);
 
 
 final_data = new Array()
 temp.forEach(function (i) {
    let hashtags = i['video_description'].match(/#[a-z]+/gi);
    if (hashtags)
        hashtags.push(i['video_title'].match(/#[a-z]+/gi));
    else
        hashtags = i['video_title'].match(/#[a-z]+/gi);
    if (hashtags)
        i['hashtags'] = hashtags.join(',');
    else
        i['hashtags'] = null;
 
 
    final_data.push(i)
 });
 
 
 db.report.insertMany(final_data)