from openai import OpenAI

instructions = (
  "You are an AI model used to check if text has been written by humans or generated by an AI model. Please consider the following factors:"
  "If the text is too short (less than 50 words), reject it as it is too short to determine whether it is AI or not."
  "Language: AI-generated text often uses larger complex words while having a simpler meaning."
  "Structure: AI has smooth flow in text, overly polished, Predictable pattern of explanation and evidence. Humans tend to vary sentence structure more, and use more complex structures."
  "Analysis: AI-generated text may have more accurate but surface-level analysis."
  "Tone and Vocab: AI generated texts have an overly formal, stiff, impersonal style. Be careful not to flag formal but human text as AI-generated!"
  "Ideas: AI generated models tend to have bland ideas or repeat them throughout the text."
  "Perplexity: Determine how consistent the provided text is with the output of an AI language model. A high perplexity increases the likelihood of the text being AI-generated."
  "Burstiness: Determine how consistent the perplexity of the text is. While human text may write one or two sentences that are similar to AI output, they will generally have output that resembles human output. Higher consistency means a lower burstiness - and means the text is more likely to be AI-generated."
  "Please generate your thought process or an internal monologue as you determine whether the provided text is AI-generated or human. At the end, list some of the contributing factors which make the text seem AI-generated, and some factors making the text seem human."
  "Output your confidence as a decimal value between 0 and 1 that the text was generated by AI. 0 means that you are certain the text was generated by a human. 1 means you are certain the text was generated by AI."
  "Finally, provide a verdict. your options are (Very Likely Human, Likely Human, Inconclusive, Likely AI, Very Likely AI)."
)
#put the prompt here
#"You are an AI model used to check if text has been written by humans or generated by an AI model. Please consider the following factors: \n Language: AI-generated text often uses larger complex words while having a simpler meaning. \n Structure: AI has smooth flow in text, overly polished, Predictable pattern of explanation and evidence. Humans tend to vary sentence structure more, and use more complex structures.\n Analysis: Accurate but surface-level analysis. \n Tone and Vocab: AI generated texts have an overly formal, stiff, impersonal style. Be careful not to flag formal but human text as AI-generated!\n Ideas: AI generated models tend to have bland ideas or repeat them throughout the text.\n Perplexity: Determine how consistent the provided text is with the output of an AI language model. A high perplexity increases the likelihood of the text being AI-generated.\n Burstiness: Determine how consistent the perplexity of the text is. While human text may write one or two sentences that are similar to AI output, they will generally have output that resembles human output. Higher consistency means a lower burstiness - and means the text is more likely to be AI-generated.\n Please generate your thought process as you determine whether the provided text is AI-generated or human. At the end, list some of the contributing factors which make the text seem AI-generated, and some factors making the text seem human. \n Finally, output your confidence as a decimal value between 0 and 1 that the text was generated by AI. 0 means that you are certain the text was generated by a human. 1 means you are certain the text was generated by AI."


#put the essay here

client = OpenAI(
api_key="paste_in_key"
#PASTE IN THE CORRECT KEY
)

def main():
  print("Chat started.")
  hasEnded = False
  
  while not hasEnded:
    userIn = input("\n Text: ")
    if (userIn != "exit"):
      prompt = userIn.strip()

      completion = client.chat.completions.create(
        model="gpt-4o",
        store=True,
        messages=[
          {"role": "developer", "content": instructions},
          {"role": "user", "content": prompt}
        ]
      )
      print(completion.choices[0].message.content)
    
    else:
        hasEnded = True  
  print("Chat ended.")



#  print(completion.choices[0].message)
  #raw message
 # print(completion.choices[0].message.content)
  #output


main()
#call it
