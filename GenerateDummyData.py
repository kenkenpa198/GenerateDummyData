'''''''''''''''''''''''''''''''''''''''
GenerateDummyData.py / メイン処理

'''''''''''''''''''''''''''''''''''''''

import utils as ut

print('\n')
print('===========================')
print('    Generate Dummy Data    ')
print('===========================')

try:
    print('\nEnter キーを送信するとダミーデータを作成します。')

    print('\n[!] 生成する総行数が多すぎると完了まで時間がかかる場合があります。')
    input('    処理の途中で中断する場合は Ctrl + C キー を押してください。')

    # CSV の出力先ファイルパスを設定
    # python の実行ファイルと同階層の export フォルダへ出力する
    export_file_path = ut.make_export_file_path(ut.make_export_dir_path())

    # ダミーデータを生成
    raw = ut.generate_dummy_raw()
    print(raw)

    # CSV ファイルとして出力
    with open(export_file_path, 'w', newline='', encoding='utf-8') as f:
        f.write(raw)

    print('ダミーデータを生成しました。')
    print('CSV ファイルを以下へ出力しました。')
    print(export_file_path)

except KeyboardInterrupt as e:
    print('\nキーボード入力により処理を中断しました。')

print('\nGenerate Dummy Data を終了します。\n')