from flask import Flask
from dotenv import load_dotenv

# Load environment variables (e.g., Telegram bot token, chat ID) from .env
load_dotenv()

app = Flask(__name__)

# Import routes so all view functions are registered.
# These routes now only use static data and do not depend on any database.
import routes  # noqa: E402,F401


if __name__ == "__main__":
    app.run()
