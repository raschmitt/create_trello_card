import os
import argparse
import requests

TRELLO_API_KEY = os.getenv("TRELLO_API_KEY")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")

def create_trello_card(name, list_id, template_card_id):
    """Creates a new Trello card using a template."""
    url = f"https://api.trello.com/1/cards"
    
    params = {
        "name": name,
        "idList": list_id,
        "idCardSource": template_card_id,
        "key": TRELLO_API_KEY,
        "token": TRELLO_TOKEN
    }
    
    response = requests.post(url, params=params)
    
    if response.status_code == 200:
        card_data = response.json()
        print(f"✅ Successfully created Trello card: {card_data['name']} (ID: {card_data['id']})")
    else:
        print(f"❌ Error creating Trello card: {response.text}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new Trello card from a template.")
    parser.add_argument("name", help="Name of the new Trello card")
    parser.add_argument("list_id", help="Trello List ID where the card will be created")
    parser.add_argument("template_card_id", help="Trello Card ID of the template")
    
    args = parser.parse_args()
    
    create_trello_card(args.name, args.list_id, args.template_card_id)
