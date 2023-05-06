import sys, os
from better_profanity import profanity
import customtkinter
import time
import openai
import pytchat
import azure.cognitiveservices.speech as speechsdk
import text2emotion as te
import asyncio 
import pyvts
import random

sys.path.append(os.path.abspath('../'))
import AUTH_KEY

PLUGIN_INFO = {
    "plugin_name": "GPT Vtube",
    "developer": "LuPow",
    "authentication_token_path": "./token.txt"
}
openai.api_key = AUTH_KEY.OPENAI_KEY
AzureApiKey = AUTH_KEY.AZURE_KEY

class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.ChatgptModel = 'gpt-3.5-turbo'
        self.pitch = "+20Hz"
        self.tts_model = "en-US-JaneNeural"

        self.youtube_streamid = ""

        self.vts = pyvts.vts(plugin_info=PLUGIN_INFO)

        self.init_style()
        self.init_widget()

    def init_style(self):
        """ initialize window style """
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        width= self.winfo_screenwidth()               
        height= self.winfo_screenheight()   
        self.geometry("%dx%d" % (width, height))
        self.frame = customtkinter.CTkFrame(master=self)
        self.frame.pack(pady=20,padx=60, fill="both",expand=True)
    
    def init_widget(self):
        # title
        self.title("GPT Vtube Luncher")
        # Label: YouTube stream ID
        self.label_youtube_streamid = customtkinter.CTkLabel(self.frame,text="Youtube Stream ID",font=("Roboto",16))
        self.label_youtube_streamid.pack(pady=2)
        # InputBox: YouTube stream ID 
        self.entry_youtube_streamid = customtkinter.CTkEntry(self.frame)
        self.entry_youtube_streamid.configure(width=500,height=30)  # shape 
        self.entry_youtube_streamid.configure(textvariable=self.youtube_streamid) # associatede variable
        self.entry_youtube_streamid.pack(padx=10)
        # Button: run
        self.button_run = customtkinter.CTkButton(self.frame, text="Run",font=("Roboto",16))
        self.button_run.configure(command=self.callback_button_run)
        self.button_run.pack(pady=5)
        # Button: clear conversation
        self.button_clear_conversation = customtkinter.CTkButton(self.frame, text="Clear Conversation",font=("Roboto",16))
        self.button_clear_conversation.pack(pady=2)
        self.button_clear_conversation.configure(command=self.callback_button_clear_conversation)
        # Switch: read chat
        self.switch_read_chat = customtkinter.CTkSwitch(self.frame, text="Reading Chat")
        self.switch_read_chat.configure(command=self.callback_switch_read_chat)
        self.switch_read_chat.select()
        self.switch_read_chat.pack()
        # Switch: filter bad words
        self.switch_filter_bad_words = customtkinter.CTkSwitch(self.frame, text="Filter Bad Words")
        self.switch_filter_bad_words.configure(command=self.callback_switch_filter_bad_words)
        self.switch_filter_bad_words.select()
        self.switch_filter_bad_words.pack()
        # inner frame
        self.inner_frame = customtkinter.CTkFrame(self.frame)

    def callback_button_run(self):
        pass

    def callback_button_clear_conversation(self):
        pass

    def callback_switch_read_chat(self):
        pass

    def callback_switch_filter_bad_words(self):
        pass