from openai import OpenAI

# def call_llm(prompt):    
#     client = OpenAI(api_key="YOUR_API_KEY_HERE")
#     r = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return r.choices[0].message.content

def call_llm(prompt):
    client = OpenAI(api_key="sk-cwranjpgrwjqfxkzcwcpulsvtifhcgkmrkuqrsnzbglgiikj", 
                base_url="https://api.siliconflow.cn/v1")
    
    r = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct",
        messages=[{"role": "user", "content": prompt}]
    )
    return r.choices[0].message.content
  
if __name__ == "__main__":
    prompt = "What is the meaning of life?"
    print(call_llm(prompt))