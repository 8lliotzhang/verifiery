#(i dunno what im doing)
#Nov 16, 2024
#EZ

from openai import OpenAI

client = OpenAI(
  organization='org-KKSqc03MluOn2vKxRCOs0vZR',
  project='proj_prYaLbRaVOCoPf9BCHZlxA99',
)

response = client.chat.completions.create(
    messages=[{
        "role": "user",
        "content": "Say this is a test",
    }],
    model="gpt-4o-mini",
)

print(response._request_id)
