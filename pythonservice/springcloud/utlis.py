def getWordDic():    """    读取词典文件    载入词典    :return:    """    words_dic = []    with open("dic/dic.txt", "r", encoding="utf8") as dic_input:        for word in dic_input:            words_dic.append(word.strip())    return words_dic