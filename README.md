# AITuber サンプル

AITuber本のコードを少し改造して自分用にした

参考：
- [AITuberを作ってみたら生成AIプログラミングがよくわかった件](https://www.amazon.co.jp/gp/product/B0CLKZ7NC3)
- [上記の本のGitHubサンプルリポジトリ](https://github.com/sr2mg/aituber_python_programing_example)


## Environment

- Windows 11
- Python 3.11.5


## Installation

```bash
$ python -m pip install -r requirements.txt
```

### その他インストールするソフト

- VOICEVOX
  1. ここからダウンロード：https://voicevox.hiroshiba.jp/

- VB-CABLE （仮想マイク）
  1. ここからダウンロード：https://vb-audio.com/Cable/index.htm
  2. ダウンロードしたZipファイルを展開
  3. `VBCABLE_Setup_x64`を右クリックして管理者として実行、インストール
  4. PCを再起動
  5. サウンドデバイスに`CABLE Input`が表示されればOK

- OBS Studio
  1. ここからダウンロード：https://obsproject.com/ja/download
  2. 初期設定は以下のような感じで
     1. 配信のために最適化し、録画は二次的なものとする
     2. 基本解像度：現在の値を使用(1920x1080)
     3. FPS：60または30のいずれか、可能なら60を優先
     4. サービス：YouTube-RTMPS
     5. アカウント接続

## Usage

### YouTube

1. コメント欄を取得したいライブ配信のvideo-idを調べる
   - ライブ配信のURL見るとわかる　`v=<配信のvideo-id>`みたいになってる

### VOICEVOX

1. ソフトを立ち上げれるだけでOK

### OBS Studio

1. シーンを作成
   
2. ソースを追加
   1. `Question`という名前のテキスト
   2. `Answer`という名前のテキスト
   3. ブラウザ（コメント欄になる）
      - URL: `https://www.youtube.com/live_chat?is_popout=1&v=<配信のvideo-id>`
   4. 背景
   
3. ツール > WebSocketサーバー設定
   1. WebSocketサーバーを有効にする　にチェック
   2. 接続情報を表示　のボタンを押す
   3. port, passwordをメモ
   
4. 音声設定
   1. 設定 > 音声 > マイク音声 を `CABLE Output`に
   2. オーディオの詳細プロパティを開き、マイクの音声モニタリングを「モニターと出力」に変更

5. さらに詳しい調整は[NoteのOBSのところ](#OBS)を参照

### コード

1. `.env`を設定
2. `run.py`を実行
   
  ```bash
  $ python run.py
  ```

## Note

### VOICEVOX

- ドキュメント：ソフトを立ち上げた状態で http://localhost:50021/docs

- 利用規約
  - VOICEVOXの利用規約：https://voicevox.hiroshiba.jp/term/
  - 各キャラクターの音声利用規約：https://voicevox.hiroshiba.jp/

### OBS

- チャット欄の見た目を整える
  - http://css4obs.starfree.jp/
  - このページでいろいろ設定して、ページ下のCSSをコピー
  - OBSのブラウザソースのプロパティを開いてカスタムCSSのところにペースト

- テキストソースのフォント
  - チャット欄のCSSのGoogleフォントに合わせたい
  - Googleフォント：https://fonts.google.com/
  - ダウンロードして展開して、ttfファイルを右クリック、インストール

- テキストソースの領域を指定する
  - プロパティを開いて、一番下のところにテキスト領域の範囲を指定するという項目があるのでチェック

### obs-python

OBSをPythonから操作できる　https://pypi.org/project/obsws-python/

### pytchat

YouTubeコメントを取得・解析する　https://pypi.org/project/pytchat/
