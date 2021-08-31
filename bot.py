'''
© All rights reserved by Mrvishal2k2

Kangers dont f*ckin kang this !!!
Should have to give credits 😏 else f***off 
This is only for personal use Dont use this for ur bot channel business!!!
'''

# Bitly Bot

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
async def start(_, update):
    await update.reply(
        f"**Hi {update.chat.first_name}!**\n\n"
        "I'm Bitly shortlink bot. Just send me link and get adsless short link",
        reply_markup=InlineKeyboardMarkup(
              [[InlineKeyboardButton("My Owner 👮", url=f"https://t.me/{OWNER}")]]),
        quote=True)


@SHORTLINKBOT.on_message(filters.regex(r'https?://[^\s]+'))
async def link_handler(_, update):
    link = update.matches[0].group(0)
    shortened_url, Err = get_shortlink(link)

    if not shortened_url:
        return await update.reply(f"Something went wrong \n{Err}", quote=True)

    await update.reply(
        text=f"Here is your shortlink\n {shortened_url}",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Link 🔗", url=shortened_url)]]),
        quote=True)
      
def get_shortlink(url):
    shortened_url,Err = False, False

    try:

       if BITLY_KEY:
           ''' Bittly Shorten'''
           shortened_url = Shortener(api_key=BITLY_KEY).bitly.short(url)
       else:
           ''' Da.gd : I prefer this '''
           shortened_url = Shortener().dagd.short(url)

    except Exception as error:
        Err = f"#ERROR: {error}"
        log.error(Err)
    return shortened_url,Err
        
        
if __name__ == "__main__" :
    log.info(">>Bot-Started<<")
    SHORTLINKBOT.run()
