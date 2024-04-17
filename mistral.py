import subprocess
from os import environ

OPENAI_API_BASE = environ.get("OPEN_AI_API_KEY")
CHATGPT_SUBSCRIPTION_ID = environ.get("MISTRAL_API_KEY")


def get_mistral_request(mode: str):
    if mode == "query":
        return """curl --location "https://api.mistral.ai/v1/chat/completions" \
             --header 'Content-Type: application/json' \
             --header 'Accept: application/json' \
             --header "Authorization: Bearer $MISTRAL_API_KEY" \
             --data '{
            "model": "mistral-tiny",
            "messages": [{"role": "user", "content": "Who is the most renowned French 
            painter?"}]
          }"""
    elif mode == "embedding":
        return """curl --location "https://api.mistral.ai/v1/embeddings" \
             --header 'Content-Type: application/json' \
             --header 'Accept: application/json' \
             --header "Authorization: Bearer $MISTRAL_API_KEY" \
             --data '{
            "model": "mistral-embed",
            "input": ["Embed this sentence.", "As well as this one."]
          }"""
    else:
        raise ValueError(f"Wrong mode given: {mode}")


curl_command = get_mistral_request("query")

curl_command = get_mistral_request("embedding")

process = subprocess.Popen(curl_command, stdout=subprocess.PIPE, shell=True)
output, error = process.communicate()
