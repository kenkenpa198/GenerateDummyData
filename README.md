<!-- omit in toc -->
# Generate Dummy Data

ランダムなダミーデータを生成して CSV として出力するツールです。

## 1. 導入方法・使い方

1. zip ファイルを展開して PowerShell でディレクトリを開く。
2. `pip install -r requirements.txt` を送信して必要モジュールをインストールする。
3. ディレクトリ直下の settings.py を開き、コメントを参考に設定して保存する。
4. `python3 GenerateDummyCSV.py` を送信するか、run-GDD.bat を実行する。
5. 当ツールが起動するので画面のとおりに進める。
6. GenerateDummyCSV.py と同階層の export フォルダに CSV として生成される。

## 2. 利用ソフトウェア

- [Python](https://www.python.org/)
- [joke2k/faker](https://github.com/joke2k/faker/blob/master/docs/index.rst)

## 3. 参考情報

- [Welcome to Faker's documentation! — Faker 13.3.2 documentation](https://faker.readthedocs.io/en/master/index.html)
- [Pythonでそれっぽいテストデータを作成する(前編) - Qiita](https://qiita.com/nandymak/items/1ab36e3d5365e8ca2942)
- [PythonにてFakerを用いてランダムなテストデータを生成する方法 - N-blog 09](https://www.nblog09.com/w/2019/01/24/python-faker/)
- [【Python】CSVファイルのダミーデータを作成する方法](https://gist.github.com/kurozumi/4642d8a70440c57a2719c0e5c02013c5)
- [[Laravel5.1]Fakerチートシート - Qiita](https://qiita.com/tosite0345/items/1d47961947a6770053af)
