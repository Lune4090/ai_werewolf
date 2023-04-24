import time

class GM_base():
    
    def __init__(self, players: list, conversation_num: int ,roles: list, names: list) -> None:
        "set players to their names and roles"
        if len(roles) != len(names):
            raise ValueError("length of roles and that of names is different!!!")
        if len(players) != len(names):
            raise ValueError("length of players and that of names is different!!!")
        self.role_list: list = roles
        self.member_list: list = names
        
        self.member_player_asssign_dict: dict = {}
        self.member_role_assign_dict: dict = {}
        self.role_member_assign_dict: dict = {}
        self.member_voted_num_dict: dict = {}


        for i in range(len(self.role_list)):
            self.member_player_asssign_dict[self.member_list[i]] = players[i]
            self.member_role_assign_dict[self.member_list[i]] = self.role_list[i]
            self.role_member_assign_dict[self.role_list[i]] = self.member_list[i]
            self.member_voted_num_dict[self.member_list[i]] = 0

        print(self.member_role_assign_dict)

        self.day_num: int = 0
        self.is_defending_success = False
        
        self.killed_dict: dict = {}
        self.defended_person: str  = None
        self.invaded_person: str  = None

        self.discussion_loop_num: int = conversation_num

    def night_session(self) -> None:
        self.day_num += 1
        member:str = ""

        if self.day_num == 1:
            print("1日目の夜です")
            print()
            print("占い師は占う人を選んで下さい")
            while member == "":
                self.member_player_asssign_dict[self.role_member_assign_dict["占い師"]].hear_as_user(comments="占う人を%sから選んでください。\
                                                                                                  選んだ名前のみ返答してください。"
                                                                                                  %(self.member_list))
                temp_comment: str = self.member_player_asssign_dict[self.role_member_assign_dict["占い師"]].think_and_say()
                print(self.role_member_assign_dict["占い師"] + ":")
                print(temp_comment)
                for i in range(len(self.member_list)):
                    if self.member_list[i] in temp_comment:
                        member = self.member_list[i]
                        break
                print(member)
                time.sleep(20)

            if self.member_role_assign_dict[member] == "人狼":
                print("%sさんは人狼です。"%(member))
                self.member_player_asssign_dict[self.role_member_assign_dict["占い師"]].hear_as_user("%sさんは人狼です。"
                                                                                                  %(member))
            else:
                print("%sさんは人狼ではありません。"%(member))
                self.member_player_asssign_dict[self.role_member_assign_dict["占い師"]].hear_as_user("%sさんは人狼ではありません。"
                                                                                                  %(member))
            member = ""

        else:
            print("%s日目の夜です"%(self.day_num))
            print()

            print("占い師は占う人を選んで下さい")
            while member == "":
                self.member_player_asssign_dict[self.role_member_assign_dict["占い師"]].hear_as_user(comments="占う人を%sから選んでください。\
                                                                                                  選んだ名前のみ返答してください。"
                                                                                                  %(self.member_list))
                temp_comment: str = self.member_player_asssign_dict[self.role_member_assign_dict["占い師"]].think_and_say()
                for i in range(len(self.member_list)):
                    if self.member_list[i] in temp_comment:
                        member = self.member_list[i]
                        break
                print(member)
                time.sleep(20)

            if self.member_role_assign_dict[member] == "人狼":
                print("%sさんは人狼です。"%(member))
                self.member_player_asssign_dict[self.role_member_assign_dict["占い師"]].hear_as_user("%sさんは人狼です。"
                                                                                                  %(member))
            else:
                print("%sさんは人狼ではありません。"%(member))
                self.member_player_asssign_dict[self.role_member_assign_dict["占い師"]].hear_as_user("%sさんは人狼ではありません。"
                                                                                                  %(member))
            member = ""

            print("騎士は守る人を選んでください")
            print()

            while member == "":
                self.member_player_asssign_dict[self.role_member_assign_dict["騎士"]].hear_as_user(comments="守る人を%sから選んでください。\
                                                                                                 選んだ名前のみ返答してください。"
                                                                                                  %(self.member_list))
                temp_comment: str = self.member_player_asssign_dict[self.role_member_assign_dict["騎士"]].think_and_say()
                for i in range(len(self.member_list)):
                    if self.member_list[i] in temp_comment:
                        member = self.member_list[i]
                        break
                time.sleep(20)
            self.defended_person = member
            member = ""

            print("人狼は襲う人を選んでください")
            print()

            while member == "":
                self.member_player_asssign_dict[self.role_member_assign_dict["人狼"]].hear_as_user(comments="襲う人を%sから選んでください。\
                                                                                                 選んだ名前のみ返答してください。"
                                                                                                  %(self.member_list))
                temp_comment: str = self.member_player_asssign_dict[self.role_member_assign_dict["人狼"]].think_and_say()
                for i in range(len(self.member_list)):
                    if self.member_list[i] in temp_comment:
                        member = self.member_list[i]
                        break
                print(member)
                time.sleep(20)
            self.invaded_person = member
            member = ""

            if self.invaded_person == self.defended_person:
                self.is_defending_success = True
            else:
                "eliminate slaughtered player"
                self.is_defending_success = False
                self.member_list.remove(self.invaded_person)
                temp_killed_player_role = self.member_role_assign_dict.pop(self.invaded_person)
                self.role_list.remove(self.member_role_assign_dict[temp_killed_player_role])
                self.member_player_asssign_dict.pop(self.invaded_person)

    def day_session(self) -> None:
        if self.day_num==0:

            print("それではゲームを開始します")
            print()

        else:
            print()
            print("%d日目の朝です"%(self.day_num))
            print()
            if self.day_num == 1:
                pass

            elif self.is_defending_success:
                print("防衛が成功し昨夜の犠牲者は居ませんでした")
                print()
                self.is_defending_success = False
                for member_name in self.member_player_asssign_dict.keys():
                    self.member_player_asssign_dict[member_name].hear_as_user("防衛が成功し昨夜の犠牲者は居ませんでした")

            else:
                print("防衛は失敗し%sさんが亡くなりました"%(self.invaded_person))
                print()
                for member_name in self.member_player_asssign_dict.keys():
                    self.member_player_asssign_dict[member_name].hear_as_user("防衛は失敗し%sさんが亡くなりました"
                                                                              %(self.invaded_person))
            self.defended_person
            self.invaded_person = None


            "Check Survivor"
            self.surviver_log: str = "現在の生存者は"
            for i in range (len(self.member_list)):
                self.surviver_log = self.surviver_log + self.member_list[i] + " さん、"
            self.surviver_log = self.surviver_log + "です。現在の状況を踏まえて発言を始めてください。"
            print(self.surviver_log)
            print()
            for member_name in self.member_player_asssign_dict.keys():
                self.member_player_asssign_dict[member_name].forget_mem()
                self.member_player_asssign_dict[member_name].hear_as_user(self.surviver_log)
                


            for i in range(self.discussion_loop_num):
                print("%d週目の会話です"%(i+1))
                for speaker_name in self.member_player_asssign_dict.keys():
                    comment = self.member_player_asssign_dict[speaker_name].think_and_say()
                    print("%sさんの会話です"%(speaker_name))
                    print(comment)
                    print()
                    for member_name in self.member_player_asssign_dict.keys():
                        if member_name != speaker_name:
                            self.member_player_asssign_dict[member_name].hear_as_assistant(comment)
                    time.sleep(20)



            print("投票の時間です")
            print()
            for member_name in self.member_player_asssign_dict.keys():
                print(member_name + "さんの投票")
                temp_exile_member = ""
                while temp_exile_member == "":
                    self.member_player_asssign_dict[member_name].hear_as_user(comments="今日、誰をこの村から追放するかを決める投票の時間です。\
                                                                              今までの議論をもとに追放する人を%sから選んでください。\
                                                                              選んだ名前のみ返答してください。"
                                                                            %(self.member_list))
                    temp_comment = self.member_player_asssign_dict[self.role_member_assign_dict["人狼"]].think_and_say()
                    print(temp_comment)

                    for i in range(len(self.member_list)):
                        if self.member_list[i] in temp_comment:
                            temp_exile_member = self.member_list[i]
                            break
                        
                    print(temp_exile_member)
                    time.sleep(20)

                self.member_voted_num_dict[temp_exile_member] += 1
            max_voted_num: int = 0
            max_voted_mans: list = []
            for member in self.member_voted_num_dict.keys():
                if self.member_voted_num_dict[member] > max_voted_num:
                    max_voted_num = self.member_voted_num_dict[member]
                    max_voted_mans = []
                    max_voted_mans.append(member)
                elif self.member_voted_num_dict[member] == max_voted_num:
                    max_voted_mans.append(member)

            print(self.member_voted_num_dict)

            if len(max_voted_mans) == 1:
                print(max_voted_mans[0])
                temp_exiled_member = max_voted_mans[0]
                self.member_list.remove(temp_exiled_member)
                temp_exiled_player_role = self.member_role_assign_dict.pop(temp_exiled_member)
                self.role_list.remove(temp_exiled_player_role)
                self.member_player_asssign_dict.pop(temp_exiled_member)
                self.member_voted_num_dict.pop(temp_exile_member)

                print("投票の結果%s さんが村から追放されました。"%(temp_exiled_member))
                for member_name in self.member_player_asssign_dict.keys():
                    self.member_player_asssign_dict[member_name].hear_as_user("投票の結果%s さんが村から追放されました。"\
                                                                              %(temp_exiled_member))

            else:
                print("投票は拮抗したため誰も村から追放されませんでした。")
                for member_name in self.member_player_asssign_dict.keys():
                    self.member_player_asssign_dict[member_name].hear_as_user("投票は拮抗したため誰も村から追放されませんでした。")
            
            "Initialize voting"
            max_voted_mans = []
            max_voted_num = 0
            for member in self.member_list:
                self.member_voted_num_dict[member] = 0

    def is_gameover(self) -> bool:
        _num_werewolves: int = 0
        _num_werewolf_allies: int = 0
        _num_normals: int = 0
        for i in range(len(self.role_list)):
            if self.role_list[i]=="人狼":
                _num_werewolves += 1

            elif self.role_list[i] == "狂人":
                _num_werewolf_allies += 1

            else:
                _num_normals += 1

        if _num_werewolves == 0:
            print("試合終了！！ 人狼全滅により村人陣営の勝ち！")
            return True

        elif _num_normals < _num_werewolves + _num_werewolf_allies:
            print("試合終了！！ 人狼陣営の数が村人陣営を上回った為人狼陣営の勝ち！")
            return True

        else:
            return False
