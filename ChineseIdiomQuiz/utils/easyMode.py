"""
@author:xiaoshuyui
"""

from pypinyin import lazy_pinyin
import random,os

class wordAndPinyin(object):
    def __init__(self,word,start,end,index):
        # index 是用来进行lambda测试的
        self.word = word 
        self.start = start
        self.end = end
        self.index = index
    
    def __str__(self):
        return self.word 


def getCurrentLocation():
    import sys
    currentLocation = sys.argv[0]
    lastLocation = os.path.abspath(os.path.dirname(currentLocation))
    # print(lastLocation)
    return lastLocation




def getWord(wordList,pinyinList,s = ""):
    if s is None or s == "":
        ind = random.randint(0,len(wordList)-1)
        # print(ind)
        tmp = pinyinList[ind]
        print(wordList[ind])
        l = len(tmp)
        # print(tmp)
        start = tmp[0]
        end = tmp[l-1]
        # print(start)
        # print(end)
        return wordList[ind],start,end
    else:
        # lis = filter(lambda x:x[0] == s,pinyinList)
        pass



def iterator2list(itera):
    res = []
    for i in itera:
        res.append(i)
    return res


def getWordByObj(wpList:list,start = None):
    if None == start or "" == start:
        ind = random.randint(0,len(wpList)-1)
        tmp = wpList[ind]
        word = tmp.word
        wordStart = tmp.start
        wordEnd = tmp.end

        return word,wordStart,wordEnd
    
    else:
        itera = filter(lambda x:x.start == start,wpList)
        lis = iterator2list(itera)

        if len(lis)>1:
            ind = random.randint(0,len(lis)-1)

            tmp = lis[ind]
            word = tmp.word
            wordStart = tmp.start
            wordEnd = tmp.end

            return word,wordStart,wordEnd
        else:
            print("当前词库没有以"+start[0]+"开头的词，重新生成中....")
            ind = random.randint(0,len(wpList)-1)
            tmp = wpList[ind]
            word = tmp.word
            wordStart = tmp.start
            wordEnd = tmp.end           
            return word,wordStart,wordEnd


# def problem()








# if __name__ == "__main__":
def easy():

    lastDir = getCurrentLocation()
    
    #loading chengyu
    fil = open(lastDir+ os.sep+ "words.txt",'r')

    lis = fil.readlines()
    wordSet = set(lis)
    wordLis = list(wordSet)
    print("共有"+str(len(wordLis))+"条成语数据")

    #word  to pinyin
    print("转换成语至拼音......")

    # pinyinLis = []
    assumbleLis = []
    for i in  wordLis:
        # pass
        ii = lazy_pinyin(i.strip())

        l = len(ii)
        # print(tmp)
        start = ii[0]
        end = ii[l-1]

        # print(start)

        ass = wordAndPinyin(i,start[0],end[0],random.randint(0,100))
        assumbleLis.append(ass)
        # print(ii)
        # pinyinLis.append(ii)

    # print(len(pinyinLis))
    print("出题中......")

    # rnd = random.randint(0,len(wordLis)-1)

    print("输入‘q’以终止程序")
    print("游戏开始....")
    # print(wordLis[rnd])

    # getWord(wordLis,pinyinLis)

    # n = 1
    results = []
    _s = ""
    _e = ""

    while 1:
        word,_s,_e = getWordByObj(assumbleLis,_s)
        print(word)
        # print(_s)
        # print(_e)

        inp = input()
        if "q" == inp:
            break
        else:
            # pass
            py = lazy_pinyin(inp)
            if len(py)<4:
                print("输入错误,大概不是个成语")
            else:
                l = len(py)
                sss = py[0]
                eee = py[l-1]
                # print(_s)
                # print("....")
                # print(sss)
                # print(eee)

                if sss[0] == _e:
                    print("bull B")
                    results.append(inp)
                    _s = eee[0]
                else:
                    print("没对上,这个词是以   "+_e+"   结尾的,而你的答案是   "+sss[0]+"   ,重新出题中...")




    #yī

    # lis = filter(lambda x:x.start == "yī",assumbleLis)

    # print(lis)
    # lol = []
    # for i in lis:
    #     lol.append(i)
    
    # print(len(lol))

    # for i in lol:
    #     print(i)
        







    # while 1:
    #     word,start,end = getWord(wordLis,pinyinLis)
    #     # print(word)
    #     print(end)
    #     results.append(word)
    #     inp = input()
    #     if "q" == inp:
    #         break
    #     else:
    #         # pass
    #         py = pinyin(inp)
    #         if len(py)<4:
    #             print("输入错误,大概不是个成语")
    #         else:
    #             l = len(py)
    #             _s = py[0]
    #             _e = py[l-1]
    #             print(_s)

    #             if _s == end:
    #                 print("bull B")
    #                 results.append(inp)
    #             else:
    #                 print("没对上")



    

