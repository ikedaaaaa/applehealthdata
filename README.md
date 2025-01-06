# applehealthdata
Extract Data from Apple Health App's XML Export
https://github.com/tdda/applehealthdata
からプログラムを拝借

# Dockerの実行方法
## 1. コンテナを作成する．
``` bash
# ymlやdockerfileを編集したから，buildしないとダメな場合
docker compose -f compose.yml up --build -d

# buildをしなくてもいい場合
docker compose -f compose.yml up  -d
```

## 2. コンテナ内に入る．
``` bash
docker exec -it applehealthdata bash
```

## 3. プログラムを実行する
```bash
# ヘルスケアアプリで生成した**.xmlファイルを指定する．その際，任意のディレクトリに入れておく．
# 任意のディレクトリにワークアウト毎の心拍csvがsplit_heartrateに出力される
python main.py data/2025**/**.xml
```

## 3. コンテナを壊す
``` bash
docker compose -f compose.yml down   
```