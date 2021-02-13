import os
import json
from random import choice
from bottle import route, run

base = {
"dict1" : [
"Коллеги, ",
"В тоже время, ",
"Однако, ",
"Тем не менее, ",
"Следовательно, ",
"Соответственно, ",
"Вместе с тем, ",
"С другой стороны, ",
],
"dict2" : [
"парадигма цифровой экономики ",
"контекст цифровой трансформации ",
"диджитализация бизнес-процессов ",
"прагматичный подход к цифровым платформам ",
"совокупность сквозных технологий ",
"программа прорывных исследований ",
"ускорение блокчейн-транзакций ",
"экспоненциальный рост Big Data ",
],
"dict3" : [
"открывает новые возможности для ",
"выдвигает новые требования ",
"несет в себе риски ",
"расширяет горизонты ",
"заставляет искать варианты ",
"не оставляет шанса для ",
"повышает вероятность ",
"обостряет проблему ",
],
"dict4" : [
"дальнейшего углубления ",
"бюджетного финансирования ",
"синергического эффекта ",
"компрометации конфиденциальных ",
"универсальной коммодитизации ",
"неснкционированной кастомизации ",
"нормативного урегулирования ",
"практического применения ",
],
"dict5" : [
"знаний и компетенций",
"непроверенных гипотез",
"волатильных активов",
"опасных экспериментов",
"государственно-частных партнерств",
"цифровых следов граждан",
"нежелательных последствий",
"внезапных открытий",
]}

@route("/")
def default_page():
    return "<H1>Генератор фраз</H1>\n<a href=" + "./api/generate/" + ">получить одну фразу</a>"

@route("/api/generate/")
def one_phrase():
    temp = {}
    temp["message"] = phrase_gen()
    return json.dumps(temp, ensure_ascii=False)

@route("/api/generate/<num:int>")
def more_phrase(num):
    temp_list = []
    for i in range(num):
        temp = phrase_gen()
        temp_list.append(temp)
    temp_dict = dict(messages = temp_list)
    return json.dumps(temp_dict, ensure_ascii=False)

def phrase_gen():
    temp_list = []
    for value in base.values():
        temp_list.append(choice(value))
    temp = ''.join(temp_list)
    print(temp)
    return temp
# def generate_message():
#     return "Сегодня уже не вчера, ещё не завтра"

# @route("/")
# def index():
#     html = """
# <!doctype html>
# <html lang="en">
#   <head>
#     <title>Генератор утверждений</title>
#   </head>
#   <body>
#     <div class="container">
#       <h1>Коллеги, добрый день!</h1>
#       <p>{}</p>
#       <p class="small">Чтобы обновить это заявление, обновите страницу</p>
#     </div>
#   </body>
# </html>
# """.format(
#         generate_message()
#     )
#     return html


# @route("/api/roll/<some_id:int>")
# def example_api_response(some_id):
#     return {"requested_id": some_id, "random_number": random.randrange(some_id)}


if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
