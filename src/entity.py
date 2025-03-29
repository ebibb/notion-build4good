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

