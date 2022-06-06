#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✅**<u>اوامر الادمن:</u>**

قبل الامر لتنفيذه في القناة **c** ضع.
/pause - لإيقاف تشغيل الموسيقى مؤقتًا 
/resume or /cresume- استئناف الموسيقى المتوقفة مؤقتًا.
/mute or /cmute- كتم صوت الموسيقى قيد التشغيل.
/unmute or /cunmute- إعادة صوت الموسيقى الصامتة.
/skip or /cskip- تخطي الموسيقى قيد التشغيل الحالية.
/stop or /cstop- أوقف تشغيل الموسيقى.
/shuffle or /cshuffle- ترتيب عشوائي لقائمة التشغيل في قائمة الانتظار
/restart - أعد تشغيل البوت لمحادثتك.
✅<u>**تخطي محدد:**</u>
/skip or /cskip [رقم(مثال: 3)] 
    - يتخطى الموسيقى إلى الرقم المحدد في قائمة الانتظار. مثال: /skip 3 سيتخطى الموسيقى إلى الموسيقى في قائمة الانتظار الثالثة وسيتجاهل الموسيقى 1 و 2 في قائمة الانتظار. 
✅<u>**حلقة التشغيل:**</u>
/loop او /cloop [Enable/disable] او [أرقام بين 1-10] 
    - عند التنشيط ، يقوم البوت بتكرار تشغيل الموسيقى الحالية إلى 1-10 مرات في الدردشة الصوتية. افتراضي إلى 10 مرات.
✅<u>**المستخدمون المعتمدون:**</u>
يمكن للمستخدمين المعتمدين استخدام أوامر المسؤول بدون رتبة الاشراف في الدردشة.
/auth [اسم المستخدم] - أضف مستخدمًا إلى قائمة المعتمدين بالمجموعة.
/unauth [اسم المستخدم] - قم بإزالة مستخدم من قائمة المعتمدين بالمجموعة.
/authusers - احضار قائمه المعتمدين."""


HELP_2 = """✅<u>**اوامر التشغيل:**</u>

الاوامر المتوفرة = play , vplay , cplay

ForcePlay اوامر = playforce , vplayforce , cplayforce

**c** لتشغيل في قناة.
**v** لتشغيل فيديو.

/play or /vplay or /cplay  - Bot will start playing your given query on voice chat or Stream live links on voice chats.

/channelplay [يوزر القناة او الايدي] او [Disable] - اربط قناتك في مجموعتك وابدأ تشغيل الاغاني في القناة من خلال مجموعتك.


✅**<u>اوامر فوائم التشغيل :</u>**
/playlist  - تحقق من قائمة التشغيل المحفوظة على الخوادم.
/deleteplaylist - احذف أي موسيقى محفوظة في قائمة التشغيل الخاصة بك
/play  - ابدأ تشغيل قائمة التشغيل المحفوظة من الخوادم."""


HELP_3 = """✅<u>**اوامر البوت:**</u>

/stats - احصل على أفضل 10 اغاني للإحصائيات العالمية ، أفضل 10 مستخدمين للروبوت ، أفضل 10 محادثات على الروبوت ، أفضل 10 تم تشغيلها في محادثة ، إلخ.
/sudolist - تحقق من المطورين 
/lyrics [اسم الاغنية] - لجلب كلمات الاغنية من الويب.
/song [اسم المقطع] او [الرابط] - قم بتنزيل أي مقطع صوتي من بتنسيقات mp3 أو mp4.
/player -  احصل على لوحة لعب تفاعلية.
/queue or /cqueue-تحقق من قائمة انتظار الموسيقى."""

HELP_4 = """✅<u>**اوامر اضافية:**</u>
/start - بدأ تشغيل البوت.
/help  - للمساعدة في اوامر البوت .
/ping- معرفة سرعة البوت .

✅<u>**اعدادات المجموعة:**</u>
/settings - Get a complete group's settings with inline buttons

🔗 **الخيارات:**

1️⃣ يمكنك ضبط ** Audio quality ** التي تريد بثها على الدردشة الصوتية..

2️⃣ يمكنك ضبط **Video Quality** التي تريد بثها في الاتصال .

3️⃣ **المعتمدين**:- يمكنك تغيير وضع أوامر المسؤول من هنا للجميع أو للمسؤولين فقط.  إذا كان كل شخص موجودًا في مجموعتك ، فسيكون قادرًا على استخدام أوامر المسؤول (like /skip, /stop etc)

