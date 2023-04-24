# AI_werewolf
人狼知能用リポジトリ(メイン)
基本的にはOpenAIのAPIを利用することを前提としています。
LLMないしAPIの都合上、通信するたびに過去の内容をリセットしてしまうので、
仮想の名前や人格、過去の発言を記憶できるように格納しています。

# 各ファイルの説明
  
pseudo_personality_base
  　そのままでは人格がなく、記憶ができないOpenAIのAPI経由でのLLMへの接続に
   それらを持たせる為のクラスである、○○_pseudo_personalityクラスの基底クラスの
   pseudo_personality_base()を格納
   クラスの内容としては、
   ・コンストラクタ
     ・KEYを使ってLLM_Modelで指定したmodelを使用してAPIに接続、temperatureを指定可能
     ・過去の会話をmemoryに保存して通信時に送信することにより、記憶を持っているかのように振舞わせる
     ・人格やゲームルールの刷り込みの消去を防ぐために回数を記憶してforget_memで削除対象外にする
   ・forget_mem()
     ・memoryが長くなりトークンを食いすぎるのを防ぐために、指定した位置から指定した長さだけ履歴を削除
   ・think_and_say()
     ・APIに履歴を送信して結果を受け取り出力
     ・自分の発言もrole:assistantとして保存する
   ・hear_as_○○()
     ・○○に入るroleとして内容をmemoryに登録
     
 making_personality
   　pseudo_personality_baseを継承したクラス群を格納
   様々なpersonalityを実現するためにいろいろ作る予定だけど今はmono_pseudo_personalityのみ
   mono_pseudo_personality(pseudo_personality_base)クラスの内容は
    ・about_personalityに人格についての情報を書き込み。
    ・nameはそのインスタンスの名前。基本的にLLM側が使うのではなく、他のプログラムが識別のために使用

making_player
  　making_personality中の特定のクラスを継承して人狼のプレイヤーにする
   基本的には
   ・AI_werewolf_player_ver0(mono_pseudo_personality)
    ・game_contents_imprinting()
      人狼のゲーム内容を刷り込み
    ・role_imprinting()
      自分の役職についての内容を特別に刷り込み
      
werewolf_GM
    人狼のGMをやってくれるGM_base()クラスを格納。かなり突貫工事なのでぐちゃぐちゃしているけど、
   基本的にはコンストラクタでプレイヤーインスタンスとその名前と役職を入力から受け取って保存、
   day_session()で昼のターンを行い、night_session()で夜のターンを行います
   is_gameover()が試合終了条件をチェックします

game_example
  　以上のファイルを用いることで、KEYに自分のAPIキーを入れて実行するとOpenAIのLLMを使って人狼ができるようにしました。
  初期プレイヤーは5人、役職は村人、人狼、狂人、騎士、占い師です。
  　また、初期刷り込み用プロトコル(○○_imprintingというメソッド)はここで刷り込み内容を書いているので、
  ここから名前や職業はもちろん、プロトコルの書き方も変更できます。
