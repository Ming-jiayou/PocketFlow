from openai import OpenAI
import os

def call_llm(messages):
    client = OpenAI(api_key="sk-cwranjpgrwjqfxkzcwcpulsvtifhcgkmrkuqrsnzbglgiikj", 
                    base_url="https://api.siliconflow.cn/v1")
    
    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct",
        messages=messages,
        temperature=0.7
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    # Test the LLM call
    messages = [{"role": "user", "content": "In a few words, what's the meaning of life?"}]
    response = call_llm(messages)
    print(f"Prompt: {messages[0]['content']}")
    print(f"Response: {response}")
