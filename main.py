# Ts-Bots


import os
import pytz
import time
import datetime

from pyrogram import Client

user_session_string = os.environ.get("user_session_string")
bots = [i.strip() for i in os.environ.get("bots").split(' ')]
update_channel = os.environ.get("update_channel")
status_message_ids = [int(i.strip()) for i in os.environ.get("status_message_id").split(' ')]
api_id = int(os.environ.get("api_id"))
api_hash = os.environ.get("api_hash")
user_client = Client(session_name=str(user_session_string), api_id=api_id, api_hash=api_hash)


def main():
    with user_client:
        while True:
            print("[INFO] starting to check uptime..")
            edit_text = f"🦋 ʀɪᴢᴀᴅ's  ʙᴏᴛ sᴛᴀᴛᴜs ッ\n\n__( All bots are checked automatically if any correction report it )__\n\n\n"
            for bot in bots:
                print(f"[INFO] checking @{bot}")
                snt = user_client.send_message(bot, '/start')

                time.sleep(15)

                msg = user_client.get_history(bot, 1)[0]
                if snt.message_id == msg.message_id:
                    print(f"[WARNING] @{bot} is down")
                    edit_text += f"𝙱𝙾𝚃 𝙽𝙰𝙼𝙴    {bot} \n𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴  @{bot}\n𝚂𝚃𝙰𝚃𝚄𝚂 ❌\n\n"
                    #user_client.send_message("me",
                                             #f"@{bot} was down")
                else:
                    print(f"[INFO] all good with @{bot}")
                    edit_text += f"𝙱𝙾𝚃 𝙽𝙰𝙼𝙴    {bot} \n𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴  @{bot}\n𝚂𝚃𝙰𝚃𝚄𝚂 ✅\n\n"
                user_client.read_history(bot)

            time_now = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            formatted_time = time_now.strftime("%d %B %Y %I:%M %p")

            edit_text += f"**Updated on {formatted_time} (IST)**"

            for status_message_id in status_message_ids:
                user_client.edit_message_text(int(update_channel), status_message_id,
                                         edit_text)
                time.sleep(5)
            print(f"[INFO] everything done! sleeping for 3 hours...")

            time.sleep(864000)


if __name__ == "__main__":
   main()
