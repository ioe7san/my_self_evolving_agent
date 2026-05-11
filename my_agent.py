import json

def get_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"status": "default"}

def process_query(query):
    config = get_config()
    return f"الوكيل يعالج الأمر: {query} بناءً على التكوين الحالي."
