from pyrogram import Client, Message, Filters, Emoji


@Client.on_message(Filters.new_chat_members & Filters.chat("CityofAddu"))
async def new_chat_members(c: Client, m: Message):
    mentions = f"<a href='tg://user?id={m.from_user.id}'>{m.from_user.first_name}</a>"
    welcome_msg = "{} Welcome to <a href='https://t.me/CityofAddu'>AdduCity Group</a>'s group chat! Keep your " \
                  "calm and enjoy the chat."

    new_members = [mentions.format(i.first_name, i.id) for i in m.new_chat_members]
    text = welcome_msg.format(Emoji.MAN_RAISING_HAND_DARK_SKIN_TONE, ", ".join(new_members))

    await m.reply_text(
        text=text,
        parse_mode="html"
    )
