import openai

# 设置 API Key
openai.api_key = "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"

# 设置请求参数
model_engine = "text-davinci-002"
prompt = "我成功了么"

completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# 获取 ChatGPT 的回复
message = completions.choices[0].text
print(message)
