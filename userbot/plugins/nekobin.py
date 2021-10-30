



import asyncio

from core import COMMAND_HELP, HNDLR, vision

from core import app



from core.data_mongo.modesdb import user_mode

from pyrogram.types import Message



@vision.on("spam")

async def spam(client, message: Message):

    if await user_mode() == "Friendly":

        return await message.edit("**Kindly Disable friendly mode to use this command**")

    txt = message.text

    a="something"

    try:

        if  message.reply_to_message:

         a=None

        else: 

         file={'file': txt.split()[1],'type':"text"}

    except IndexError:

        txt=None

        await message.edit(

            "**Syntax** : {HNDLR}spam <reply to image/video/gif> or <give text>"

        )

    number=None

    try:

        if message.reply_to_message:

            number=int(txt.split()[2])

        else:

            

         number=int(txt.split()[3])

    except IndexError:



        pass

    limit=5

    try:

        if message.reply_to_message:

            

         limit=int(txt.split()[1])

        else:

            

         limit=int(txt.split()[2])

    except IndexError:

        pass

    

    if not a:

        if message.reply_to_message:

            a=message.reply_to_message

            

            if a.sticker:

                file = {"file": a.sticker.file_id,"type":"sticker"}

            elif a.photo:

                file={"file":a.photo.file_id,"type": 'photo'}

            elif a.video:

                file={'file':a.video.file_id,'type' :"video"}

            elif a.animation:

                file={"file": a.animation.file_id,"type": "gif"}

            elif a.text:

                file={"file":a.text,"type":"text"}

            else:

                return await message.edit("**Invalid document**")

            

    if file:

      typeOf=file.get("type")

      f=file.get("file")

      for i in range(int(limit)) :

        if typeOf == "sticker":

        

            await app.send_sticker(message.chat.id,file.get("file"))

        elif typeOf == "video":

            await app.send_video(message.chat.id,video=file.get('file'))

        elif typeOf == "photo":

            await app.send_photo(message.chat.id,photo=f)

        elif typeOf == "gif":

            await app.send_animation(message.chat.id,animation=f)

        elif typeOf == "text":

            await app.send_message(message.chat.id,f)

        if number:

            await asyncio.sleep(int(number))

            

            

            

COMMAND_HELP.update({

    "spam": f'''`{HNDLR}spam` __<txt> <spam limit>__ | <reply to message/sticker/gifs/text> or <give text>

    

    

**FOR DELAY SPAM** : `{HNDLR}spam` __<text/replytomessage text> <number of limit> <sleep limit>__   



    

''',

"spam's help": "__Spam given text/media/stickers in a chat__"

})
