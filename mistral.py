import subprocess
from os import environ

# Load API keys from environment variables
OPENAI_API_KEY = environ.get("OPENAI_API_KEY")
MISTRAL_API_KEY = environ.get("MISTRAL_API_KEY")

def get_mistral_request(mode: str) -> str:
    """
    Generates the appropriate curl command for Mistral API requests based on the mode.

    Args:
        mode (str): The type of request to make, either 'query' or 'embedding'.

    Returns:
        str: The curl command to be executed for the API request.

    Raises:
        ValueError: If an unsupported mode is provided.
    """
    if not MISTRAL_API_KEY:
        raise EnvironmentError("MISTRAL_API_KEY is not set in environment variables.")

    if mode == "query":
        return f"""curl --location "https://api.mistral.ai/v1/chat/completions" \
             --header 'Content-Type: application/json' \
             --header 'Accept: application/json' \
             --header "Authorization: Bearer {MISTRAL_API_KEY}" \
             --data '{{
                "model": "mistral-tiny",
                "messages": [{{"role": "user", "content": "Who is the most renowned French painter?"}}]
             }}'"""
    elif mode == "embedding":
        return f"""curl --location "https://api.mistral.ai/v1/embeddings" \
             --header 'Content-Type: application/json' \
             --header 'Accept: application/json' \
             --header "Authorization: Bearer {MISTRAL_API_KEY}" \
             --data '{{
                "model": "mistral-embed",
                "input": ["Embed this sentence.", "As well as this one."]
             }}'"""
    else:
        raise ValueError(f"Invalid mode provided: {mode}. Supported modes are 'query' and 'embedding'.")

def execute_curl_command(mode: str):
    """
    Executes the curl command for the specified mode and returns the output.

    Args:
        mode (str): The mode for the API request, either 'query' or 'embedding'.

    Returns:
        str: The output from the curl command, or an error message if it fails.
    """
    curl_command = get_mistral_request(mode)
    process = subprocess.Popen(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    if process.returncode != 0:
        raise RuntimeError(f"Error executing curl command: {error.decode('utf-8')}")
    
    return output.decode('utf-8')

# Example usage:
try:
    print("Query Request Output:")
    print(execute_curl_command("query"))

    print("\nEmbedding Request Output:")
    print(execute_curl_command("embedding"))
except Exception as e:
    print(f"An error occurred: {e}")
