FastAPI docker APIのサンプル
##　技術構成
---
・FastAPI
・SQLAlchemy
・MySQL
・Pydantic

## API
---
### トップ

|説明|メソッド|URI|
|----|----|----|
|確認用のエンドポイント。文字列を返す。|GET|/|

### タスク

|説明|メソッド|URI|
|----|----|----|
|全TODOデータを取得|GET|/tasks|
|TODOデータの新規作成。| POST|/tasks|
|指定したTODOデータの削除|DELETE|/task{id}|
|指定したTODOデータの更新|PATCH|/task{id}|



## 環境構築

- dockerを起動
```
docker compose up
```
- 自動的にuvicornが起動する。

- 以下のURLに接続しレスポンスを確認
 - http:127.0.0.1:8000/
