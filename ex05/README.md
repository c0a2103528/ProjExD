# 第5回
## 戦え！こうかとん（ex05/fight_kokaton.py）
### ゲーム概要
- ex05/fight_kokaton.pyを実行すると，1600x900䛾スクリーンに草原が描画され，こうかとんを移動させ飛び回る爆弾から逃げるゲーム
- こうかとんが爆弾と接触するとゲームオーバーで終了する
### 操作方法
- 矢印キーでこうかとんを上下左右に移動する
### 追加機能
- 増加：爆弾を複数個にする
- 加速：時間とともに爆弾が加速する
- 画像切替：着弾時、空中、陸上でこうかとん画像が切り替わる
- 攻撃：こうかとんに剣を持たせ、剣がボールに当たった時、ボールが消える
- ゲームオーバー：着弾時、「Game Over」のテキストを表示し、2秒後に終了する
- スコア：画面左上に表示し、爆弾を一つ消す度に加算する
- クリア判定：全ての爆弾を消したらクリアとし、「Congratulations!」の文字を表示する
### ToDo（実装しようと思ったけど時間がなかった）
- [ ] 方向反転：逆方向を向いたとき、剣も含めて反転させる
- [ ] アイテム：道具を取ることで剣の大きさが変わる
- [ ] 速さが速くなりすぎたとき、爆弾が消えるバグの修正
- [ ] BGMの追加
### メモ