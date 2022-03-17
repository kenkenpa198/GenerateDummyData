'''''''''''''''''''''''''''''''''''''''
GenerateDummyData.py / メイン処理

'''''''''''''''''''''''''''''''''''''''

import settings as st
import utils as ut

print('\n')
print('===========================')
print('    Generate Dummy Data    ')
print('===========================')

try:

    # 設定の表示
    print('\n▼ 生成設定一覧')
    print('----------------------------------------------------------\n')

    print(f'総行数設定     : {st.TOTAL_ROWS_NUM}')
    print(f'ヘッダーの設定 : {st.HEADER}')
    print(f'値の設定       : {st.DATA_COLUMNS}')
    print(f'値の言語設定   : {st.LANGUAGE}')

    print('\n----------------------------------------------------------')

    print('\n上記の設定でダミーデータを生成します。')
    print('問題なければ Enter キーを送信してください。')

    print('\n[!] 生成する総行数が多すぎると完了まで時間がかかる場合があります。')
    input('    処理の途中で中断する場合は Ctrl + C キー を押してください。\n')

    # CSV の出力先ファイルパスを設定
    # python の実行ファイルと同階層の export フォルダへ出力する
    export_file_path = ut.make_export_file_path(ut.make_export_dir_path())

    # ダミーデータを生成
    raw = ut.generate_dummy_raw()

    print('\n----------------------------------------------------------\n')
    print(raw)
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