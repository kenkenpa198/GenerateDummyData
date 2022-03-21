'''''''''''''''''''''''''''''''''''''''
GenerateDummyData.py / メイン処理

'''''''''''''''''''''''''''''''''''''''
import utils as ut

print('')
print('=========================')
print('    GenerateDummyData    ')
print('=========================')

try:
    # 設定ファイル用フォルダから設定ファイルのリストを取得
    print('\nsettings フォルダに格納されている JSON ファイルを表示します。\n')
    setting_file_path_list = ut.get_setting_file_path_list()

    # 表示したリストから設定ファイルの選択を要求しファイルパスを取得
    setting_file_path = ut.request_select_file_path_list(setting_file_path_list)

    # 設定ファイルから設定値を読み込んでそれぞれの設定値の変数へ格納
    generate_rows_num, faker_language, seed_value, remove_wqm, generate_data_dict = ut.import_json(setting_file_path)

    # 読み込んだ生成設定をプリント
    input(f'\n{setting_file_path} の読み込みに成功しました。\nEnter キーを押すと生成の設定を表示します。')
    ut.print_settings(generate_rows_num, faker_language, seed_value, remove_wqm, generate_data_dict)

    print('\n上記の設定でダミーデータを生成します。')
    print('問題なければ Enter キーを押してください。')

    print('\n[!] 生成する行数が多すぎると完了まで時間がかかる場合があります。')
    input('    処理の途中で中断する場合は Ctrl + C キーを押してください。')

    # CSV の出力先ファイルパスを設定
    # python の実行ファイルと同階層の export フォルダへ出力する
    export_file_path = ut.make_export_file_path(ut.make_export_dir_path())

    # ダミーデータを生成するメイン処理
    # 生成時間が長い場合に備えて生成中であることを示すテキストを表示
    print('\nダミーデータを生成しています……。')
    raw = ut.generate_dummy_data_raw(generate_rows_num, faker_language, seed_value, generate_data_dict)
    print('ダミーデータを生成していました。')

    # remove_wqm の設定が TRUE であれば " " の削除関数を実行する
    if remove_wqm:
        print('\n" " を生成しています……。')
        raw = ut.remove_wqm(raw)
        print('" " を削除しました。')

    # 生成結果プレビューをプリント
    ut.print_relust(raw)

    # CSV ファイルとして出力
    with open(export_file_path, 'w', newline='', encoding='utf-8') as f:
        f.write(raw)

    print('ダミーデータを生成しました。')
    print('CSV ファイルを以下へ出力しました。')
    print(export_file_path)

except KeyboardInterrupt:
    print('\nキーボード入力により処理を中断しました。')

print('\nGenerateDummyData を終了します。')
