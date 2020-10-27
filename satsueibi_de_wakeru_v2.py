'''
指定ディレクトリ内の写真を撮影日毎にフォルダ分けする(静止画専用)
---------------------------------------------------
第1引数: 写真が格納されているディレクトリパス
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

# メインシーケンス
# -----------------------------------------------------------------------

def satsueibi_de_wakeru_v2(dir_path):
    # このスクリプトで対応させる拡張子のリスト
    exts = ["jpg", "png", "bmp", "heic"]

    fil_base = dir_path + "/*."

    count_success = 0
    count_fail = 0
    
    # 拡張子毎に処理を行う
    for ext in exts:
        fil = fil_base + ext
        f_list = glob.glob(fil)

        # ファイルをひとつずつチェックする
        for f_path in f_list:
            # "f_path"がディレクトリパスならスキップ
            if os.path.isdir(f_path):
                continue

            # 写真の撮影日を取得する
            exif_str = hiduke.get_exif(f_path)        
            # 撮影日情報の無い画像については処理をスキップする
            if exif_str == None:
                err_txt = '> ERROR: "' + os.path.basename(f_path) + '" has no date data.'
                print(err_txt)
                count_fail += 1
                continue
            else:
                dt = datetime.datetime.strptime(hiduke.get_exif(f_path), '%Y:%m:%d %H:%M:%S')
            
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
            print('> Succesed: "' + name_1 + '" moved to ' + dt_dir_path)
            print('> And Renamed: ' + name_1 + ' -> ' + name_2)
            count_success += 1

    print('> All Finished!')
    print('>> Result')
    print('>>> Successed: ' + str(count_success) + " files.")
    print('>>> Failed: ' + str(count_fail) + " files.")    

if __name__ == '__main__':
    args = sys.argv
    dir_path = args[1]
    satsueibi_de_wakeru_v2(dir_path)
    

