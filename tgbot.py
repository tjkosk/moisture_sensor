import telepot
import time
import arduino

def handle(msg):
  chat_id=msg['chat']['id']
  command=msg['text']
  user=msg['from']['username']

  print(str(user),':')
  print(str(command))

  if str(user) not in users:
    bot.sendMessage(chat_id, 'Access denied')
  else:
    if command == '/status':
     query = arduino.queryArduino(serID)
     answer = 'Ruukun kosteus: ' + str(query)+'%' 
     bot.sendMessage(chat_id,answer)
     # bot.sendMessage(chat_id,'Olethan muistannut kastella tomaatit?')

bot=telepot.Bot('token')
users = ['retsihaha','tomikoskinen']

serID = arduino.openSerial()
if serID != 0:
  print("Serial communication started.")
else:
  print("Serial communication failed.")
bot.message_loop(handle)
print('Listening...')

while 1:
  time.sleep(10)
