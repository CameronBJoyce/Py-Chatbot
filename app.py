from flask import Flask, render_template, request
import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

bot = ChatBot("Michelin_Man", storage_adapter="chatterbot.storage.SQLStorageAdapter",
              logic_adapters=[
                  {
                      'import_path': 'chatterbot.logic.BestMatch',
                      'default_response': 'I am sorry, but I do not understand.',
                      'maximum_similarity_threshold': 0.90
                  }
              ])
directory = '/Users/cameronjoyce/Desktop/Code/ChatbotSetup/TrainingText'

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        print('\n Chatbot training with ' + os.path.join(directory, filename) + ' file')
        training_data = open(os.path.join(directory, filename)).read().splitlines()
        trainer = ListTrainer(bot)
        trainer.train(training_data)
    else:
        continue


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run()
