# cleaning.pyの使い方

## cleaning_directory.txt

整理したいディレクトリの絶対パスを登録するファイル．  
<br>

## urls.txt
入手先を登録しておくファイル．ここに書いたパス(URL)以下の階層からダウンロードしたファイルが自動振り分け対象となる
<br>

## target_directory.txt
振り分け先のディレクトリの絶対パスを記述しておくファイル．site.txtと行で対応させる必要がある．

<br>
<br>

ex. site.txtの2行目に https://hogehoge/sample と書かれていたとして，このパスから始まるページでダウンロードしたファイルはtarget_directory.txtの2行目に書かれたディレクトリに振り分けられる
