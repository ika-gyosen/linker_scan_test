# -*- coding: utf-8 -*-

import json
import glob
import os
import shutil

linker_extensions_name = 'ld'
copy_dir_name = 'linker_scan_result'

# path + filename にフォルダを作成します。フォルダが存在した場合はスルーされます。


def make_dir(path, filename):
    os.makedirs(path + filename.replace("/", "／"), exist_ok=True)

# copy_fromから./copy_dir_name/フォルダへファイルをコピーします。もし同名のファイルが存在した場合コピーされません。


def copy_file(copy_from):
    copy_to = './' + copy_dir_name + '/' + os.path.basename(copy_from)
    if (os.path.exists(copy_to)) != True:  # ファイル名重複チェック
        shutil.copy2(copy_from, copy_to)
        return True
    else:
        return False


# このプログラムが実行されたディレクトリから下にある*.ldという名前のファイルをすべて検索し、
# 重複しないように./copy_dir_name/へコピーします。
if __name__ == "__main__":
    file_names = [p for p in glob.glob(
        './**/**.' + linker_extensions_name, recursive=True) if os.path.isfile(p)]  # .ldを検索し、ファイルならリストへ追加
    count = 0
    make_dir('./', copy_dir_name)  # 保存先が存在しなければ作成
    for names in file_names:
        if copy_file(names) == True:  # コピー実行し、重複せずコピーが実行された場合はパスをprint
            count = count + 1
            print(count, names)
    print('end')

# memo
# Python 3.7.2
# たぶん再帰的に動いてしまったときおかしなことになる。
