import os
from openai import OpenAI

def call_llm(prompt):
    client = OpenAI(api_key="sk-cwranjpgrwjqfxkzcwcpulsvtifhcgkmrkuqrsnzbglgiikj", 
                    base_url="https://api.siliconflow.cn/v1")
    
    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    
    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    print(call_llm("Tell me a short joke")) 