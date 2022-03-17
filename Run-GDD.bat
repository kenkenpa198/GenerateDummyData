:: ===== 設定 =====
:: 標準出力へコマンドを表示しない
@echo off
:: カレントディレクトリを再設定
cd /d %~dp0
:: 環境変数をローカル化
setlocal
:: CMD へ表示する文字コードを UTF-8 に設定
chcp 65001


:: ===== メイン処理 =====
echo GenerateDummyData.py を実行します。
python GenerateDummyData.py
echo 終了するには何らかのキーを押してください。
pause