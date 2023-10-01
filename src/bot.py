from transformers import AutoTokenizer
from transformers import pipeline
import transformers
import torch
from huggingface_hub import login

import os

class LlamaBot:
    def __init__(self):
        login(token = os.environ['HF_TOKEN'])
        self.model = "meta-llama/Llama-2-7b-chat-hf"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model, use_auth_token=True)
        self.llama_pipeline = pipeline(
            "text-generation",  # LLM task
            model=self.model,
            torch_dtype=torch.bfloat16,
            device_map="auto",
        )

    def get_response(self, prompt):
        """
        Generate a response from the Llama model.

        Parameters:
            prompt (str): The user's input/question for the model.

        Returns:
            str: The model's response.
        """
        sequences = self.llama_pipeline(
            prompt,
            do_sample=True,
            top_k=10,
            num_return_sequences=1,
            eos_token_id=self.tokenizer.eos_token_id,
            max_length=512,
        )
        return sequences[0]['generated_text']

class BhagavadGitaBot:
    def __init__(self):
        self.llama_bot = LlamaBot()

    def get_response(self, query):
        """
        Generate a response from the Bhagavad Gita bot.

        Parameters:
            query (str): The user's input/question for the bot.

        Returns:
            str: The bot's response.
        """
        # AI Chatbot which answers User’s queries/life problems by quoting examples
# from The Bhagavad Gita using Meta’s Llama 2 model.
        prompt = f"You are a AI Chatbot which answers queries/life problems by quoting examples from The Bhagavad Gita. User: {query} Bot:"
        return self.llama_bot.get_response(query)