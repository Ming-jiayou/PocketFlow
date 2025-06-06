from openai import OpenAI
import os

# def call_llm(prompt):
#     client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", "your-api-key"))
#     response = client.messages.create(
#         model="claude-3-7-sonnet-20250219",
#         max_tokens=10000,
#         messages=[
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return response.content[0].text

def call_llm(prompt):
    client = OpenAI(api_key="sk-cwranjpgrwjqfxkzcwcpulsvtifhcgkmrkuqrsnzbglgiikj", 
                    base_url="https://api.siliconflow.cn/v1")
    
    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    print("## Testing call_llm")
    prompt = "In a few words, what is the meaning of life?"
    print(f"## Prompt: {prompt}")
    response = call_llm(prompt)
    print(f"## Response: {response}")