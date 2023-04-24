import openai as ai
from making_personality import mono_pseudo_personality

class player_making():
    pass

class AI_werewolf_player_ver0(mono_pseudo_personality):
    
    def __init__(self, KEY: str, LLM_model: str, temperature: float = 1) -> None:
        super().__init__(KEY, LLM_model, temperature)

    
    def role_imprinting(self, about_role: str, role: str) -> str:
        self.role = role

        self.hear_as_system(about_role)
        self.num_system_comments += 1

        completion = ai.ChatCompletion.create(
            model = self.LLM_model,
            messages = self.memory,
            temperature = self.temperature
        )

        return completion["choices"][0]["message"]["content"]
    
    
    def game_contents_imprinting(self, about_werewolf: str) -> str:

        self.hear_as_system(about_werewolf)
        self.num_system_comments += 1

        completion = ai.ChatCompletion.create(
            model = self.LLM_model,
            messages = self.memory,
            temperature = self.temperature
        )

        return completion["choices"][0]["message"]["content"]