'''''''''''''''''''''''''''''''''''''''''''''
archive.py / アーカイブ

作ったけどメインの構成では使わなかった関数や設定値。
今後使うかもなのでアーカイブとして残している。

'''''''''''''''''''''''''''''''''''''''''''''

import random
import string

import pandas as pd

import utils

'''
■ 範囲指定した日付と時間を pandas.date_range で生成

NOTE:
periods に生成する数、freq に加算する箇所（月だったら 'm', 時間だったら 'h'）を指定。
色々柔軟に対応できるみたい。

Faker だとランダムに生成してしまうので、連続する日時を出力したい際に使えそう？

参考: http://ailaby.com/date_range/
'''
date_index = pd.date_range('2020-01-25 02:00:00', periods=100, freq='h')


'''
■ 引数で与えた桁数のランダムな文字列を生成する関数

NOTE:
桁数指定で半角英数字のランダムな文字列を返す。
'''
def random_name(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)


'''
■ 0 埋めの文字列を生成する関数

NOTE:
char に指定した文字列（※ int の場合は str() で変換が必要）に対して
digits に指定された桁数分の 0 埋め文字列を返す。

例）
>>> text = gen_zfill(1, 4)
>>> print(text)
0001

テストケースの連番割り振りに使えそう。
'''
def gen_zfill(char, digits):
    return char.zfill(digits)



'''
■ テストデータ生成処理

NOTE:
テストデータ自動生成処理の初期案の残骸。

設定用ファイルで生成する値の範囲などを簡単に変更できるようにしたかったけど、
設定用ファイルそのものが複雑になりそうだったのでやめた。
'''
# 多次元リスト用のリストを定義
rows = []

# 生成
for i in range(50):

    row = []
    fill_num = utils.gen_zfill(str(i + 1), setup.ID_ZERO_FILL)

    # ID を生成
    row.append(f'{setup.ID_BEGIN_CHAR}{fill_num}')

    # 名前を生成
    row.append(f'テスト{fill_num}さん')

    # 名前を生成（フラグが True / False でエイリアスの有り無しを決める
    if setup.EMAIL_ALIAS_FLAG:
        row.append(f'{setup.EMAIL_USER}+{fill_num}{setup.EMAIL_DOMAIN}')
    else:
        row.append(f'{setup.EMAIL_USER}{setup.EMAIL_DOMAIN}')

    # 時間日時を生成
    rows.append(row)
