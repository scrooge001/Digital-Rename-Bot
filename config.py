import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # digital_botz client config
    API_ID = os.environ.get("API_ID", "")
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

    # premium account string session required 😢 
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    
    # database config
    DB_NAME = os.environ.get("DB_NAME","Cluster0")     
    DB_URL = os.environ.get("DB_URL","")
 
    # other configs
    RKN_PIC = os.environ.get("ADGPic", "https://telegra.ph/file/b746aadfe59959eb76f59.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6705898491').split()]
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002123429361"))

    #force subs
    try:
        FORCE_SUB = int(os.environ.get("FORCE_SUB", "")) 
    except:
        FORCE_SUB = os.environ.get("FORCE_SUB", "Digital_Botz")
        
    # wes response configuration     
    PORT = int(os.environ.get("PORT", "8080"))
    BOT_UPTIME = time.time()

class rkn(object):
    # part of text configuration
    START_TXT = """<b>Ｈ𝙰𝙸, {}👋

𝚃ʜɪs 𝙸s 𝙰ɴ 𝙰ᴅᴠᴀᴄᴇᴅ 𝙰ɴᴅ 𝚈ᴇᴛ 𝙿ᴏᴡᴇʀғᴜʟ 𝚁ᴇɴᴀᴍᴇ 𝙱ᴏᴛ
𝚄sɪɴɢ 𝚃ʜɪs 𝙱ᴏᴛ 𝚈ᴏᴜ 𝙲ᴀɴ 𝚁ᴇɴᴀᴍᴇ & 𝙲ʜᴀɴɢᴇ 𝚃ʜᴜᴍʙɴᴀɪʟ 𝙾ғ 𝚈ᴏᴜʀ 𝙵ɪʟᴇ 
𝚈ᴏᴜ 𝙲ᴀɴ 𝙰ʟsᴏ 𝙲ᴏɴᴠᴇʀᴛ 𝚅ɪᴅᴇᴏ 𝚃ᴏ 𝙵ɪʟᴇ & 𝙵ɪʟᴇ 𝚃ᴏ 𝚅ɪᴅᴇᴏ
𝚃𝙷𝙸𝚂 𝙱𝙾𝚃 𝙰𝙻𝚂𝙾 𝚂𝚄𝙿𝙿𝙾𝚁𝚃𝚂 𝙲𝚄𝚂𝚃𝙾𝙼 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻 𝙰𝙽𝙳 𝙲𝚄𝚂𝚃𝙾𝙼 𝙲𝙰𝙿𝚃𝙸𝙾𝙽

Tʜɪs Bᴏᴛ Wᴀs Cʀᴇᴀᴛᴇᴅ Bʏ : @Scrooge010 💞</b>"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 ᴍy ɴᴀᴍᴇ : {}
├🖥️ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : <a href=https://t.me/scrooge010>ScroogeX</a> 
├👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/scrooge010>ScroogeX</a>
├📕 Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
├✏️ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pyᴛʜᴏɴ 3</a>
├💾 Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>
├📊 ᴠᴇʀsɪᴏɴ: 1.0</a></b>     
╰───────────────⍟ """

    HELP_TXT = """
<b>•></b> /start Tʜᴇ Bᴏᴛ.

✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>•></b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nɴᴀᴍᴇ \nAɴᴅ Aᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].           
ℹ️ 𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/scrooge010>CONTACT ADMIN</a>
"""

    UPGRADE= """
•⪼ ★𝘗𝘭𝘢𝘯𝘴     -    ⏳𝘋𝘢𝘵𝘦 -  💸𝘗𝘳𝘪𝘤𝘦 
•⪼ 🥉𝘉𝘳𝘰𝘯𝘻𝘦   -     3𝘥𝘢𝘺𝘴 -    100
•⪼ 🥈𝘚𝘪𝘭𝘷𝘦𝘳    -     7𝘥𝘢𝘺𝘴 -    200
•⪼ 🥇𝘎𝘰𝘭𝘥     -    15𝘥𝘢𝘺𝘴 -   300
•⪼ 🏆𝘗𝘭𝘢𝘵𝘪𝘯𝘶𝘮  -    1𝘮𝘰𝘯𝘵𝘩 -   400
•⪼ 💎𝘋𝘪𝘢𝘮𝘰𝘯𝘥  -    2𝘮𝘰𝘯𝘵𝘩 -   600

- 𝘋𝘢𝘪𝘭𝘺 𝘜𝘱𝘭𝘰𝘢𝘥 𝘓𝘪𝘮𝘪𝘵 𝘜𝘯𝘭𝘪𝘮𝘪𝘵𝘦𝘥
- 𝘋𝘪𝘴𝘤𝘰𝘶𝘯𝘵 𝘈𝘭𝘭 𝘗𝘭𝘢𝘯 𝘙𝘴.500
    """
    THUMBNAIL = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ</u></b>

<b>•></b> Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ.
"""
    CAPTION= """
📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>

<b>•></b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ

Exᴀᴍᴩʟᴇ:- `/set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}`
"""
    BOT_STATUS = """
⚡️ ʙᴏᴛ sᴛᴀᴛᴜs ⚡️

⌚️ ʙᴏᴛ ᴜᴩᴛɪᴍᴇ: `{}`
👭 ᴛᴏᴛᴀʟ ᴜsᴇʀꜱ: `{}`
💸 ᴛᴏᴛᴀʟ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs: `{}`
֍ ᴜᴘʟᴏᴀᴅ: `{}`
⊙ ᴅᴏᴡɴʟᴏᴀᴅ: `{}`
"""
    LIVE_STATUS = """
⚡ ʟɪᴠᴇ sᴇʀᴠᴇʀ sᴛᴀᴛᴜs ⚡

ᴜᴘᴛɪᴍᴇ: `{}`
ᴄᴘᴜ: `{}%`
ʀᴀᴍ: `{}%` 
ᴛᴏᴛᴀʟ ᴅɪsᴋ: `{}`
ᴜsᴇᴅ sᴘᴀᴄᴇ: `{} {}%`
ғʀᴇᴇ sᴘᴀᴄᴇ: `{}`
ᴜᴘʟᴏᴀᴅ: `{}`
ᴅᴏᴡɴʟᴏᴀᴅ: `{}`
V1.𝟶.𝟶 [STABLE]
"""
    DIGITAL_METADATA = """
❪ SET CUSTOM METADATA ❫

- /metadata - Tᴏ Sᴇᴛ & Cʜᴀɴɢᴇ ʏᴏᴜʀ ᴍᴇᴛᴀᴅᴀᴛᴀ ᴄᴏᴅᴇ

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @adgmovies" -metadata author="@scrooge010" -metadata:s:s title="Subtitled By :- @adgmovies" -metadata:s:a title="By :- @adgmovies" -metadata:s:v title="By:- @scrooge010" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @scrooge010
"""
    
    CUSTOM_FILE_NAME = """
<u>🖋️ Custom File Name</u>

you can pre-add a prefix and suffix along with your new filename

➢ /set_prefix - To add a prefix along with your _filename.
➢ /see_prefix - Tᴏ Sᴇᴇ Yᴏᴜʀ Pʀᴇғɪx !!
➢ /del_prefix - Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Pʀᴇғɪx !!
➢ /set_suffix - To add a suffix along with your filename_.
➢ /see_suffix - Tᴏ Sᴇᴇ Yᴏᴜʀ Sᴜғғɪx !!
➢ /del_suffix - Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Sᴜғғɪx !!

Exᴀᴍᴩʟᴇ:- `/set_suffix @ADGMOVIES`
Exᴀᴍᴩʟᴇ:- `/set_prefix @ADGMOVIES`
"""
    
    DEV_TXT = """<b><u>Sᴩᴇᴄɪᴀʟ Tʜᴀɴᴋꜱ & Dᴇᴠᴇʟᴏᴩᴇʀꜱ</b></u>
    
» 𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘 : <a href=https://t.me/scrooge010>ScroogeX</a>

• ❣️ <a href=https://t.me/scrooge010>Developer</a>"""
    # ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️

    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @adgmovies" -metadata author="@scrooge010" -metadata:s:s title="Subtitled By :- @adgmovies" -metadata:s:a title="By :- @adgmovies" -metadata:s:v title="By:- @scrooge010" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @adgmovies
"""
    
    RKN_PROGRESS = """<b>\n
╭━━━━❰RKN PROCESSING...❱━➣
┣⪼ 🗃️ ꜱɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ ᴅᴏɴᴇ : {0}%
┣⪼ 🚀 ꜱᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ ᴇᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""

