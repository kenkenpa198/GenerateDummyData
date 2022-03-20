'''''''''''''''''''''''''''''''''''''''
GenerateDummyData.py / メイン処理

'''''''''''''''''''''''''''''''''''''''
import utils as ut

print('')
print('=========================')
print('   Generate Dummy Data   ')
print('=========================')

try:
    # 設定ファイルから設定値を読み込んでタプルとして格納
    setting_tuple = ut.import_json('settings/sample.json')

    # 生成設定をプリント
    ut.print_settings(*setting_tuple)

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
    raw = ut.generate_dummy_data_raw(*setting_tuple)

    # 生成結果プレビューをプリント
    ut.print_relust(raw)

    # CSV ファイルとして出力
    with open(export_file_path, 'w', newline='', encoding='utf-8') as f:
        f.write(raw)

    print('ダミーデータを生成しました。')
    print('CSV ファイルを以下へ出力しました。')
    print(export_file_path)

except KeyboardInterrupt as e:
    print('\nキーボード入力により処理を中断しました。')

print('\nGenerate Dummy Data を終了します。\n')