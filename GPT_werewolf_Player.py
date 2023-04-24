import openai as ai

class AI_werewolf_player_base():
    """
    AI_werewolf_player is handling the memory for GPT,
    and it's also handling OpenAI-API.
    """

    def __init__(self, KEY: str) -> None:
        ai.api_key = KEY
        self.memory: list = []
        self.is_already_heard_start_declaration: bool = False

    def clear_mem(self) -> None:
        if len(self.memory)>15:
            del self.memory[6:]
            print(self.memory)
    
    def think_and_say(self) -> str:
        "use api to think and say my opinion"
        completion = ai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = self.memory
        )
        content = completion["choices"][0]["message"]["content"].replace("\n", "").replace(" ", "")
        self.memory.append({"role": "assistant", "content": f'{content}'})

        return content
    
    def hear_start_declaration(self, start_context: str) -> None:
        "hear system context to GPT for starting werewolf game session, called only once at first"

        if self.is_already_heard_start_declaration:
            raise ValueError("self.is_already_done_start_declaration = True, You are already make start_declaration!")
        else:
            self.memory.append({"role": "system", "content": start_context})
            self.is_already_done_heard_declaration = True
        
    
    def hear_other_agents_comments(self, comments: str) -> None:
        "hear other agent's comment and update my memory."
        self.memory.append({"role": "assistant", "content": comments})

    def hear_GM_comments(self, comments:str) -> None:
        "hear other GM's comment and update my memory"
        self.memory.append({"role": "user", "content": comments})
