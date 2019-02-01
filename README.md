## jieba-seg-api-heroku
將jieba部署到heroku上，實現斷詞API

### 部署指令
先確認有設置好heroku
```
git clone https://github.com/marvincwhuang/jieba-seg-api-heroku.git
cd jieba-seg-api-heroku 
heroku create
git push heroku master
```
### Example 
```
https://intense-coast-89223.herokuapp.com/seg?q=將jieba部署到heroku上，實現斷詞API
```
```
{
  resCode: 0,
  resMsg: "ok",
  resData: [
    "將",
    "jieba",
    "部署",
    "到",
    "heroku",
    "上",
    "，",
    "實現",
    "斷詞",
    "API"
  ]
}
```
