import openai as ai

class pseudo_personality_base():
    """
    AI_werewolf_player is handling the memory for GPT,
    and it's also handling OpenAI-API, like API key and temperature.
    """

    def __init__(self, KEY: str, LLM_model: str, temperature: float = 1.0) -> None:
        ai.api_key = KEY
        self.memory: list = []
        "past conversation is preserved as memory"
        self.temperature = temperature
        self.num_system_comments = 0
        "count the number of comments as system, for preserving the reset"
        self.LLM_model = LLM_model

    def forget_mem(self, forgeting_target_position: int = 6, forgeting_len: int = 6) -> None:
        if forgeting_target_position > len(self.memory):
            print("The length of my memory is too short to delete")

        elif forgeting_target_position < self.num_system_comments:
            print("The number of comments as system %d is larger than forgeting_target%d,\
                so only the rest of the content will be removed"\
                %(self.num_system_comments, forgeting_target_position))
            
            if forgeting_target_position + forgeting_len >= len(self.memory):
                del self.memory[forgeting_target_position:]
            else:
                del self.memory[forgeting_target_position:forgeting_len] 
                
        else:
            if forgeting_target_position + forgeting_len >= len(self.memory):
                del self.memory[forgeting_target_position:]
            else:
                del self.memory[forgeting_target_position:forgeting_len] 

    def think_and_say(self) -> str:
        "Based on the memory, think about what to say and say my opinion"
        completion = ai.ChatCompletion.create(
            model = self.LLM_model,
            messages = self.memory,
            temperature = self.temperature
        )
        content = completion["choices"][0]["message"]["content"].replace("\n", "")
        self.memory.append({"role": "assistant", "content": f'{content}'})

        return content
    
    def hear_as_system(self, start_context: str) -> None:
        "hear given comment as it is assistant information. It wil be helpful to inform the model about backgrounds"
        self.memory.append({"role": "system", "content": start_context})
        self.num_system_comments += 1
    
    def hear_as_assistant(self, comments: str) -> None:
        "hear given comment as it is assistant information. It will be helpful to inform the model other agent's comments."
        self.memory.append({"role": "assistant", "content": comments})

    def hear_as_user(self, comments:str) -> None:
        "hear given comment as it is user requirement. It will be helpful to inform what you the model want her to do."
        self.memory.append({"role": "user", "content": comments})