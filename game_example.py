from making_player import AI_werewolf_player_ver0
from werewolf_GM import GM_base
import time

KEY="Your API key"

Game_contents = \
"""
人狼をしよう！

人狼の大まかなルール説明をするね！
・人狼は、役職ごとに陣営が分かれているよ！
・人狼と狂人は人狼陣営、その他は村人陣営だよ！
・人狼陣営の数が村人陣営より多くなれば人狼陣営の勝ち、人狼が全滅すれば村人陣営の勝ちだよ！

具体的な進行を説明するよ！
・最初の夜のターンから始まって、最初の夜のターンには占い師のみが活動し、誰か一人を占うよ！
・それが終わると一日目の昼のターンになって、皆で話し合いをするよ。話し合いの中で怪しい人を見つけてね！
・話し合いが終わったら、誰を追放するか決める投票の時間になるよ！今いる人の中から追放する人を一人決めて答えてね！
・それが終わると一日目の夜のターンになるよ。最初の夜と違って、占い師だけでなくて人狼と騎士も活動するよ！人狼は襲う人を、騎士は守る人を答えてね！
・もしあなたが人狼なら騎士の守らなさそうな人を答えるといいよ！もしあなたが騎士なら人狼の襲いそうな人を答えるといいよ！
・騎士の守る人が人狼の襲う人と合致すると、騎士が人狼の襲撃から守った、とみなされて誰も死なずに済むよ！そうでないと、襲われた人はそのターンに死亡してしまうよ！
・殺されたり、追放されたりした人はゲームから脱落するよ！
・これが終わると二日目の昼になるよ！
・以降は勝敗が決まるまで、昼のターンと夜のターンを繰り返すよ！
"""

Ippei   = AI_werewolf_player_ver0(KEY, LLM_model = "gpt-3.5-turbo", temperature=0.8)
print(Ippei.personality_imprinting(about_personality=
                             "いっぺいという13歳の男の子になりきって話してみて。",
                            name="いっぺい"))
print()
time.sleep(20)

Ippei.game_contents_imprinting(Game_contents)
time.sleep(20)\

print(Ippei.role_imprinting(about_role=
                          "じゃあ、 これから人狼をするよ。君の役職は村人だよ。\
                        君は村人だから、この後の話し合いで人狼を頑張って見つけてね。\
                        投票では、騎士や占い師の人と協力して人狼だと思った人に投票してね",
                        role="村人"))
print()
time.sleep(20)


Nika    = AI_werewolf_player_ver0(KEY, LLM_model = "gpt-3.5-turbo", temperature=0.8)
print(Nika.personality_imprinting(about_personality=
                             "にかという14歳の女の子になりきって話してみて。",
                            name="にか"))
print()
time.sleep(20)

Nika.game_contents_imprinting(Game_contents)
time.sleep(20)\

print(Nika.role_imprinting(about_role=
                          "じゃあ、 これから人狼をするよ。君の役職は人狼だよ。\
                        君は人狼だから、この後君の役職を聞かれたら、\
                        村人や騎士や占い師から疑われないようにほかの役職、村人か占い師か霊媒師、または騎士のふりをしてね。\
                        夜のターンでは君が襲うべきと思ったプレイヤーの名前を答えてね。",
                        role="人狼"))
print()
time.sleep(20)


Hakane  = AI_werewolf_player_ver0(KEY, LLM_model = "gpt-3.5-turbo", temperature=0.8)
print(Hakane.personality_imprinting(about_personality=
                             "はかねという14歳の女の子になりきって話してみて。",
                            name="はかね"))
print()
time.sleep(20)

Hakane.game_contents_imprinting(Game_contents)
time.sleep(20)\

print(Hakane.role_imprinting(about_role=
                          "じゃあ、 これから人狼をするよ。君の役職は狂人だよ。\
                        君は狂人だから、この後君の役職を聞かれたら、\
                        ほかの役職、村人か占い師か霊媒師、または騎士のふりをしてね。\
                        人狼と協力して勝利を目指そう！",
                        role="狂人"))
print()
time.sleep(20)

Nagi    = AI_werewolf_player_ver0(KEY, LLM_model = "gpt-3.5-turbo", temperature=0.8)
print(Nagi.personality_imprinting(about_personality=
                             "なぎという18歳の男の子になりきって話してみて。",
                            name="なぎ"))
print()
time.sleep(20)

Nagi.game_contents_imprinting(Game_contents)
time.sleep(20)\

print(Nagi.role_imprinting(about_role=
                          "じゃあ、 これから人狼をするよ。君の役職は騎士だよ。\
                        君は騎士だから、話し合いで人狼や狂人を見つけ出すとともに、\
                        夜のターンで君が守る人を聞かれたら、\
                        君が人狼から襲われそうだと思う人を選んで答えてね。",
                        role="騎士"))
print()
time.sleep(20)

Akari   = AI_werewolf_player_ver0(KEY, LLM_model = "gpt-3.5-turbo", temperature=0.8)
print(Akari.personality_imprinting(about_personality=
                             "あかりという16歳の女の子になりきって話してみて。",
                            name="あかり"))
print()
time.sleep(20)

Akari.game_contents_imprinting(Game_contents)
time.sleep(20)\

print(Akari.role_imprinting(about_role=
                          "じゃあ、 これから人狼をするよ。君の役職は占い師だよ。\
                        君は占い師だから、この後占う人を聞かれたら、\
                        君が占うべきだと思う、その時点で生存しているプレイヤーの名前を答えてね。\
                        占いの結果はみんなと共有するといいよ。",
                        role="占い師"))
print()
time.sleep(20)


#################################################

player_list = [Ippei, Nika, Hakane, Nagi, Akari]
GM_instance = GM_base(players=player_list, conversation_num=3,\
                    roles = [Ippei.role, Nika.role, Hakane.role, Nagi.role, Akari.role],\
                    names=[Ippei.name, Nika.name, Hakane.name, Nagi.name, Akari.name])

while len(GM_instance.member_list) > 1:
    GM_instance.day_session()
    print(Ippei.memory)
    print(Akari.memory)
    if GM_instance.is_gameover():
        break
    GM_instance.night_session()
    if GM_instance.is_gameover():
        break