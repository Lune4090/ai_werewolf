import openai as ai
from pseudo_personality_base import pseudo_personality_base

class mono_pseudo_personality(pseudo_personality_base):

    def __init__(self, KEY: str, LLM_model: str, temperature: float = 1) -> None:
        super().__init__(KEY, LLM_model, temperature)
        

    def personality_imprinting(self, about_personality: str, name: str):
        self.name = name

        self.hear_as_system(about_personality)
        self.num_system_comments += 1

        completion = ai.ChatCompletion.create(
            model = self.LLM_model,
            messages = self.memory,
            temperature = self.temperature
        )

        return completion["choices"][0]["message"]["content"]


class main_pseudo_personality(pseudo_personality_base):

    def __init__(self, KEY: str, temperature: float = 1) -> None:
        super().__init__(KEY, temperature)

class sub_pseudo_personality(pseudo_personality_base):

    def __init__(self, KEY: str, temperature: float = 1) -> None:
        super().__init__(KEY, temperature)