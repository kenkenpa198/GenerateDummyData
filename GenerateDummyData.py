'''''''''''''''''''''''''''''''''''''''
GenerateDummyData.py / メイン処理

'''''''''''''''''''''''''''''''''''''''

from pprint import pprint

import settings as st
import utils as ut

print('\n')
print('=========================')
print('   Generate Dummy Data   ')
print('=========================')

try:

    # 設定の表示
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




    print('\n上記の設定でダミーデータを生成します。')
    print('問題なければ Enter キーを送信してください。')

    print('\n[!] 生成する行数が多すぎると完了まで時間がかかる場合があります。')
    input('    処理の途中で中断する場合は Ctrl + C キーを押してください。')

    # CSV の出力先ファイルパスを設定
    # python の実行ファイルと同階層の export フォルダへ出力する
    export_file_path = ut.make_export_file_path(ut.make_export_dir_path())

    # 生成時間が長い場合に安心させるため生成中であることを示すテキストを表示
    print('\nダミーデータを生成しています……')

    # ダミーデータを生成
    raw = ut.generate_dummy_raw()
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

    # CSV ファイルとして出力
    with open(export_file_path, 'w', newline='', encoding='utf-8') as f:
        f.write(raw)

    print('ダミーデータを生成しました。')
    print('CSV ファイルを以下へ出力しました。')
    print(export_file_path)

except KeyboardInterrupt as e:
    print('\nキーボード入力により処理を中断しました。')

print('\nGenerate Dummy Data を終了します。\n')