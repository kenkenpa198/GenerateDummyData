'''''''''''''''''''''''''''''''''''''''
utils.py / 自作モジュール

'''''''''''''''''''''''''''''''''''''''
import datetime
import os

from faker.factory import Factory

import settings as st


'''
■ 出力先のディレクトリを作成する関数

デフォルトだと Python の実行ファイルと同じ階層の export ディレクトリへ出力する。
保存先となるディレクトリパスも返す。

'''
def make_export_dir_path(parent_dir_path=os.path.dirname(os.path.abspath(__file__)), dir_name="export"):

    # ディレクトリパスの作成
    export_dir_path = os.path.join(parent_dir_path, dir_name)

    # ディレクトリを作成（既に存在したら何もしない）
    os.makedirs(export_dir_path, exist_ok=True)

    return export_dir_path


'''
■ 出力先のファイルパスを作成する関数

指定ディレクトリ/result_YYYYMMDDhhmmss.csv の形で返す。

'''
def make_export_file_path(export_dir_path):

    # ファイル名の作成
    dt_now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')  # 現在の日時を取得
    filename = f'result_{dt_now}.csv'                          # ファイル名を設定

    # ファイルパスの作成
    export_file_path = os.path.join(export_dir_path, filename) # ディレクトリパスとファイル名を結合

    return export_file_path


'''
■ ダミーデータの CSV を出力する関数

外部モジュールの Faker を使ってダミーデータを生成する。
settings.py で設定した情報を基にする。

CSV 形式のテキストが返されるので、これをそのままテキストに書き込めば OK 。

参考:
Pythonでそれっぽいテストデータを作成する(前編)
https://qiita.com/nandymak/items/1ab36e3d5365e8ca2942

PythonにてFakerを用いてランダムなテストデータを生成する方法 - N-blog 09
https://www.nblog09.com/w/2019/01/24/python-faker/

Faker の公式リファレンス
https://faker.readthedocs.io/en/master/index.html
https://faker.readthedocs.io/en/master/providers/faker.providers.misc.html?highlight=csv#faker.providers.misc.Provider.csv

'''
def generate_dummy_raw():

    # クラス指定の短縮など
    Faker = Factory.create
    fake = Faker()
    # fake.seed(0)            # シード値をここで指定すると生成されるデータを固定できる
    fake = Faker(st.LANGUAGE) # ダミーデータのローカライズを設定

    # CSV 形式でダミーデータの raw テキストを生成する
    raw_text = fake.csv(
        header=st.HEADER,             # ヘッダー設定を読み込み
        data_columns=st.DATA_COLUMNS, # 値設定を読み込み
        num_rows=st.TOTAL_ROWS_NUM,   # 総行数設定を読み込み
        include_row_ids=False,        # 重複を許可しない設定（たぶん…）
    )

    return raw_text
