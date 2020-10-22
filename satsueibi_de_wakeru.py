﻿'''
指定ディレクトリ内のファイルを作成日時毎にフォルダ分けする
---------------------------------------------------
第1引数: ディレクトリパス
第2引数: 拡張子['.'無しで]
'''

import os
import sys
import datetime
import glob
import shutil
import add_satsueibi as hiduke


# 日付ディレクトリ内のファイル名の通し番号の末尾を返す
# -----------------------------------------------------------------------
def getLastNumber(dir_path, ext):
    file_filter = '*.' + ext
    file_filter = os.path.join(dir_path, file_filter)
    file_list = glob.glob(file_filter)
    num = 0
    max_num = 0    
    for file_path in file_list:
        b_name = os.path.splitext(os.path.basename(file_path))[0]
        num_str = b_name.split('_')[1]
        num = int(num_str)
        if num >= max_num:
            max_num = num
    return max_num

'''
def get_exif(image_path):
    captured_datetime = None
    with Image.open(image_path) as imgfh:
        try:
            exif = imgfh._getexif()
            for attr, val in exif.items():
                tag = ExifTags.TAGS.get(attr, attr)
                if tag == 'DateTimeOriginal':
                    captured_datetime = val
        except AttributeError:
            pass
    return captured_datetime
'''

# メインシーケンス
# -----------------------------------------------------------------------
if __name__ == '__main__':
    args = sys.argv
    dir_path = args[1]
    ext = args[2]

    fil = dir_path
    if ext == 'all':
        fil += '/*'
    else:
        fil += '/*.'
        fil += ext

    f_list = glob.glob(fil)

    # ファイルをひとつずつチェックする
    print('Rename: ')
    for f_path in f_list:
        # "f_path"がディレクトリパスならスキップ
        if os.path.isdir(f_path):
            continue

        # ファイルの最終更新日を取得する
        dt = datetime.datetime.strptime(hiduke.get_exif(f_path), '%Y:%m:%d %H:%M:%S')
        
#        dt = hiduke.get_exif(f_path)

        # 日付を文字列に変換する
        dt_str = dt.strftime('%Y%m%d')

        # 日付ディレクトリパスを生成する
        dt_dir_path = dir_path + '/' + dt_str
        # 日付ディレクトリが存在しないなら、新規作成する
        if not os.path.exists(dt_dir_path):
            os.mkdir(dt_dir_path)

        # 日付フォルダへ振り分ける処理
        # ----------------------------------------------------------------------
        # 拡張子('.'無し)の文字列を取り出す
        ext_str = os.path.splitext(os.path.basename(f_path))[1][1:]
        # 日付ディレクトリに格納されているファイルの通し番号の最後の値を取得する
        last_num = getLastNumber(dt_dir_path, ext_str)
        # 新規の番号はその次の値
        last_num += 1

        # 日付ディレクトリへ格納後、ファイル名を"日付+通し番号"に変更する
        # ますはファイル名の生成
        new_name = dt_str + '_'
        new_name += '{:0=4}'.format(last_num)
        new_name += os.path.splitext(os.path.basename(f_path))[1]

        # 日付ディレクトリへファイルを移動する
        shutil.move(f_path, os.path.join(dt_dir_path, new_name))

        # 結果をコンソール画面へ出力
        # ----------------------------------------------------------------------
        name_1 = os.path.basename(f_path)
        name_2 = new_name
        print('> ' + name_1 + ' -> ' + name_2)
        print('> moved to ' + dt_dir_path)

