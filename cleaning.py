import glob
import subprocess
from subprocess import PIPE
import binascii
import shutil
import os 

# 整理対象ファイルの展開
f = open('cleaning_directory.txt', 'r')
from_directory = f.read().split('\n')
f.close()

file_list = []
for d in from_directory:
    file_list += glob.glob(d + "/*")

# 登録した入手先ファイルの展開
with open('urls.txt', 'r') as urls:
    # 移動先ディレクトリファイルの展開
    with open('target_directory.txt', 'r') as directory:

        urls_list = urls.read().split('\n')
        to_directories = directory.read().split('\n')

        # ファイル名にスペースが入っていることへの対策
        for d in to_directories:
            d.replace(' ', '\ ')

        # ファイルごとにコマンド実行して入手先情報を得る
        for moved_file in file_list:
            command = "xattr -p com.apple.metadata:kMDItemWhereFroms " + moved_file.replace(' ', '\ ')
            out = subprocess.run(command, shell=True, stdout=PIPE, stderr=PIPE, text=True)
            binary = out.stdout

            # 16進数表示を直してstr型へ
            binary_text = str(binascii.unhexlify(binary.replace(' ', '').replace('\n', '')))

            for i, url in enumerate(urls_list):
                # URL候補にヒットすればヒット部分の先頭インデックスが帰ってくる
                start_index = binary_text.find(url)

                # URL候補になければ次のファイルへ
                if start_index == -1:
                    continue

                # 候補にあれば転送する．転送先に同一名称ファイルがあった場合削除するか質問する．
                try:
                    new_path = shutil.move(moved_file, to_directories[i])
                    print(new_path)
                except Exception as e:
                    print(e)
                    res = input(moved_file + 'を削除します．よろしいですか？ y/n\n')
                    if res == 'y':
                        os.remove(moved_file)
                    else:
                        print('一応残しておきます...')