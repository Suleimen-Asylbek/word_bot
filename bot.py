from telebot import TeleBot
from lemma import init, get_placement 

init_world, world_dict = init()
similarities = []
TOKEN = '6417825825:AAE2DWq6y-mKHyFsxgI5F9qxQ-Ya-0HwV3k'
bot = TeleBot(TOKEN)

print(len(world_dict))
print(init_world)

def get_sring_words(similarities):
    end_string = ''
    for sim, count in similarities:
        end_string += f'{sim} {count}\n'
    return end_string


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, 'Вводите любые слова, чтобы играть. Используйте команду word')

@bot.message_handler(commands=['word'])
def word(message):
    global similarities
    if len(message.text.split(' ')) > 2:
        bot.send_message(
        message.chat.id, 'Больше одного слова нельзя!')
        return
    _, word = message.text.split(' ')
    if word == init_world:
        bot.send_message(message.chat.id, 'Правильно!')
        return
    place = get_placement(word, world_dict)
    if place == -1:
        bot.send_message(message.chat.id, 'Очень далеко')
        return
    similarities.append((word, place))
    similarities.sort(key=lambda tup: tup[1])
    msg = get_sring_words(similarities)
    bot.send_message(message.chat.id, msg)

if __name__ == '__main__':
    bot.polling(non_stop=True)