class RaitingList:
    
    def __init__(self):
        self.__averange = 0 #Среднее значение
        self.__items = []   #Список словарей

    def addItem(self, item): 
        #Словарь в Python выглядит как {key: value} и при добавлении другого вида 
        # Нужно преобразование в словарь
        # Следующая проверка преобразует item в словарь
           #Для {'A', 4} - сет       #Для ['A', 4] - список      #Для ('A', 4) - кортеж
        if type(item) is type(set()) or type(item) is type(list()) or type(item) is type(tuple()):
            temp = list(item)   #Преобразуем item в список, из-за того что элемент в set в Python нельзя получить по индексу
            item = {temp[0] : temp[1]} if type(temp[1]) is type(int()) else {temp[1] : temp[0]}# set сортирует элементы и ключ-значение могут поменяться местами
        self.__items.append(item) # Добавляем элемент в список 
        self.__items.sort(key=lambda item: list(item.values())[0])# Сортируем список по позициям в рейтинге
        self.__setAvarange()   # Обновляем среднее значение 

    def addItems(self, *args): # Добавляем множество элементов за раз
        for arg in args:
            self.addItem(arg)

    def __setAvarange(self):
        sumOfRating = 0 
        for i in self.__items:
            sumOfRating += list(i.values())[0]
        self.__averange = sumOfRating / len(self.__items)

    def getAvarange(self): # Получить среднее значение
        return self.__averange

    def getItems(self): # Получить список 
        return self.__items

obj = RaitingList()

obj.addItems({'A', 5}, {"B", 2}, {"C", 13}, {"D", 11}, {'E', 4})
print(obj.getItems())
print(obj.getAvarange())
