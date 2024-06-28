# ディレクトリ構成図
## ツリー
`__pycache__`など自動で作成されるものは除外
```
.
├── api # apiのファイル
│   ├── migrations # migrationファイル
│   │   └── versions # alembicを使って作成されたマイグレーションファイル
│   ├── src
│   │   ├── models # sqlalchemyのモデル
│   │   ├── repositories # modelを使ってDBから値を取得したり保存したりする
│   │   ├── routers # ルーティングファイル
│   │   ├── schemas # リクエスト/レスポンススキーマ
│   │   └── usecases # ロジックを記載する
│   └── test
├── documents # ドキュメントいれば
└── mysql # mysqlコンテナで必要なものが入る
```
