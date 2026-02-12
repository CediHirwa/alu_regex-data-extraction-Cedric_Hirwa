import re
import json
import os

def run_extraction_tool(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    with open(file_path, 'r') as file:
        raw_data = file.read()

    print(f"--- Processing Data from: {file_path} ---\n")

    html_pattern = r'<[^>]*>'
    clean_text = re.sub(html_pattern, "[SECURITY_STRIPPED]", raw_data)

    patterns = {
        "emails": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        "urls": r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',
        "credit_cards": r'\b(?:\d{4}[-\s]?){3}\d{4}\b',
        "currency": r'(?:[\$\€\£]\s?\d+(?:,\d{3})*(?:\.\d{2})?)|(?:\b\d+(?:,\d{3})*(?:\.\d{2})?\s?(?:RWF|USD|EUR|GBP)\b)'
    }

    results = {
        "emails": list(set(re.findall(patterns["emails"], clean_text))), 
        "urls": re.findall(patterns["urls"], clean_text),
        "currency": re.findall(patterns["currency"], clean_text),
        "masked_credit_cards": []
    }

    raw_cards = re.findall(patterns["credit_cards"], clean_text)
    for card in raw_cards:
        digits = re.sub(r'\D', '', card) 
        results["masked_credit_cards"].append(f"****-****-****-{digits[-4:]}")

    with open('output.json', 'w') as out_file:
        json.dump(results, out_file, indent=4)
    
    print("Extraction complete. Results saved to 'output.json'.")
    return results

if __name__ == "__main__":
    extracted = run_extraction_tool("sample_input.txt")
    if extracted:
        print(json.dumps(extracted, indent=4))
