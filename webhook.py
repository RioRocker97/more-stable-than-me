from cgitb import handler
from fastapi import FastAPI,Response,Request
from os import environ
from linebot import LineBotApi,WebhookHandler
from linebot.models import MessageEvent,TextMessage,ImageSendMessage,TextSendMessage
from txt2img import txt2img
#from txt2img import txt2img
LINE_TOKEN = environ['LINE_TOKEN']
LINE_SECRET = environ['LINE_SECRET']
webhook = FastAPI()
line_api = LineBotApi(LINE_TOKEN)
handler = WebhookHandler(LINE_SECRET)
@webhook.post('/line/webhook')
async def respond(req:Request):
    signature = req.headers.get('X-Line-Signature')
    body = await req.body()
    handler.handle(body.decode('UTF-8'),signature)
    return Response()
@webhook.get('/line/webhook')
def keep_alive():
    return Response()

@handler.add(MessageEvent,message=TextMessage)
def get_prompt(event):
    line_api.reply_message(
        event.reply_token,
        TextSendMessage('Processing... Please wait')
    )
    res = txt2img(event.message.text)
    line_api.reply_message(
        event.reply_token,
        ImageSendMessage(res,res)
    )