4️⃣ **وضع التنظيف:** عند التمكين ، يحذف رسائل الروبوت بعد 5 دقائق من مجموعتك للتأكد من بقاء محادثتك نظيفة وجيدة.

5️⃣ **تنظيف الاوامر** : عند التمكين سيحذف الاوامر المعطاة له مباشرة من الادمن بعد تنفيذها مثل  (/play, /pause, /shuffle, /stop etc) immediately.

6️⃣ **اعدادات التشغيل:**

/playmode - احصل على لوحة إعدادات تشغيل كاملة مع أزرار حيث يمكنك ضبط إعدادات تشغيل مجموعتك. 

<u>الخيارات فيها:</u>

1️⃣ **وضع البحث** [مباشر او انلاين] - غير حسب ما تريده من ترسل الامر  /play . 

2️⃣ **اوامر الادمن** [الجميع لو بس الادمن ] - اذا الحميع راح الكل يكدر يستخدم الاوامر اما اذا الادمنز بس يعني المشرفين فقط يتحكمون باوامر (like /skip, /stop etc)

3️⃣ **اوامر التشغيل** [الكل لو الادمن ] - اذا ادمن بس الادمنية يكدرون يشغلون الاغاني اما اذا الجميع الكل عادي ."""

HELP_5 = """🔰**<u>ADD & REMOVE SUDO USERS :</u>**
/addsudo [Username or Reply to a user]
/delsudo [Username or Reply to a user]

🛃**<u>HEROKU:</u>**
/usage - Dyno Usage.

🌐**<u>CONFIG VARS:</u>**
/get_var - Get a config var from Heroku or .env.
/del_var - Delete any var on Heroku or .env.
/set_var [Var Name] [Value] - Set a Var or Update a Var on heroku or .env. Seperate Var and its Value with a space.

🤖**<u>BOT COMMANDS:</u>**
/reboot - Reboot your Bot. 
/update - Update Bot.
/speedtest - Check server speeds
/maintenance [enable / disable] 
/logger [enable / disable] - Bot logs the searched queries in logger group.
/get_log [Number of Lines] - Get log of your bot from heroku or vps. Works for both.
/autoend [enable|disable] - Enable Auto stream end after 3 mins if no one is listening.

📈**<u>STATS COMMANDS:</u>**
/activevoice - Check active voice chats on bot.
/activevideo - Check active video calls on bot.
/stats - Check Bots Stats

⚠️**<u>BLACKLIST CHAT FUNCTION:</u>**
/blacklistchat [CHAT_ID] - Blacklist any chat from using Music Bot
/whitelistchat [CHAT_ID] - Whitelist any blacklisted chat from using Music Bot
/blacklistedchat - Check all blacklisted chats.

👤**<u>BLOCKED FUNCTION:</u>**
/block [Username or Reply to a user] - Prevents a user from using bot commands.
/unblock [Username or Reply to a user] - Remove a user from Bot's Blocked List.
/blockedusers - Check blocked Users Lists

👤**<u>GBAN FUNCTION:</u>**
/gban [Username or Reply to a user] - Gban a user from bot's served chat and stop him from using your bot.
/ungban [Username or Reply to a user] - Remove a user from Bot's gbanned List and allow him for using your bot
/gbannedusers - Check Gbanned Users Lists

🎥**<u>VIDEOCALLS FUNCTION:</u>**
/set_video_limit [Number of Chats] - Set a maximum Number of Chats allowed for Video Calls at a time. Default to 3 chats.
/videomode [download|m3u8] - If download mode is enabled, Bot will download videos instead of playing them in M3u8 form. ByDefault to M3u8. You can use download mode when any query doesnt plays in m3u8 mode.

⚡️**<u>PRIVATE BOT FUNCTION:</u>**
/authorize [CHAT_ID] - Allow a chat for using your bot.
/unauthorize [CHAT_ID] - Disallow a chat from using your bot.
/authorized - Check all allowed chats of your bot.

🌐**<u>BROADCAST FUNCTION:</u>**
/broadcast [Message or Reply to a Message] - Broadcast any message to Bot's Served Chats.

<u>options for broadcast:</u>
**-pin** : This will pin your message 
**-pinloud** : This will pin your message with loud notification
**-user** : This will broadcast your message to the users who have started your bot.
**-assistant** : This will broadcast your message from assistant account of your bot.
**-nobot** : This will force your bot to not broadcast message

**Example:** `/broadcast -user -assistant -pin Hello Testing`

"""
