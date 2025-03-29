from notion_client import Client
notion = Client(auth="API_KEY")
page_id = "557885410ce143b0a5305ed6cd46572e"
page_content = notion.blocks.children.list(page_id)
def extract_text(blocks):
    """Extracts plain text from Notion blocks""""
    try:
        if 'results' not in blocks:
            return ""
        return ''.join(
            t['plain_text']
            for block in blocks['results']
            if block.get('type') == 'paragraph' and 'text' in block['paragraph']
            for t in block['paragraph'].get['text',[]]
        )
    except Exception as e:
        print(f"Error inside extract_text: {e}")
        return ''

client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_KEY")
)
def summarize(text):
    text = extract_text(page_id)
    try:
        response = client.chat.completion.create(
            model = 'whisper-large-v3',
            message = [
                    {"role": "system", "content": "You are a helpful quiz question generator."},
                    {"role": "user", "content": f'Summerize this: {text}'},
                ]
                return response.choices[0].message.content.strip()
        )
    except Exception as e:
        return f'error generating question {e}'