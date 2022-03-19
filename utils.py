'''''''''''''''''''''''''''''''''''''''
utils.py / 自作モジュール

'''''''''''''''''''''''''''''''''''''''
import datetime
import os
from pprint import pprint

from faker.factory import Factory

import settings as st


'''
■ 生成設定をプリントする関数
'''
def print_settings():
    print('\n▼ 生成設定')
    print('----------------------------------------------------------')

    print(f'生成行数       : {st.GENERATE_ROWS_NUM} 行')
    print(f'値の言語設定   : {st.LANGUAGE}')

    seed_setting = st.SEED if st.SEED else '設定なし'
    print(f'シード値の設定 : {seed_setting}')

    print('----------------------------------------------------------')

    print(f'\n▼生成するダミーデータの設定')
    print('----------------------------------------------------------')

    pprint(st.GENERATE_DATA_DICT, sort_dicts=False)

    print('----------------------------------------------------------')


'''
■ 生成結果プレビューをプリントする関数
'''
def print_relust(raw):
    raw_list = raw.splitlines()

    print('\n▼ 生成結果プレビュー')
    print('----------------------------------------------------------')

    # 7行（6行生成）を超過している場合は最初と最後の3行分のみ出力
    if len(raw_list) > 7:
        print(raw_list[0]) # ヘッダー
        print(raw_list[1])
        print(raw_list[2])
        print(raw_list[3])
        print('\n...\n')
        print(raw_list[-3])
        print(raw_list[-2])
        print(raw_list[-1])
    else:
        print(raw.rstrip())

    print('----------------------------------------------------------\n')


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

    # クラスと関数を変数へ格納
    Faker = Factory.create
    fake = Faker()

    # setting.py へ SEED の設定がされていればシード値を設定する
    if st.SEED:
        fake.seed(st.SEED)

    # ダミーデータのローカライズを設定
    fake = Faker(st.LANGUAGE)

    # ダミーデータ辞書のキーと値をヘッダーのリストと値のリストに変換
    header = list(st.GENERATE_DATA_DICT.keys())
    data_columns = list(st.GENERATE_DATA_DICT.values())

    # ダミーデータの raw テキストを生成
    raw_text = fake.csv(
        header=header,                 # ヘッダー設定を読み込み
        data_columns=data_columns,     # 値のオプション設定を読み込み
        num_rows=st.GENERATE_ROWS_NUM, # 生成行数設定を読み込み
        include_row_ids=False          # 重複を許可しない設定（たぶん…）
    )

    return raw_text
