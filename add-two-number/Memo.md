step1
- step1ではresule_nodeに正しく値が収納されていなかった
- ListNodeの全ての値を合計した後に、割れなくなるまで分解していく手法
- ListNodeの加算処理が間違っていそう

step2
- placeではなくcarryの方が題に合う
- 商と余りを同時に取得できるdivmodメソッドがある
- 与えられたl1,l2をそのまま動かさず、コピーを動かすべきだった
- step1では全ての合計を求めた後に10ずつ割っていく処理を入れていたが、総和は必要なかった
- inner_functionは使いやすくて良いと思った
- 格納方法について
  - result.next = ListNode(sum_digit % 10)
  - resultのnextに結果を代入するのは違和感があるというコメント
  - result に値を格納していって、whileの最後で result = result.next していくのが自然らしい
- 繰り上がりの行をListNode(1, None), 繰り上がりが無い行をListNode(0, None)で場合分けする方法もあった
- 番兵は作らない
    - 最初のノードだけに対応するような処理を入れずに、dummyを作成して入れ替えることで対応
- 丁寧にやるならl1,l2の大きさ判定やnextが存在しない場合にnodeの最後のNoneを入れるなどを行うべきだった