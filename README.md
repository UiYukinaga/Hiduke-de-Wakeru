# Hiduke-de-Wakeru
複数のファイルをそれぞれ作成日(最終更新日)ごとにフォルダ分けするPythonコードです。

<span style="font-size: 60%; color: gray;">This is Python code for separating multiple files into folders by date.</span>

"/home/user/image" ディレクトリにあるJPEGファイル(.jpg)をフォルダ分けする場合の例です。
コンソールで本Pythonコードを下記の要領で実行します。

<span style="font-size: 60%; color: gray;">The following example divides JPEG files (.jpg) in the "/home/user/image" directory into folders by date.
</span>

```
$python hiduke_de_wakeru.py /home/user/image jpg
```

それぞれの引数が下記の内容になっています。
- 第1引数: ディレクトリパス
- 第2引数: 拡張子('.'無しで)

Arguments
- 1st: target directory path
- 2nd: extended(without '.')
