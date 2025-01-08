# Voice_assistant_using_Retellai

![image](https://github.com/user-attachments/assets/18b35121-a8e7-4e85-aea5-6ae7cfde67ca)

Task: 
API integration: using Retellai.com to build an MVP of voice agent platform that support voice options = LLM(openai/deep seek) + transcription model(deepgram/talkscriber + voice model(11labs/deep gram/cartesia) to generate a real time voice agent. 

I’m using Make.com to automate the process and connect different tools like Deepgram, OpenAI, and 11labs.
1.	When I speak, the audio is sent through a Webhook to Deepgram, which converts it into text.
2.	The text is then sent to OpenAI to generate a relevant response.
3.	Finally, the response is sent to 11labs, which turns the text into natural-sounding speech, and the assistant speaks back to me.
Make.com ties it all together, making the workflow smooth and automated. This way, the assistant understands my voice, processes it, and responds with speech.

