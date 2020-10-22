# Hiduke-de-Wakeru



## hiduke_de_wakeru.py
***
複数のファイルをそれぞれ **作成日(最終更新日)ごと** にフォルダ分けするPythonコードです。
スケッチなどのカメラで撮影していないイメージファイルにも使用できます。

<span style="font-size: 60%; color: gray;">This is Python code for separating multiple files into folders by date.</span>
<span style="font-size: 60%; color: gray;">It can also be used for image files such as sketches that have not been taken with the camera..</span>

"/home/user/image" ディレクトリにあるJPEGファイル(.jpg)をフォルダ分けする場合の例です。
コンソールで本Pythonコードを下記の要領で実行します。

<span style="font-size: 60%; color: gray;">The following example divides JPEG files (.jpg) in the "/home/user/image" directory into folders by date.
</span>

```
$python hiduke_de_wakeru.py /home/user/image jpg
```

## satsueibi_de_wakeru.py
***
複数のファイルをそれぞれ **撮影日ごと** にフォルダ分けするPythonコードです。
カメラで撮影した画像の生データ等、撮影日時の情報が入っているイメージファイルにのみ適用できます。

<span style="font-size: 60%; color: gray;">Python code that divides multiple files into folders according to shooting date.
It can be applied only to image files that contain information on the shooting date and time, such as raw data of images taken with the camera.</span>

## Pythonコード呼び出し時に与える引数について
***

それぞれの引数が下記の内容になっています。
- 第1引数: ディレクトリパス
- 第2引数: 拡張子('.'無しで)

Arguments
- 1st: target directory path
- 2nd: extended(without '.')
