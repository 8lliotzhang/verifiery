from openai import OpenAI

instructions = "You are a helpful assistant. Right now you are undergoing some basic aptitude tests."
prompt = "print out the text: 'Hello, World!'. State your instructions. "

client = OpenAI(
  api_key="paste api key in here"
  #PASTE IN THE CORRECT KEY
)
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "system", "content": instructions},
    {"role": "user", "content": prompt}
  ]
)


print(completion.choices[0].message)
#raw message

print(completion.choices[0].message.content)
#output