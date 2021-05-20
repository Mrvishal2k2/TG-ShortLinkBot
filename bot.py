'''
© All rights reserved by Mrvishal2k2

Kangers dont f*ckin kang this !!!
Should have to give credits 😏 else f***off 
This is only for personal use Dont use this for ur bot channel business 😂
Thanks to Mahesh Malekar for his Gplinks Bot !!
'''
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyshorteners import Shortener
from config import *


SHORTLINKBOT = Client('ShortlinkBot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)
             
             

@SHORTLINKBOT.on_message(filters.command(['start','help']))
async def start(bot, update):
    markup = InlineKeyboardMarkup([[InlineKeyboardButton("My Owner 👮", url=f"https://t.me/{OWNER}")]])
    await update.reply(
        f"**Hi {update.chat.first_name}!**\n\n"
        "I'm shortlink bot. Just send me link and get adsless short link",
        reply_markup=markup,
        quote=True)

@SHORTLINKBOT.on_message(filters.regex(r'https?://[^\s]+'))
async def link_handler(_, update):
    link = update.matches[0].group(0)
    shortened_url, Err = get_shortlink(link)
    if shortened_url is None:
        message = f"Something went wrong \n{Err}"
        await update.reply(message, quote=True)
        return
    message = f"Here is your shortlink\n {shortened_url}"
    markup = InlineKeyboardMarkup([[InlineKeyboardButton("Link 🔗", url=shortened_url)]])
    # i don't think this bot with get sending message error so no need of exceptions
    await update.reply_text(text=message, reply_markup=markup, quote=True)
      
def get_shortlink(url):
    shortened_url = None
    Err = None
    try:
       if API_KEY:
           ''' Cuttly Shorten'''
           s = Shortener(api_key=API_KEY)
           shortened_url = s.cuttly.short(link)
       else:
           ''' Da.gd : I prefer this '''
           s = Shortener()
           shortened_url = s.dagd.short(link)
    except Exception as error:
        Err = f"#ERROR: {error}"
        log.info(Err)
    return shortened_url,Err
        
        
if __name__ == "__main__" :
    SHORTLINKBOT.run()
