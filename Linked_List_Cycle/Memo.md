# step1
- 初見ではオブジェクトでデータを持てば良いくらいしか分からなかった
- ListNodeを定義して解く方法を考えたが具体的な解法が思い浮かばなかった
- 最終的にYoutubeを視聴して理解し、JavaのコードをPythonで置き換えた
# 具体的に分からなかった点
1. サークルが存在するかどうか判定する条件
- 配列とposを使ってどのように判定するのか思いつかなかった
- リストの大きさとposの値で判定する手法を考えたが異なった
2. Optional[ListNode]の使い方
- python3に関する知識が足りない
3. ListNodeについて
- うろ覚え程度で実装できるレベルではなかった

# 学んだこと
1. ListNode
- データ構造の１種であり、自分の次の要素を持つ
- 次の要素のみをもつListを片方向連結リスト、次だけでなく前のノードを持つListを双方向連結リスト
- データに順番があり、辿らないと目的の要素にアクセスできない
- listと異なり、あらかじめ余分なメモリ確保が必要無い
- 新しい要素を追加する場合の計算量がO(1),削除も同様
- ただ、対象を探す操作自体はO(n)必要であるため、リスト先頭以外への操作は得意ではない
- 以下のサイト参照
    - https://ufcpp.net/study/algorithm/col_flist.html?key=flist#flist

2. Optional
- 最近のPythonでは型を明示できるようになった
- その中でも、Noneが入る可能性がある場合の型を明示する際に使用する
- Optional[X] は X | None (や Union[X, None]) と同等です
- Optional[ListNode]と定義することで、ListNode型かNoneが含まれていることを明示
- 以下のサイトを参照
  - https://docs.python.org/ja/3/library/typing.html#typing.Optional

3. 理論について
- サイクルを持つか　= 2つの変数を動かし続け、追いついたらサイクルがある　という発想には辿り着けなかった

# step2
- 拝見したPR
  - https://github.com/t0hsumi/leetcode/pull/1/files
    - Space complexity(空間計算量)、計算量の総称
      - Auxiliary Space Complexity
        - 処理のために追加で必要になったメモリの空間計算量
      - Total Space Complexity
        - Auxiliary Space Complexityと入力に必要なメモリとを両方考慮したもの
    - set()を使った解法
      - set()とは空の集合を生成する
      - 空の集合に現在の要素（head）を１つずつ追加していく
      - サイクルすることで集合に含まれる要素と重複したものが現れるので、そのタイミングでTrueを返す
      - 疑問点：seenに追加したheadとサイクルで再度出現したheadは本当に同一なんだろうか？サイクルしているため、現在のvalとnextの要素は等しくなることは理解できる。ただ、本当に同一のものか上手く説明することができない。mutableオブジェクトとimmutableオブジェクトの違いは学んだが、今回はmutableオブジェクトに値するのでしょうか？

      ```python
      def hasCycle(self, head: Optional[ListNode]) -> bool:
         seen = set()
         while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
         return False
      ```
  - https://github.com/onyx0831/leetcode/pull/1/files#r1852638322
    > current は個人的にはあまり好まないです。
context のようなグローバルな設定などに用いられる傾向が強いからです。
next, previous との対比ならば分からなくもないです。
    - 自分も現在の値をcurrentとつけがち、対比として使用していないならつける必要が無いというのは新たな発見だった


- 拝見したサイト
 
  - https://discordapp.com/channels/1084280443945353267/1221030192609493053/1225674901445283860
  - 処理の流れの自然さについて納得できた
  - 無限処理を使用する例も良かった
  - 脳のワーキングメモリをさっさと解放することが大事というのも胸に刺さった
  ```
  while 1:
    if not A:
      短いZ
      return D
    短いX
    if B:
      break
    長いY
  return C
  ```