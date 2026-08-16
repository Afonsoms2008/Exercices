nums1 = {"1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8" : "eight",
        "9": "nine" ,  
        "10": "ten" ,
        "11": "eleven",
        "12": "twelve",
        "13": "thirteen",
        "14": "fourteen", 
        "15": "fifteen",
        "16": "sixteen",
        "17": "seventeen",
        "18": "Eighteen",
        "19" : "nineteen"}
nums2 = {
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety"
}
number = input("Insert the desired number: ")
if int(number) <1 or int(number) >99:
    print("invalid number please insert a number in the range of (1-99)")
elif number in nums1:
    print(f"{nums1[number]}")
elif number[1] == "0":
    print(nums2[number[0]])
elif int(number) >19:
    digit1 = nums2[number[0]]
    digit2 = nums1[number[1]]
    print(f"{digit1}-{digit2}")