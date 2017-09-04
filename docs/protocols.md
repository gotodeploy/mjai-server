# プロトコル

## 接続時

* From server

```json
{"type":"hello","protocol":"mjsonp","protocol_version":1}
```

* To server

```json
{"type":"join","name":"A","room":"default"}
```

ゲームに参加することを送る。プレイヤ名はA

* From server(ゲーム開始)

```json
{"type":"start_game","gametype":"tonpu","id":1,"names":["D","A","C","B"]}
```

gametype(ゲームの種類): tonpu(東風戦)

idは1、この数字はactorに連動する。

* To server

問題がなければ{"type":"none"}を返す。

```json
{"type":"none"}
```


## 局開始時

* From server

```json
{"type":"start_kyoku","bakaze":"E","kyoku":1,"honba":0,"kyotaku":0,"oya":0,"dora_marker":"5mr","tehais":[["?","?","?","?","?","?","?","?","?","?","?","?","?"],["2m","3p","8p","1s","4s","5s","6s","8s","9s","W","N","P","F"],["?","?","?","?","?","?","?","?","?","?","?","?","?"],["?","?","?","?","?","?","?","?","?","?","?","?","?"]]}
```

東1局数0本場供託0本
親はidが0のプレイヤ
ドラ表示牌が赤5m
tehaisは配牌

* To server

```json
{"type":"none"}
```

## ツモ時

### 自家のツモ番

* From server

```json
{"type":"tsumo","actor":1,"pai":"E","possible_actions":[]}
```

東をツモ

* To server

```json
{"type":"dahai","actor":1,"pai":"W","tsumogiri":false}
```

西を切る
ツモ切りか手出しを選択をできる。
ツモ切りする場合は"tsumogiri":true
手出しする場合は"tsumogiri":false

* From server

```json
{"type":"dahai","actor":1,"pai":"W","tsumogiri":false}
```
サーバーからの確認

* To server

```json
{"type":"none"}
```

### 他家のツモ番

* From server

```json
{"type":"tsumo","actor":0,"pai":"?"}
```

idが0のプレイヤのツモ番。
当然何をツモしたかはわからない。

* To server

```json
{"type":"none"}
```

* From server

```json
{"type":"dahai","actor":0,"pai":"N","tsumogiri":false,"possible_actions":[]}
```

北を手出し

* To server

```json
{"type":"none"}
```

## リーチ

### 自家のリーチ宣言

* From server

```json
{"type":"tsumo","actor":1,"pai":"6m","possible_actions":[{"type":"reach","actor":1}]}
```

id1が聴牌

* To server

```json
{"actor":1,"type":"reach"}
```

リーチを宣言

* From server

```json
{"type":"reach","actor":1,"cannot_dahai":["1m","2m","3m","5mr","7m","6p","7p","8p","9p","4s","6m"]}
```

サーバーから確認

* To server

```json
{"actor":1,"pai":"6s","tsumogiri":false,"type":"dahai"}
```

6sを切る

* From server

```json
{"type":"dahai","actor":1,"pai":"6s","tsumogiri":false}
```

確認

* To server

```json
{"type":"none"}
```

* From server

```json
{"type":"reach_accepted","actor":1,"deltas":[0,-1000,0,0],"scores":[25000,29800,34700,9500]}
```
リーチ宣言が認められたため、点数状況を表示

* To server

```json
{"type":"none"}
```

### 他家のリーチ宣言

* From server

```json
{"type":"tsumo","actor":3,"pai":"?"}
```

id3のツモ番

* To server

```json
{"type":"none"}
```

* From server

```json
{"type":"reach","actor":3}
```

idがリーチを宣言

* To server

```json
{"type":"none"}
```

* From server

```json
{"type":"dahai","actor":3,"pai":"8s","tsumogiri":false,"possible_actions":[]}
```

8sを切る

* To server

```json
{"type":"none"}
```

* From server

```json
{"type":"reach_accepted","actor":3,"deltas":[0,0,0,-1000],"scores":[25000,30800,24400,17800]}
```
リーチ宣言が認められたため,点数状況を表示
* To server

```json
{"type":"none"}
```

## ポン

### 自家が鳴き

* From server

```json
{"type":"dahai","actor":3,"pai":"1s","tsumogiri":false,"possible_actions":[{"type":"pon","actor":1,"target":3,"pai":"1s","consumed":["1s","1s"]}]}
```

相手の切った1sが鳴ける

* To server

```json
{"type":"pon","actor":1,"consumed":["1s","1s"],"pai":"1s","target":3}
```

* `pon`: ポンを宣言
* `actor`: ポンするプレイヤ
* `consumed`: さらす牌
* `pai`: 鳴く牌
* `target`: 鳴いた相手のid

* From server

```json
{"type":"pon","actor":1,"target":3,"pai":"1s","consumed":["1s","1s"],"cannot_dahai":[]}
```

