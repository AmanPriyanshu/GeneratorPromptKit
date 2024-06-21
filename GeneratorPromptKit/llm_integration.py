import json
import time

def send_query2gpt(client, llm_model, messages, function_template=None, temperature=0, pause=5):
    if function_template is not None:
        response = client.chat.completions.create(
            model=llm_model,
            messages=messages,
            temperature=temperature,
            max_tokens=512,
            functions=[function_template], 
            seed=0,
            function_call={"name": function_template["name"]}
        )
        answer = response.choices[0].message.function_call.arguments
        generated_response = json.loads(answer)
        time.sleep(pause)
        return generated_response
    else:
        response = client.chat.completions.create(
            model=llm_model,
            messages=messages,
            temperature=temperature,
            max_tokens=512,
            seed=0,
        )
        answer = response.choices[0].message.content
        time.sleep(pause)
        return answer