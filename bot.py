import discord
from discord.ext import commands

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(name)

# Функция для старта
def start(update: Update, context: CallbackContext) -> None:
    welcome_text = (
        "Здравствуйте! Я ваш виртуальный помощник по репетиторству английского языка. Рад приветствовать вас на этом увлекательном пути изучения языка, который откроет перед вами новые горизонты и возможности. Независимо от вашего уровня — будь то новичок или продвинутый — я здесь, чтобы поддержать вас и помочь достичь ваших целей.\n\n"
        "Моя задача — сделать процесс обучения интересным и эффективным. Мы можем работать над грамматикой, словарным запасом и навыками общения. Я предложу вам разнообразные упражнения и материалы, которые помогут закрепить полученные знания.\n\n"
        "Давайте вместе сделаем изучение английского языка увлекательным и продуктивным!"
    )
    
    keyboard = [[InlineKeyboardButton("Начнём обучение", callback_data='start_learning')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(welcome_text, reply_markup=reply_markup)

# Функция для обработки нажатия кнопки
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Отлично! Давайте начнем обучение. Какую тему вы хотите изучить?")

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(name)

# Приветственное сообщение
def start(update: Update, context: CallbackContext) -> None:
    welcome_text = (
        "Здравствуйте! Я ваш виртуальный помощник по репетиторству английского языка. "
        "Рад приветствовать вас на этом увлекательном пути изучения языка.\n\n"
        "Пожалуйста, выберите ваш уровень:"
    )
    
    keyboard = [
        [InlineKeyboardButton("A1", callback_data='level_A1')],
        [InlineKeyboardButton("A2", callback_data='level_A2')],
        [InlineKeyboardButton("B1", callback_data='level_B1')],
        [InlineKeyboardButton("B2", callback_data='level_B2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(welcome_text, reply_markup=reply_markup)

# Функция для обработки выбора уровня
def level_selection(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    level = query.data.split('_')[1]  # Получаем уровень из callback_data
    if level == 'A1':
        exercises_A1(query)
    elif level == 'A2':
        query.edit_message_text(text="Упражнения для уровня A2 добавлены.")
    elif level == 'B1':
        query.edit_message_text(text="Упражнения для уровня B1 добавлены.")
    elif level == 'B2':
        query.edit_message_text(text="Упражнения для уровня B2 добавлены.")

# Функция для отображения упражнений уровня A1
def exercises_A1(query):
    exercises_text = (
        "Упражнения А1:\n\n"
        "Алфавит и произношение:\n"
        "A - эй, B - би, C - си, D - ди, E - и, F - эф, G - джи, H - эйч,\n"
        "I - ай, J - джей, K - кей, L - эл, M - эм, N - эн,\n"
        "O - оу, P - пи, Q - кью, R - ар, S - эс,\n"
        "T - ти, U - ю, V - ви, W - дабл-ю, X - экс, Y - уай, Z - зи или зед.\n\n"
        
        "Существительные:\n"
        "1. apple - яблоко\n"
        "2. book - книга\n"
        "3. car - машина\n"
        "4. dog - собака\n"
        "5. cat - кот\n"
        "6. house - дом\n"
        "7. school - школа\n"
        "8. table - стол\n"
        "9. chair - стул\n"
        "10. friend - друг\n"
        "11. family - семья\n"
        "12. water - вода\n"
        "13. food - еда\n"
        "14. city - город\n"
        "15. street - улица\n\n"

        "Местоимения:\n"
        "1. I - я\n"
        "2. you - ты/вы\n"
        "3. he - он\n"
        "4. she - она\n"
        "5. it - оно (для животных и предметов)\n"
        "6. we - мы\n"
        "7. they - они\n\n"

        "Глаголы:\n"
        "1. be - быть\n"
        "2. have - иметь\n"
        "3. do - делать\n"
        "4. go - идти/ехать\n"
        "5. come - приходить\n"
        "6. see - видеть\n"
        "7. hear - слышать\n"
        "8. speak - говорить\n"
        "9. say - сказать\n"
        "10. like - нравиться\n"
        "11. want - хотеть\n"
        "12. need - нуждаться\n"
        "13. make - делать/создавать\n"
        "14. take - брать\n"
        "15. give - давать\n\n"

        "Прилагательные:\n"
        "1. big - большой\n"
        "2. small - маленький\n"
        "3. good - хороший\n"
        "4. bad - плохой\n"
        "5. happy - счастливый\n"
        "6. sad - грустный\n"
        "7. hot - горячий\n"
        "8. cold - холодный\n"
        "9. new - новый\n"
        "10. old - старый\n\n"

        "Числа и времени:\n"
        "1. 0 - zero\n"
        "2. 1 - one\n"
        "3. 2 - two\n"
        "4. 3 - three\n"
        "5. 4 - four\n"
        "6. 5 - five\n"
        "7. 6 - six\n"
        "8. 7 - seven\n"
        "9. 8 - eight\n"
        "10. 9 - nine\n"
        "11. 10 - ten"
    )
    
    query.edit_message_text(text=exercises_text)

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(name)

# Приветственное сообщение
def start(update: Update, context: CallbackContext) -> None:
    welcome_text = (
        "Здравствуйте! Я ваш виртуальный помощник по репетиторству английского языка. "
        "Рад приветствовать вас на этом увлекательном пути изучения языка.\n\n"
        "Пожалуйста, выберите ваш уровень:"
    )
    
    keyboard = [
        [InlineKeyboardButton("A1", callback_data='level_A1')],
        [InlineKeyboardButton("A2", callback_data='level_A2')],
        [InlineKeyboardButton("B1", callback_data='level_B1')],
        [InlineKeyboardButton("B2", callback_data='level_B2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(welcome_text, reply_markup=reply_markup)

# Функция для обработки выбора уровня
def level_selection(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    level = query.data.split('_')[1]  # Получаем уровень из callback_data
    if level == 'A1':
        exercises_A1(query)
    elif level == 'A2':
        exercises_A2(query)
    elif level == 'B1':
        query.edit_message_text(text="Упражнения для уровня B1 еще не добавлены.")
    elif level == 'B2':
        query.edit_message_text(text="Упражнения для уровня B2 еще не добавлены.")

# Функция для отображения упражнений уровня A1
def exercises_A1(query):
    exercises_text = (
        "Упражнения А1:\n\n"
        "Алфавит и произношение:\n"
        "A - эй, B - би, C - си, D - ди, E - и, F - эф, G - джи, H - эйч,\n"
        "I - ай, J - джей, K - кей, L - эл, M - эм, N - эн,\n"
        "O - оу, P - пи, Q - кью, R - ар, S - эс,\n"
        "T - ти, U - ю, V - ви, W - дабл-ю, X - экс, Y - уай, Z - зи или зед.\n\n"
        
        "Существительные:\n"
        "1. apple - яблоко\n"
        "2. book - книга\n"
        "3. car - машина\n"
        "4. dog - собака\n"
        "5. cat - кот\n"
        "6. house - дом\n"
        "7. school - школа\n"
        "8. table - стол\n"
        "9. chair - стул\n"
        "10. friend - друг\n"
        "11. family - семья\n"
        "12. water - вода\n"
        "13. food - еда\n"
        "14. city - город\n"
        "15. street - улица\n\n"

        "Местоимения:\n"
        "1. I - я\n"
        "2. you - ты/вы\n"
        "3. he - он\n"
        "4. she - она\n"
        "5. it - оно (для животных и предметов)\n"
        "6. we - мы\n"
        "7. they - они\n\n"

        "Глаголы:\n"
        "1. be - быть\n"
        "2. have - иметь\n"
        "3. do - делать\n"
        "4. go - идти/ехать\n"
        "5. come - приходить\n"
        "6. see - видеть\n"
        "7. hear - слышать\n"
        "8. speak - говорить\n"
        "9. say - сказать\n"
        "10. like - нравиться\n"
        "11. want - хотеть\n"
        "12. need - нуждаться\n"
        "13. make - делать/создавать\n"
        "14. take - брать\n"
        "15. give - давать\n\n"

        "Прилагательные:\n"
        "1. big - большой\n"
        "2. small - маленький\n"
        "3. good - хороший\n"
        "4. bad - плохой\n"
        "5. happy - счастливый\n"
        "6. sad - грустный\n"
        "7. hot - горячий\n"
        "8. cold - холодный\n"
        "9. new - новый\n"
        "10. old - старый\n\n"

        "Числа и времени:\n"
        "1. 0 - zero\n"
        "2. 1 - one\n"
        "3. 2 - two\n"
        "4. 3 - three\n"
        "5. 4 - four\n"
        "6. 5 - five\n"
        "7. 6 - six\n"
        "8. 7 - seven\n"
        "9. 8 - eight\n"
        "10. 9 - nine\n"
        "11. 10 - ten."
    )
    
    query.edit_message_text(text=exercises_text)

# Функция для отображения упражнений уровня A2
def exercises_A2(query):
    exercises_text = (
        "Упражнения A2:\n\n"
        
        # Описание людей
        "Описание людей:\nОписание людей на английском языке может включать в себя различные аспекты, такие как внешность, характер, увлечения и другие характеристики.\n"

        "Внешность (Appearance)\n"

        "*Волосы (Hair)*\n" 
         "- Color: blonde, brown, black, red, gray.\n" 
         "- Length: short, medium, long.\n" 
         "- Style: straight, curly, wavy.\n" 
         "*Пример*: She has long, straight brown hair.\n"

         "*Глаза (Eyes)*\n" 
         "- Color: blue, green, brown, hazel.\n" 
         "- Shape: round, almond-shaped.\n" 
         "*Пример*: He has bright blue eyes.\n"

         "*Рост (Height)*\n" 
         "- Tall, short, average height.\n" 
         "*Пример*: She is tall and slender.\n"

         "*Телосложение (Build)*\n" 
         "- Slim, athletic, overweight, muscular.\n" 
         "*Пример*: He has an athletic build.\n"

         "*Особенности (Features)*\n" 
         "- Freckles, dimples, scars.\n" 
         "*Пример*: She has freckles on her cheeks.\n"

         "Характер (Personality)\n" 
         "- Friendly (дружелюбный).\n" 
         "- Funny (смешной).\n" 
         "- Shy (скромный).\n" 
         "- Outgoing (общительный).\n" 
         "- Kind (добрый).\n" 
         "- Hardworking (трудолюбивый).\n" 
         "*Пример*: He is very friendly and always makes people laugh.\n"

         "Увлечения и интересы (Hobbies and Interests)\n" 
         "- Sports: football, basketball, swimming.\n" 
         "- Arts: painting, music, dancing.\n" 
         "- Reading, traveling, cooking.\n" 
         "*Пример*: She loves painting and often spends her weekends at art galleries.\n"

         "Примеры описаний\n" 
         "*Пример 1*: My friend Sarah is a tall girl with long curly black hair and green eyes... \n"  
         "*Пример 2*: John is a short man with a muscular build and short brown hair...\n"

         "Описание вещей:\nОписание вещей на английском языке также может включать в себя различные аспекты:\n"

         "Внешний вид (Appearance)\n"

         "*Цвет (Color)*\n" 
         "- Red, blue, green...\n" 
         "*Пример*: The car is bright red.\n"

         "*Размер (Size)*\n" 
         "- Small, medium...\n" 
         "*Пример*: The box is small enough to fit in my backpack.\n"

         "*Форма (Shape)*\n" 
         "- Round, square...\n" 
         "*Пример*: The table is rectangular.\n"

         "*Материал (Material)*\n" 
         "- Wood, metal...\n" 
         "*Пример*: The chair is made of wood.\n"

         "Функциональность (Functionality)\n" 
         "- What the item is used for.\n" 
         "*Пример*: This blender is used for making smoothies and soups.\n"

         "Примеры описаний\n" 
         "*Пример 1*: This is a beautiful vase made of glass...\n"  
         "*Пример 2*: The backpack is made of durable fabric...\n"
    )
    
    query.edit_message_text(text=exercises_text)

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(name)

# Приветственное сообщение
def start(update: Update, context: CallbackContext) -> None:
    welcome_text = (
        "Здравствуйте! Я ваш виртуальный помощник по репетиторству английского языка. "
        "Рад приветствовать вас на этом увлекательном пути изучения языка.\n\n"
        "Пожалуйста, выберите ваш уровень:"
    )
    
    keyboard = [
        [InlineKeyboardButton("A1", callback_data='level_A1')],
        [InlineKeyboardButton("A2", callback_data='level_A2')],
        [InlineKeyboardButton("B1", callback_data='level_B1')],
        [InlineKeyboardButton("B2", callback_data='level_B2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(welcome_text, reply_markup=reply_markup)

# Функция для обработки выбора уровня
def level_selection(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    level = query.data.split('_')[1]  # Получаем уровень из callback_data
    if level == 'A1':
        exercises_A1(query)
    elif level == 'A2':
        exercises_A2(query)
    elif level == 'B1':
        exercises_B1(query)
    elif level == 'B2':
        query.edit_message_text(text="Упражнения для уровня B2 еще не добавлены.")

# Функция для отображения упражнений уровня A1
def exercises_A1(query):
    exercises_text = (
        "Упражнения А1:\n\n"
        "Алфавит и произношение:\n"
        "A - эй, B - би, C - си, D - ди, E - и, F - эф, G - джи, H - эйч,\n"
        "I - ай, J - джей, K - кей, L - эл, M - эм, N - эн,\n"
        "O - оу, P - пи, Q - кью, R - ар, S - эс,\n"
        "T - ти, U - ю, V - ви, W - дабл-ю, X - экс, Y - уай, Z - зи или зед.\n\n"
        
        "Существительные:\n"
        "1. apple - яблоко\n"
        "2. book - книга\n"
        "3. car - машина\n"
        "4. dog - собака\n"
        "5. cat - кот\n"
        "6. house - дом\n"
        "7. school - школа\n"
        "8. table - стол\n"
        "9. chair - стул\n"
        "10. friend - друг\n"
        "11. family - семья\n"
        "12. water - вода\n"
        "13. food - еда\n"
        "14. city - город\n"
        "15. street - улица\n\n"

        "Местоимения:\n"
        "1. I - я\n"
        "2. you - ты/вы\n"
        "3. he - он\n"
        "4. she - она\n"
        "5. it - оно (для животных и предметов)\n"
        "6. we - мы\n"
        "7. they - они\n\n"

        "Глаголы:\n"
        "1. be - быть\n"
        "2. have - иметь\n"
        "3. do - делать\n"
        "4. go - идти/ехать\n"
        "5. come - приходить\n"
        "6. see - видеть\n"
        "7. hear - слышать\n"
        "8. speak - говорить\n"
        "9. say - сказать\n"
        "10. like - нравиться\n"
        "11. want - хотеть\n"
        "12. need - нуждаться\n"
        "13. make - делать/создавать\n"
        "14. take - брать\n"
        "15. give - давать\n\n"

        "Прилагательные:\n"
        "1. big - большой\n"
        "2. small - маленький\n"
        "3. good - хороший\n"
        "4. bad - плохой\n"
        "5. happy - счастливый\n"
        "6. sad - грустный\n"
        "7. hot - горячий\n"
        "8. cold - холодный\n"
        "9. new - новый\n"
        "10. old - старый.\n\n"

        "Числа и времени:\n"
        "1. 0 - zero\n"
        "2. 1 - one\n"
        "3. 2 - two\n"
        "4. 3 - three\n"
        "5. 4 - four\n"
        "6. 5 - five\n"
        "7. 6 - six\n"
        "8. 7 - seven\n"
        "9. 8 - eight\n"
        "10. 9 - nine\n"
        "11. 10 - ten."
    )
    
    query.edit_message_text(text=exercises_text)

# Функция для отображения упражнений уровня A2
def exercises_A2(query):
    exercises_text = (
        "Упражнения A2:\n\n"

# Описание людей
         "Описание людей:\nОписание людей на английском языке может включать в себя различные аспекты...\n"

         "Внешность (Appearance)\n" 
         "*Волосы (Hair)*\n" 
         "- Color: blonde, brown, black...\n" 
         "*Пример*: She has long, straight brown hair.\n"

         "Характер (Personality)\n" 
         "- Friendly (дружелюбный).\n" 
         "*Пример*: He is very friendly and always makes people laugh.\n"

         "Примеры описаний\n" 
         "*Пример 1*: My friend Sarah is a tall girl...\n"  

         "Описание вещей:\nОписание вещей на английском языке также может включать в себя различные аспекты...\n"

         "Внешний вид (Appearance)\n" 
         "*Цвет (Color)*\n" 
         "- Red, blue...\n" 
         "*Пример*: The car is bright red.\n"

         "Примеры описаний\n" 
         "*Пример 1*: This is a beautiful vase made of glass...\n"  
    )
    
    query.edit_message_text(text=exercises_text)

# Функция для отображения упражнений уровня B1
def exercises_B1(query):
    exercises_text = (
        "Упражнения B1:\n\n"

        "Путешествия и туризм:\n▎Основные термины\n"
        
        "1. Travel — путешествовать\n"
        "2. Tourism — туризм\n"
        "3. Destination — место назначения\n"
        "4. Itinerary — маршрут\n"
        "5. Accommodation — жилье (где остановиться)\n"
        "6. Reservation — бронирование\n"
        "7. Sightseeing — осмотр достопримечательностей\n"
        "8. Adventure — приключение\n"
        "9. Passport — паспорт\n"
        "10. Visa — виза\n"

        "\n▎Связанные концепции\n"

        "1. Backpacking — туристические походы с рюкзаком\n"
        "2. Cultural exchange — культурный обмен\n"
        "3. Travel guide — путеводитель\n"
        "4. Tour package — туристический пакет\n"
        "5. Transportation — транспорт\n"
        "6. Travel insurance — туристическая страховка\n"
        "7. Souvenir — сувенир\n"
        "8. Local cuisine — местная кухня\n"
        "9. Eco-tourism — экологический туризм\n"
        "10. Travel blog — туристический блог\n"

        "\n▎Примеры предложений:\n"

        "1. I love to travel and explore new cultures.\n   (Я люблю путешествовать и изучать новые культуры.)\n"  
        
        "2. Make sure to check your passport and visa requirements before traveling.\n   (Обязательно проверьте требования к паспорту и визе перед поездкой.)\n"

        "3. We booked a tour package that includes accommodation and meals.\n   (Мы забронировали туристический пакет, который включает жилье и питание.)\n"

        "4. Sightseeing is one of the best ways to learn about a new city.\n   (Осмотр достопримечательностей — один из лучших способов узнать новый город.)\n"

        "5. Don't forget to buy souvenirs to remember your trip!\n   (Не забудьте купить сувениры, чтобы помнить о своей поездке!)\n"

        
       "Здоровье и фитнес:\nВот некоторые слова и фразы на английском языке, связанные с темой здоровья и фитнеса:\n▎Основные термины:\n"

       "1. Health — здоровье.\n"  
       "2. Fitness — фитнес, физическая форма.\n"  
       "3. Exercise — упражнение.\n"  
       "4. Nutrition — питание.\n"  
       "5. Diet — диета.\n"  
       "6. Wellness — благополучие.\n"  
       "7. Cardio — кардионагрузка (сердечно-сосудистые упражнения).\n"  
       "8. Strength training — силовые тренировки.\n"  
       "9. Flexibility — гибкость.\n"  
       "10. Hydration — гидратация.\n"  

       "\n▎Связанные концепции:\n"

       "1. Personal trainer — персональный тренер.\n"  
       "2. Workout routine — программа тренировок.\n"
       "3. Healthy lifestyle — здоровый образ жизни.\n"  
       "4. Calorie — калория.\n"  
       "5. BMI (Body Mass Index) — индекс массы тела.\n"  
       "6. Supplement — добавка (например, витаминов).\n"  
       "7. Mental health — психическое здоровье.\n"  
       "8. Yoga — йога.\n"  
       "9. Meditation — медитация.\n"  
       "10. Recovery — восстановление.\n"  

       "\n▎Примеры предложений:\n"

"1. Regular exercise is essential for maintaining good health.\n   (Регулярные физические упражнения необходимы для поддержания хорошего здоровья.)\n"

       "2. A balanced diet is important for overall wellness.\n   (Сбалансированное питание важно для общего благополучия.)\n"

       "3. I work out three times a week to stay fit.\n   (Я занимаюсь спортом три раза в неделю, чтобы поддерживать форму.)\n"

       "4. Drinking enough water is crucial for hydration during workouts.\n   (Достаточное количество воды имеет решающее значение для гидратации во время тренировок.)\n"

       "5. Yoga helps improve flexibility and reduce stress.\n   (Йога помогает улучшить гибкость и снизить уровень стресса.)\n"

       
      "Технологии и медиа:\n▎Основные термины:\n"

      "1. Technology — технология.\n"  
      "2. Media — медиа, средства массовой информации.\n"  
      "3. Digital — цифровой.\n"  
      "4. Internet — интернет.\n"  
      "5. Social media — социальные сети.\n"  
      "6. Broadcasting — вещание.\n"  
      "7. Streaming — потоковая передача.\n"  
      "8. Podcast — подкаст.\n"  
      "9. Website — веб-сайт.\n"  
      "10. App (Application) — приложение.\n"  

      "\n▎Связанные концепции:\n"

      "1. Content creation — создание контента.\n"  
      "2. User interface (UI) — пользовательский интерфейс.\n"  
      "3. User experience (UX) — пользовательский опыт.\n"  
      "4. Virtual reality (VR) — виртуальная реальность.\n"  
      "5. Augmented reality (AR) — дополненная реальность.\n"  
      "6. Artificial intelligence (AI) — искусственный интеллект.\n"  
      "7. Cybersecurity — кибербезопасность.\n"  
      "8. Cloud computing — облачные вычисления.\n"  
      "9. Big data — большие данные.\n"  
      "10. E-commerce — электронная коммерция.\n"

      "\n▎Примеры предложений:\n"

      '1.Technology has transformed the way we communicate and consume media.\n   (Технология изменила способ, которым мы общаемся и потребляем медиа.)\n'
    )

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(name)

# Приветственное сообщение
def start(update: Update, context: CallbackContext) -> None:
    welcome_text = (
        "Здравствуйте! Я ваш виртуальный помощник по репетиторству английского языка. "
        "Рад приветствовать вас на этом увлекательном пути изучения языка.\n\n"
        "Пожалуйста, выберите ваш уровень:"
    )
    
    keyboard = [
        [InlineKeyboardButton("A1", callback_data='level_A1')],
        [InlineKeyboardButton("A2", callback_data='level_A2')],
        [InlineKeyboardButton("B1", callback_data='level_B1')],
        [InlineKeyboardButton("B2", callback_data='level_B2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(welcome_text, reply_markup=reply_markup)

# Функция для обработки выбора уровня
def level_selection(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    level = query.data.split('_')[1]  # Получаем уровень из callback_data
    if level == 'A1':
        exercises_A1(query)
    elif level == 'A2':
        exercises_A2(query)
    elif level == 'B1':
        exercises_B1(query)
    elif level == 'B2':
        query.edit_message_text(text="Упражнения для уровня B2 еще не добавлены.")

# Функция для отображения упражнений уровня A1
def exercises_A1(query):
    exercises_text = (
        "Упражнения А1:\n\n"
        "Алфавит и произношение:\n"
        "A - эй, B - би, C - си, D - ди, E - и, F - эф, G - джи, H - эйч,\n"
        "I - ай, J - джей, K - кей, L - эл, M - эм, N - эн,\n"
        "O - оу, P - пи, Q - кью, R - ар, S - эс,\n"
        "T - ти, U - ю, V - ви, W - дабл-ю, X - экс, Y - уай, Z - зи или зед.\n\n"
        
        "Существительные:\n"
        "1. apple - яблоко\n"
        "2. book - книга\n"
        "3. car - машина\n"
        "4. dog - собака\n"
        "5. cat - кот\n"
        "6. house - дом\n"
        "7. school - школа\n"
        "8. table - стол\n"
        "9. chair - стул\n"
        "10. friend - друг\n"
        "11. family - семья\n"
        "12. water - вода\n"
        "13. food - еда\n"
        "14. city - город\n"
        "15. street - улица\n\n"

        "Местоимения:\n"
        "1. I - я\n"
        "2. you - ты/вы\n"
        "3. he - он\n"
        "4. she - она\n"
        "5. it - оно (для животных и предметов)\n"
        "6. we - мы\n"
        "7. they - они\n\n"

        "Глаголы:\n"
        "1. be - быть\n"
        "2. have - иметь\n"
        "3. do - делать\n"
        "4. go - идти/ехать\n"
        "5. come - приходить\n"
        "6. see - видеть\n"
        "7. hear - слышать\n"
        "8. speak - говорить\n"
        "9. say - сказать\n"
        "10. like - нравиться\n"
        "11. want - хотеть\n"
        "12. need - нуждаться\n"
        "13. make - делать/создавать\n"
        "14. take - брать\n"
        "15. give - давать\n\n"

        "Прилагательные:\n"
        "1. big - большой\n"
        "2. small - маленький\n"
        "3. good - хороший\n"
        "4. bad - плохой\n"
        "5. happy - счастливый\n"
        "6. sad - грустный\n"
        "7. hot - горячий\n"
        "8. cold - холодный\n"
        "9. new - новый\n"
        "10. old - старый.\n\n"

        "Числа и времени:\n"
        "1. 0 - zero\n"
        "2. 1 - one\n"
        "3. 2 - two\n"
        "4. 3 - three\n"
        "5. 4 - four\n"
        "6. 5 - five\n"
        "7. 6 - six\n"
        "8. 7 - seven\n"        "9. 8 - eight\n"
        "10. 9 - nine\n"
        "11. 10 - ten."
    )
    
    query.edit_message_text(text=exercises_text)

# Функция для отображения упражнений уровня A2
def exercises_A2(query):
    exercises_text = (
        "Упражнения A2:\n\n"

# Описание людей
         "Описание людей:\nОписание людей на английском языке может включать в себя различные аспекты...\n"

         "Внешность (Appearance)\n" 
         "*Волосы (Hair)*\n" 
         "- Color: blonde, brown, black...\n" 
         "*Пример*: She has long, straight brown hair.\n"

         "Характер (Personality)\n" 
         "- Friendly (дружелюбный).\n" 
         "*Пример*: He is very friendly and always makes people laugh.\n"

         "Примеры описаний\n" 
         "*Пример 1*: My friend Sarah is a tall girl...\n"  

         "Описание вещей:\nОписание вещей на английском языке также может включать в себя различные аспекты...\n"

         "Внешний вид (Appearance)\n" 
         "*Цвет (Color)*\n" 
         "- Red, blue...\n" 
         "*Пример*: The car is bright red.\n"

         "Примеры описаний\n" 
         "*Пример 1*: This is a beautiful vase made of glass...\n"  
    )
    
    query.edit_message_text(text=exercises_text)

# Функция для отображения упражнений уровня B1
def exercises_B1(query):
    exercises_text = (
        "Упражнения B1:\n\n"

        "Здоровье:\n"

        "1. A balanced diet is essential for good health.\n   (Сбалансированное питание необходимо для хорошего здоровья.)\n"  
        
        "2. Mental health is just as important as physical health.\n   (Психическое здоровье так же важно, как и физическое.)\n"

        "3. Vaccination is a key preventive measure against infectious diseases.\n   (Вакцинация является ключевой профилактической мерой против инфекционных заболеваний.)\n"

        
       "Общество:\nВот некоторые слова и фразы на английском языке, связанные с темой общества:\n"

       "\n▎Основные термины:\n"

       "1. Society — общество.\n"  
       "2. Community — сообщество.\n"  
       "3. Culture — культура.\n"  
       "4. Socialization — социализация.\n"  
       "5. Diversity — разнообразие.\n"  
       "6. Tradition — традиция.\n"  
       "7. Values — ценности.\n"  
       "8. Norms — нормы.\n"  
       "9. Identity — идентичность.\n"  
       "10. Interaction — взаимодействие.\n"  

       "\n▎Социальные группы и структуры:\n"

       "1. Family — семья.\n"  
       "2. Peer group — группа сверстников.\n"  
       "3. Class — класс (социальный).\n"  
       "4. Ethnicity — этничность.\n"  
       "5. Gender — пол.\n"  
       "6. Religion — религия.\n"  
       "7. Institution — институт (например, образовательный, религиозный).\n"  
       "8. Organization — организация.\n"  
       "9. Civic engagement — гражданское участие.\n"  
       "10. Activism — активизм.\n"  

       "\n▎Связанные фразы:\n"

       "1. Social issues — социальные проблемы.\n"  
       "2. Community service — общественные работы.\n"  
       "3. Cultural exchange — культурный обмен.\n"  
       "4. Social justice — социальная справедливость.\n"  
       "5. Human rights — права человека.\n"  
       "6. Public opinion — общественное мнение.\n"  
       "7. Civic responsibility — гражданская ответственность.\n"  
       "8. Social cohesion — социальная сплоченность.\n"  
       "9. Marginalized groups — маргинализированные группы.\n"  
       "10. Globalization — глобализация.\n"

       "\n▎Примеры предложений:\n"

       '1.A diverse society enriches cultural experiences for everyone.\n   (Разнообразное общество обогащает культурный опыт для всех.)\n'

       '2.Social issues like poverty and inequality need to be addressed.\n   (Социальные проблемы, такие как бедность и неравенство, нуждаются в решении.)\n'

       '3.Community service can strengthen the bonds among residents.\n   (Общественные работы могут укрепить связи между жителями.)\n'       '4.Civic engagement is crucial for a healthy democracy.\n   (Гражданское участие имеет решающее значение для здоровой демократии.)\n'

       '5.Understanding different cultures fosters tolerance and respect.\n   (Понимание различных культур способствует терпимости и уважению.)\n'

"Культура:\nВот некоторые слова и фразы на английском языке, связанные с темой культуры:\n"

      "\n▎Основные термины:\n"

      "1.Culture — культура.\n"  
      "2.Tradition — традиция.\n"  
      "3.Heritage — наследие.\n"  
      "4.Custom — обычай.\n"  
      "5.Art — искусство.\n"  
      "6.Literature — литература.\n"  
      "7.Music — музыка.\n"  
      "8.Dance — танец.\n"  
      "9.Cuisine — кухня (кулинарные традиции).\n"  
      "10.Festival — фестиваль.\n"

      "\n▎Связанные концепции:\n"

      "1.Cultural identity — культурная идентичность.\n"  
      "2.Cultural diversity — культурное разнообразие.\n"  
      "3.Folklore — фольклор.\n"  
      "4.Mythology — мифология.\n"  
      "5.Ritual — ритуал.\n"  
      "6.Symbolism — символизм.\n"  
      "7.Aesthetics — эстетика.\n"  
      "8.Craftsmanship — мастерство (ремесло).\n"  
      "9.Performing arts — исполнительские искусства.\n"  
      "10.Visual arts — изобразительное искусство.\n"

      "\n▎Примеры предложений:\n"

      '1.Cultural diversity enriches our society and promotes understanding.\n   (Культурное разнообразие обогащает наше общество и способствует пониманию.)\n'

      '2.Festivals are a great way to celebrate cultural heritage.\n   (Фестивали — отличный способ отпраздновать культурное наследие.)\n'

      '3.Traditional music often reflects the history of a community.\n   (Традиционная музыка часто отражает историю сообщества.)\n'

      '4.Literature can provide insight into the values and beliefs of a culture.\n   (Литература может дать представление о ценностях и убеждениях культуры.)\n'

      '5.Art is a powerful medium for expressing cultural identity.\n   (Искусство — мощное средство для выражения культурной идентичности.)\n'
    )
    
    query.edit_message_text(text=exercises_text)

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(name)

# Приветственное сообщение
def start(update: Update, context: CallbackContext) -> None:
    welcome_text = (
        "Здравствуйте! Я ваш виртуальный помощник по репетиторству английского языка. "
        "Рад приветствовать вас на этом увлекательном пути изучения языка.\n\n"
        "Пожалуйста, выберите тему:"
    )
    
    keyboard = [
        [InlineKeyboardButton("Новые слова A1", callback_data='new_words_A1')],
        [InlineKeyboardButton("Приветствия и прощания", callback_data='greetings')],
        [InlineKeyboardButton("Личные местоимения", callback_data='pronouns')],
        [InlineKeyboardButton("Основные глаголы", callback_data='verbs')],
        [InlineKeyboardButton("Числа", callback_data='numbers')],
        [InlineKeyboardButton("Цвета", callback_data='colors')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(welcome_text, reply_markup=reply_markup)

# Функция для обработки выбора темы
def topic_selection(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    topic = query.data.split('_')[1]  # Получаем тему из callback_data
    if topic == 'new_words_A1':
        new_words_A1(query)
    elif topic == 'greetings':
        greetings(query)
    elif topic == 'pronouns':
        pronouns(query)
    elif topic == 'verbs':
        verbs(query)
    elif topic == 'numbers':
        numbers(query)
    elif topic == 'colors':
        colors(query)

# Функции для каждой темы
def new_words_A1(query):
    words_text = (
        "Новые слова A1:\n\n"
        "1. Apple - яблоко\n"
        "2. Book - книга\n"
        "3. Car - машина\n"
        "4. Dog - собака\n"
        "5. Cat - кот\n"
        "6. House - дом\n"
        "7. School - школа\n"
        "8. Table - стол\n"
        "9. Chair - стул\n"
        "10. Friend - друг\n"
    )
    
    query.edit_message_text(text=words_text)

def greetings(query):
    greetings_text = (
        "Приветствия и прощания:\n\n"
        "1. Hello! - Привет!\n"
        "2. Hi! - Привет!\n"
        "3. Good morning! - Доброе утро!\n"
        "4. Good afternoon! - Добрый день!\n"
        "5. Good evening! - Добрый вечер!\n"
        "6. Goodbye! - До свидания!\n"
        "7. Bye! - Пока!\n"
        "8. See you later! - Увидимся позже!\n"
        "9. See you soon! - Увидимся скоро!\n"
        "10. Take care! - Береги себя!\n"
    )
    
    query.edit_message_text(text=greetings_text)

def pronouns(query):
    pronouns_text = (
        "Личные местоимения:\n\n"
        "1. I - я\n"
        "2. You - ты / вы\n"
        "3. He - он\n"
        "4. She - она\n"
        "5. It - оно (для предметов и животных)\n"
        "6. We - мы\n"
        "7. They - они\n"
        "8. Me - меня (объектное местоимение)\n"
        "9. You - тебя / вас (объектное местоимение)\n"
        "10. Him - его (объектное местоимение, для 'he')\n"
        "11. Her - её (объектное местоимение, для 'she')\n"
        "12. Us - нас (объектное местоимение, для 'we')\n"
        "13. Them - их (объектное местоимение, для 'they')\n"
    )
    
    query.edit_message_text(text=pronouns_text)

def verbs(query):
    verbs_text = (
        "Основные глаголы:\n\n"
        "1. Be - быть\n"
        "2. Have - иметь\n"
        "3. Do - делать\n"
        "4. Go - идти, ехать\n"        "5. Come - приходить\n"
        "6. See - видеть\n"
        "7. Look - смотреть\n"
        "8. Say - говорить\n"
        "9. Get - получать\n"
        "10. Make - делать, создавать\n"
        "11. Like - нравиться\n"
        "12. Want - хотеть\n"
    )
    
    query.edit_message_text(text=verbs_text)

def numbers(query):
    numbers_text = (
        "Числа:\n\n"
        "1. One - один\n"
        "2. Two - два\n"
        "3. Three - три\n"
        "4. Four - четыре\n"
        "5. Five - пять\n"
        "6. Six - шесть\n"
        "7. Seven - семь\n"
        "8. Eight - восемь\n"
        "9. Nine - девять\n"
        "10. Ten - десять\n"

        "\nДалее числа от 11 до 20:\n"

        "11. Eleven - одиннадцать\n"  
        "12. Twelve - двенадцать\n"  
        "13. Thirteen - тринадцать\n"  
        "14. Fourteen - четырнадцать\n"  
        "15. Fifteen - пятнадцать\n"  
        "16. Sixteen - шестнадцать\n"  
        "17. Seventeen - семнадцать\n"  
        "18. Eighteen - восемнадцать\n"  
        "19. Nineteen - девятнадцать\n"  
        "20. Twenty - двадцать\n"

        "\nТакже полезно знать десятки:\n"

        "- Thirty - тридцать\n"  
        "- Forty - сорок\n"  
        "- Fifty - пятьдесят\n"  
        "- Sixty - шестьдесят\n"  
        "- Seventy - семьдесят\n"  
        "- Eighty - восемьдесят\n"  
        "- Ninety - девяносто\n"  
        "- Hundred - сто\n"  
    )
    
    query.edit_message_text(text=numbers_text)

def colors(query):
    colors_text = (
        "Цвета:\n\n"
        "1. Red - красный\n"
        "2. Blue - синий\n"
        "3. Green - зеленый\n"
        "4. Yellow - желтый\n"
        "5. Black - черный\n"
        "6. White - белый\n"
        "7. Gray (или Grey) - серый\n"
        "8. Pink - розовый\n"
        "9. Orange - оранжевый\n"
        "10. Purple - фиолетовый\n"
    )

query.edit_message_text(text=colors_text)

# Основная функция для запуска бота
def main() -> None:
    # Вставьте сюда ваш токен
    TOKEN = '7849750307:AAGpEou6WacHs_Uf9l_icZRCIeyfKvp563o'
    
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(topic_selection, pattern='.*'))

    # Запускаем бота
    updater.start_polling()

    # Останавливаем бота при завершении работы
    updater.idle()

if __name__ == '__main__':
    main()
