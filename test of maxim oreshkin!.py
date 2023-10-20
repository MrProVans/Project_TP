import random
locations=["школа","работа","others"]
#дописать множество локаций!!!
school_otmazki=["переводил бабушку через дорогу","захотел туалет перед школой"]
work_otmazki=["забыл выключил ли я утюг","отвозил сына в садик"]
#запилить другие отмазки
location=input(f"Введите номер места куда вы опоздали:{locations}\n")
if location=="школа" or location=="Школа":
    print("Я опоздал в школу ,потому что "+random.choice(school_otmazki))
elif location=="Работа" or location=="работа":
    print("Я опоздал на работу ,потому что "+random.choice(work_otmazki))
