import requests
from bs4 import BeautifulSoup
import re
from telegram.ext import Updater, CommandHandler


def get_page(url):
  # Send a GET request to the Website URL starts with http or https
  response = requests.get(url)

  # Parse the response
  soup = BeautifulSoup(response.text, 'html.parser')

  # Return the page content
  return soup.prettify()


def send_page(update, context):
  # Extract the URL from the user's message
  pattern = r'https?://[^\s<>"]+|(?:www\.)[^\s<>"]+'
  urls = re.findall(pattern, update.message.text)

  # Check if a URL was found
  if not urls:
    update.message.reply_text('No URL was found in your message')
  else:
    # Get the first URL
    url = urls[0]

    # Add https:// to the URL if it does not start with http:// or https://
    if not url.startswith('http://') and not url.startswith('https://'):
      url = 'https://' + url

    # Get the page content
    page = get_page(url)

    # Save the page content to a file
    with open('page.html', 'w') as file:
      file.write(page)

    # Send the file to the user
    context.bot.send_document(update.message.chat_id, open('page.html', 'rb'))


def main():
  # Create the Updater and attach the send_page function to the '/scrape' command
  updater = Updater('YOUR_TOKEN',
                    use_context=True)
  updater.dispatcher.add_handler(CommandHandler('scrape', send_page))

  # Start the bot
  updater.start_polling()
  updater.idle()


if __name__ == '__main__':
  main()
