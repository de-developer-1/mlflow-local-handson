# mlflow-local-handson

このリポジトリは、ローカル環境で Delta Lake + MLflow を連携させた機械学習ワークフローのハンズオン用テンプレートです。

## 構成

- `docker/`: JupyterLab および MLflow サーバーの Dockerfile と docker-compose 設定
- `notebooks/`: データ準備、モデル学習、推論の Jupyter Notebook
- `scripts/`: サンプルデータ生成スクリプト
- `data/raw/`: CSV形式のサンプルデータ
- `data/delta/`: Delta Lake 形式のデータ保存先
- `mlruns/`: MLflow のローカル実験ログ保存先

## 起動方法

```bash
cd docker
docker-compose up --build
```

## Jupyter アクセス

- URL: http://localhost:8888/lab

## MLflow UI アクセス

- URL: http://localhost:5000

## 備考

- モデル推論ノートブック内の `<run_id>` は、MLflow UI から実行IDを取得して差し替えてください。
