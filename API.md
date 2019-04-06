# API

## `GET /api`

### A successful request
```bash
# request
curl --request GET \
    --url http://localhost:5000/api \
    --data '{
        "url": "https://www.pixiv.net/member_illust.php?mode=medium&illust_id=51145109"
    }'

# response
{
    "payload": {
        "digest": "",
        "images": [
            "https://i.pximg.net/c/600x600/img-master/img/2015/06/29/00/33/53/51145109_p0_master1200.jpg"
        ],
        "title": "\u3010\u30e9\u30d6\u30e9\u30a4\u30d6!\u3011\u300c\u7121\u984c\u300d/\u300cRio.LW\u300d\u306e\u30a4\u30e9\u30b9\u30c8 [pixiv]"
    },
    "status": "ok"
}
```

### A failed request
```bash
# request
curl --request GET \
    --url http://localhost:5000/api \
    --data '{
        "url": "foobar"
    }'

# response
{
    "error_message": "some error message",
    "status": "error"
}
```
