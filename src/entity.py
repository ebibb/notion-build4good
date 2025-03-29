from notion_client import Client
notion = Client(auth="API_KEY")
page_id = "557885410ce143b0a5305ed6cd46572e"
page_content = notion.blocks.children.list(page_id)
