'''''''''''''''''''''''''''''''''''''''
utils.py / 自作モジュール

'''''''''''''''''''''''''''''''''''''''
import datetime
import glob
import json
import os
from pprint import pprint
import sys

from faker.factory import Factory


'''
■ 設定ファイルパスのリストを取得する関数
'''
def get_setting_file_path_list():

    # 設定ファイル用ディレクトリ内のファイルパスのみを再帰的に取得しリスト化する
    setting_file_path_list = [p for p in glob.glob('settings/**/*.json', recursive=True)
       if os.path.isfile(p)]

    if setting_file_path_list:
        # 設定ファイルパスのリストを昇順に並び替えて返す
        setting_file_path_list.sort()
        return setting_file_path_list

    else:
        print('\n[!] 設定ファイルのリストを取得できませんでした。')
        print('    GenerateDummyData.py と同階層に settings フォルダがあることや\n    settings フォルダの中に JSON ファイルが存在することを確認してください。')
        print('\nツールの実行を終了します。')
        sys.exit()



'''
■ 設定ファイルパスリストの情報を表示して選択を要求する関数
'''
def request_select_file_path_list(setting_file_path_list):

    try:
        # 設定ファイルパスリストを INDEX 番号と共にプリント
        index_num = 0
        for fp in setting_file_path_list:
            print(f'{index_num} : {fp}')
            index_num += 1

        # 入力を要求する
        selected_index_num = int(input('\n読み込みたい設定ファイルに表示されている INDEX 番号を入力してください: '))

        # 入力された INDEX 番号からファイルパスを取得して変数へ格納
        selected_setting_file_path = setting_file_path_list[selected_index_num]

    # TODO: 例外があった場合は終了するのではなく繰り返し要求するようにする

    # 例外処理: 値エラーをキャッチしたとき
    except ValueError as e:
        print('\n[!] 値エラーを検知しました。入力した値が半角の数値であるか確認してください。')
        print(f'    ValueError: {e}')
        print('\nツールの実行を終了します。')
        sys.exit()

    # 例外処理: INDEX エラーをキャッチしたとき
    except IndexError as e:
        print('\n[!] INDEX エラーを検知しました。入力した値がリストに表示されている数値だったか確認してください。')
        print(f'    IndexError: {e}')
        print('\nツールの実行を終了します。')
        sys.exit()

    # 例外が発生しなければ入力されたファイルパスを返す
    else:
        # 情報を表示する
        print('\n以下のファイルを読み込みます。問題なければ Enter キーを押してください。')
        print(selected_setting_file_path)
        input()

        # 設定ファイルパスを返す
        return selected_setting_file_path



'''
■ 設定用の JSON ファイルを読み込む関数

下記の設定値をタプルとして返す。

- generate_rows_num（生成行数設定）
- faker_language（言語設定）
- seed_value（シード値設定）
- generate_dummy_data_dict（ダミーデータ生成用辞書設定）

'''
def import_json(json_file_path):

    try:
        # 引数で渡された設定用の JSON ファイルを読み込み
        with open(json_file_path, 'r', encoding='utf-8') as f:
            json_dict = json.load(f)

        # 読み込んだ設定を変数と辞書へ格納
        generate_rows_num        = json_dict["generate_rows_num"]
        faker_language           = json_dict["faker_language"]
        seed_value               = json_dict["seed_value"]
        generate_dummy_data_dict = json_dict["generate_dummy_data_dict"]

    # 例外処理: JSON のデコードエラーをキャッチしたとき
    except json.decoder.JSONDecodeError as e:
        print('[!] JSON 情報のデコードに失敗しました。JSON ファイルの記述に問題がないか確認してください。')
        print(f'    json.decoder.JSONDecodeError: {e}')
        print('\nツールの実行を終了します。')
        sys.exit()

    # 例外処理: 存在しない辞書のキーを参照しているエラーをキャッチしたとき
    except KeyError as e:
        print('[!] 設定値の取得に失敗しました。下記に表示されている設定値の記述に問題がないか確認してください。')
        print(f'    KeyError: {e}')
        print('\nツールの実行を終了します。')
        sys.exit()

    # 例外が発生しなければ設定値を返す
    else:

        print('設定情報の読み込みに成功しました。')

        return (
            generate_rows_num,
            faker_language,
            seed_value,
            generate_dummy_data_dict
        )



'''
■ 生成設定をプリントする関数
'''
def print_settings(generate_rows_num, faker_language, seed_value, generate_data_dict):

    input('Enter キーを押すと生成の設定を表示します。')

    print('\n▼ 生成時の設定')
    print('----------------------------------------------------------')

    print(f'生成行数       : {generate_rows_num} 行')
    print(f'値の言語設定   : {faker_language}')

    seed_setting = seed_value if seed_value else '設定なし'
    print(f'シード値の設定 : {seed_setting}')

    print('----------------------------------------------------------')

    print(f'\n▼ 生成するダミーデータの設定')
    print('----------------------------------------------------------')

    pprint(generate_data_dict, sort_dicts=False)

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

TODO: 設定が異常値などで関数の実行に失敗した際の例外処理を加える

'''
def generate_dummy_data_raw(generate_rows_num, faker_language, seed_value, generate_data_dict):

    # クラスと関数を変数へ格納
    Faker = Factory.create
    fake  = Faker()

    # setting.py へ SEED の設定がされていればシード値を設定する
    if seed_value:
        fake.seed(seed_value)

    # faker の言語を設定
    fake = Faker(faker_language)

    # ダミーデータ辞書のキーと値をヘッダーのリストと値のリストに変換
    header = list(generate_data_dict.keys())
    data_columns = list(generate_data_dict.values())

    # ダミーデータの raw テキストを生成
    raw_text = fake.csv(
        header=header,              # ヘッダー設定を読み込み
        data_columns=data_columns,  # 値のオプション設定を読み込み
        num_rows=generate_rows_num, # 生成行数設定を読み込み
        include_row_ids=False       # 重複を許可しない設定（たぶん…）
    )

    return raw_text