確認

* To server

```json
{"type":"dahai","actor":1,"pai":"3p","tsumogiri":false}
```

切る牌の選択

* From server

```json
{"type":"dahai","actor":1,"pai":"3p","tsumogiri":false}
```

確認

* To server

```json
{"type":"none"}
```

### 他家が鳴き

* From server

```json
{"type":"dahai","actor":3,"pai":"8m","tsumogiri":true,"possible_actions":[]}
```

相手が8mを切る

* To server

```json
{"type":"none"}
```

自分は鳴かない。

* From server

```json
{"type":"pon","actor":2,"target":3,"pai":"8m","consumed":["8m","8m"]}
```

id2がtarget3から8mをポン

* To server

```json
{"type":"none"}
```

* From server

```json
{"type":"dahai","actor":2,"pai":"C","tsumogiri":false,"possible_actions":[]}
```

プレイヤ2の打牌

* To server

```json
{"type":"none"}
```

チーやカンなども同様

```json
{"type":"chi","actor":0,"target":3,"pai":"4s","consumed":["5sr","6s"]}
```

```json
{"type":"ankan","actor":2,"consumed":["3m","3m","3m","3m"]}
```

```json
{"type":"kakan","actor":3,"pai":"8m","consumed":["8m","8m","8m"]}
```

```json
{"type":"daiminkai","actor":1,"target":3,"pai":"4s","consumed":["4s","4s","4s"]}
```

新ドラがめくれた時

* From server

```json
{"type":"dora","dora_marker":"6p"}
```

表示牌は6p

* To server

```json
{"type":"none"}
```

## 和了

### 自家が和了

* From server

```json
{"type":"tsumo","actor":1,"pai":"8p","possible_actions":[{"type":"hora","actor":1,"target":1,"pai":"8p"}]}
```

8pをツモ

* To server

```json
{"type":"hora","actor":1,"pai":"8p","target":1}
```

`hora`: 和了を宣言、ロンやツモではなくhoraでOK。
`pai`: 和了牌
`actor`: 和了したプレイヤ
`target`: ツモの場合は自分、ロンの場合は切ったプレイヤのid

大事なことは点数を申告する必要はない

* From server

```json
{"type":"hora","actor":1,"target":1,"pai":"8p","uradora_markers":["3p"],"hora_tehais":["1m","2m","3m","5mr","6m","7m","6p","7p","7p","8p","9p","4s","4s"],"yakus":[["akadora",1],["reach",1],["menzenchin_tsumoho",1],["pinfu",1]],"fu":20,"fan":4,"hora_points":5200,"deltas":[-1300,6200,-2600,-1300],"scores":[23700,36000,32100,8200]}
```

サーバーが点数を教えてくれる。

* `uradora_markers`: 裏ドラ表示牌
* `hora_points`: 和了点
* `hora_tehais`: 和了した手牌
* `deltas`: 得点変動
* `scores`: 最終的な得点状況を表示。

* To server

```json
{"type":"none"}
```

* From server

```json
{"type":"end_kyoku"}
```

* To server

```json
{"type":"none"}
```

### 他家が和了

* From server

```json
{"type":"dahai","actor":3,"pai":"9m","tsumogiri":true,"possible_actions":[]}
```

id3が9mをツモ切り

* To server

```json
{"type":"none"}
```

* From server

```json
{"type":"hora","actor":2,"target":3,"pai":"9m","uradora_markers":["6m"],"hora_tehais":["5m","5mr","7m","8m","1p","1p","1p","3p","4p","5pr","8s","8s","8s"],"yakus":[["uradora",1],["akadora",2],["reach",1]],"fu":50,"fan":4,"hora_points":8000,"deltas":[0,0,10300,-8300],"scores":[25000,30800,34700,9500]}
```

id2がid3から9mで和了。

* To server

```json
{"type":"none"}
```

* From server

```json
{"type":"end_kyoku"}
```

## 局終了

* To server

```json
{"type":"none"}
```

## 流局時

```json
{"type":"ryukyoku","reason":"fanpai","tehais":[["?","?","?","?","?","?","?","?","?","?","?","?","?"],["?","?","?","?","?","?","?","?","?","?","?","?","?"],["?","?","?","?","?","?","?","?","?","?","?","?","?"],["?","?","?","?","?","?","?","?","?","?","?","?","?"]],"tenpais":[false,false,false,false],"deltas":[0,0,0,0],"scores":[25000,25000,25000,25000]}
```

* `reason`: 流局した理由
* `tehais`: 手牌
* `tenpais`: 聴牌したプレイヤ
* `deltas`: 点数移動
* `scores`: 最終的な点数

### ゲーム終了時

```
{"type":"end_game","scores":[25000,25000,25000,25000]}
```

* `scores`: 最終的な点数
