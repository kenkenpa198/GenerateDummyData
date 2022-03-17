<!-- omit in toc -->
# Generate Dummy Data

![kv](images/kv.jpg)

Generate Dummy Data は、ランダムなダミーデータを生成して CSV として出力するツールです。

## 1. 導入方法

Python の動作環境が無い場合は、先に下記のサイト様を参考にインストールしてください。  
[Python のインストール方法 - Windows - Python の準備 - やさしい Python 入門](https://python.softmoco.com/devenv/how-to-install-python-windows.php)

Python をインストールしたら、当ツールの zip ファイルを好きなディレクトリに展開してください。  
その後下記の手順で必要モジュールをインストールしてください。

1. ツールを展開したディレクトリをエクスプローラーで開く。
2. `Shift` キーを押しながら右クリック > `PowerShell ウィンドウをここで開く(S)` を選択する。
3. PowerShell が起動する。
4. `pip install -r requirements.txt` を送信して必要モジュールをインストールする。
5. インストールが完了したら、次項の使い方を参考に動作確認する。

## 2. 使い方

1. 展開したディレクトリ直下の `settings.py` をテキストエディタで開き、コメントを参考に設定して保存する（そのままでも OK です）。
2. 下記のいずれかの方法でツールを実行する。
   1. コンソール上で `python GenerateDummyData.py` を送信する。
   2. ディレクトリ直下の `Run-GDD.bat` をダブルクリックで実行する。
3. ツールが起動するので画面のとおりに進める。
4. `GenerateDummyData.py` と同階層の `export` フォルダへ CSV ファイルとして生成される。

## 3. オプション情報

`setting.py` > `DATA_COLUMNS` へ設定するダミーデータのオプションに関する情報を掲載しています。  
オプションは 200 個以上あるようなので、自由度はかなり高そうです。

### 3.1. オプション一覧（ピックアップ）

特に使いやすそうなものを公式リファレンスの中からピックアップしています（名前順）。  
\* 印が付いているオプションは初期値で設定しているものです。

オプション   | 説明                                                        | 生成例（日本語設定）
------------ | ----------------------------------------------------------- | ----------------------------------------
address      | 住所。リアルっぽすぎるので「テスト」を結合した方がいいかも。| 高知県稲城市月島40丁目13番6号 花島コーポ615
\* boolean   | ブール値。True / False のどちらかが生成されます。           | True
color        | カラーコード（#FFFFFF 形式）。                              | #79c3e0
color_name   | カラーコード（色名）。色系は他にも hex_color（HEX 値で生成）などいろいろあるようです。 | HotPink
\* date      | 日付（YYYY-MM-DD 形式） 。                                  | 2014-11-17
\* date_time | 日付時刻（YYYY-MM-DD hh:mm:ss 形式）。                      | 1993-02-19 01:48:57
\* email     | Email アドレス。ドメインはすべて example.xxx になります。   | zyoshidaexample.com
file_path    | ファイルパス。日本語設定だと無駄に日本語化されてしまうようなので、後述の言語設定を切り替えた方が使いやすそう。 | /状況/スマッシュ.webm
first_name   | 下の名前。name 系には他にもカタカナ版、英語版、男性っぽい / 女性っぽい などいろいろあるようです。 | 亮介
image_url    | 画像 URL 。実際に遷移できるようです。                       | [https://placekitten.com/680/409](https://placekitten.com/680/409)
job          | 職業。                                                      | 野球
\* name      | 人名。苗字と名前の間に半スぺが入ります。                    | 伊藤 太郎
phone_number | 電話番号。                                                  | 090-9657-4596
port_number  | ポート番号。ランダムな数値文字列としても使えそう？          | 21188
text         | 文章っぽい文字列。全体は 180 字前後で、改行（CRLF）を 4 個程度含みます。 | 明らかにする省略ホイールコーラス画面（省略）見落とすリハビリ。
time         | 時間（hh:mm:ss 形式）。                                     | 01:48:57
\* user_name | ユーザー名。ローマ字 + 時々数字で生成されます。             | manabu23
\* uuid4     | UUID 。ほぼ必ず一意になる 32 桁分の値が生成されます。       | 362ed54b-584d-4f49-bf97-3ff670e79a23
\* word      | 適当な一単語。                                              | 野球

### 3.2. オプションの情報が掲載されているサイト

- [[Laravel5.1]Fakerチートシート - Qiita](https://qiita.com/tosite0345/items/1d47961947a6770053af)
  - オプションが日本語でまとまっている記事。
  - ただし Python 版用では無いので、パスカルケースのものはそのままだと動かきません。
  - パスカルケースをスネークケースに変更すれば動くみたいです（UUID など一部を除く）。  
  例）DateTime ⇒ date_time

- [Faker 公式リファレンス > 標準のオプションリスト](https://faker.readthedocs.io/en/master/providers.html)
  - 公式の標準オプションリスト。カテゴリごとに各ページへ分かれています。
  - 名前系から MAC アドレスまで、かなり幅も広いようです。

- [Faker 公式リファレンス > 日本語対応のオプションリスト](https://faker.readthedocs.io/en/master/locales/ja_JP.html)
  - 言語設定を日本語にした際に、オプションごとにどう表示が変わるかまで掲載されているリストです。
  - ただし中途半端にしか掲載されていないようなので、前述の標準のオプションリストを確認する方がいいかも。

## 4. ライセンス

Generate Dummy Data は MIT ライセンスの下でリリースされています。  
ライセンス全文はディレクトリ直下の LICENSE ファイルをご確認ください。

## 5. クレジット

### 5.1. 利用ソフトウェア

- [Python](https://www.python.org/)
- [joke2k/faker](https://github.com/joke2k/faker)

### 5.2. 参考サイト様

- [Welcome to Faker's documentation! — Faker 13.3.2 documentation](https://faker.readthedocs.io/en/master/index.html)
- [Pythonでそれっぽいテストデータを作成する(前編) - Qiita](https://qiita.com/nandymak/items/1ab36e3d5365e8ca2942)
- [PythonにてFakerを用いてランダムなテストデータを生成する方法 - N-blog 09](https://www.nblog09.com/w/2019/01/24/python-faker/)
- [【Python】CSVファイルのダミーデータを作成する方法](https://gist.github.com/kurozumi/4642d8a70440c57a2719c0e5c02013c5)
- [[Laravel5.1]Fakerチートシート - Qiita](https://qiita.com/tosite0345/items/1d47961947a6770053af)
