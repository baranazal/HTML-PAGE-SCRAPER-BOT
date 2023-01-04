# Web Scraper Bot

A Telegram bot that can scrape and send web pages to users.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need the following packages:

- requests
- beautifulsoup4
- python-telegram-bot

You can install these packages using pip:

```
pip install requests beautifulsoup4 python-telegram-bot
```

### Installing

Clone the repository to your local machine:

```
git clone https://github.com/your-username/web-scraper-bot.git
```

Or you can download it manually 

You will also need to replace "YOUR_TOKEN" with your actual Telegram bot token in the code. You can obtain a bot token by talking to the @BotFather bot on Telegram and following the instructions here : https://t.me/botfather . 


Then run the following command:

```
python main.py
```


The bot should now be running and listening for updates.

## Usage

To use the bot, send a message in the following format to your bot:

```
/scrape https://www.example.com
```


The bot will scrape the page at the specified URL and send the page content to you as a file.

## Built With

- [requests](https://pypi.org/project/requests/) - Used to send HTTP requests
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) - Used to parse HTML
- [python-telegram-bot](https://pypi.org/project/python-telegram-bot/) - Used to interact with the Telegram API

## Contributing

If you would like to contribute to this project, please create a fork and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


