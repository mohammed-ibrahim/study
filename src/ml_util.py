# -*- coding: utf-8 -*-

arabic_to_english_numbers = {u"٠":"0",u"١":"1",u"٢":"2",u"٣":"3",u"٤":"4",u"٥":"5",u"٦":"6",u"٧":"7",u"٨":"8",u"٩":"9"}
english_to_arabic_numbers = dict((v,k) for k,v in arabic_to_english_numbers.iteritems())

def getNumberInArabic(number):
    strNum = str(number)
    val = ""

    for char in strNum:
        val = val + english_to_arabic_numbers[char]

    return val

if __name__ == '__main__':
    for i in range(1, 500):
        print(getNumberInArabic(i))
