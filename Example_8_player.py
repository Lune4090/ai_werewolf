import GPT_werewolf_Player
from GPT_werewolf_GM import GM_base

KEY="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"

AI_player_A = GPT_werewolf_Player.AI_werewolf_player_base(KEY)
AI_player_B = GPT_werewolf_Player.AI_werewolf_player_base(KEY)
AI_player_C = GPT_werewolf_Player.AI_werewolf_player_base(KEY)
AI_player_D = GPT_werewolf_Player.AI_werewolf_player_base(KEY)
AI_player_E = GPT_werewolf_Player.AI_werewolf_player_base(KEY)
AI_player_F = GPT_werewolf_Player.AI_werewolf_player_base(KEY)


player_list = [AI_player_A, AI_player_B, AI_player_C, AI_player_D, AI_player_E, AI_player_F]
GM_instance = GM_base(player_list=player_list, conversation_num=3)

while len(GM_instance.member_list) > 1:
    GM_instance.day_session()
    if GM_instance.is_gameover():
        break
    GM_instance.night_session()
    if GM_instance.is_gameover():
        break
