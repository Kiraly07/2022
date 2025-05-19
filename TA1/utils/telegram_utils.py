import json
import requests

def send_telegram_alert(message, config_path="telegram_config.json"):
    """Send an alert message to Telegram."""
    try:
        with open(config_path, "r") as config_file:
            config = json.load(config_file)
        bot_token = config.get("TELEGRAM_BOT_TOKEN")
        chat_id = config.get("TELEGRAM_CHAT_ID")
        if not bot_token or not chat_id:
            print("Telegram configuration is missing.")
            return

        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message
        }
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            print(f"Failed to send Telegram message: {response.text}")
    except FileNotFoundError:
        print("Telegram configuration file not found.")
    except Exception as e:
        print(f"Error sending Telegram message: {e}")

def configure_telegram(bot_token, chat_id, config_path="telegram_config.json"):
    """Save Telegram bot configuration."""
    config = {
        "TELEGRAM_BOT_TOKEN": bot_token,
        "TELEGRAM_CHAT_ID": chat_id
    }
    try:
        with open(config_path, "w") as config_file:
            json.dump(config, config_file, indent=4)
        return True
    except Exception as e:
        print(f"Error saving Telegram configuration: {e}")
        return False