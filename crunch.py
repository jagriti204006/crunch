import optparse 
import itertools

def mainFunc():
        parser = optparse.OptionParser()
        parser.add_option("-s", "--string",
                        dest = "string",
                        help = "string of all characters to be included")
        parser.add_option("-l", "--limit",
                        dest = "limit",
                        help = "limit for number of characters to be included")
                        
        (options, args) = parser.parse_args()
        if not options.string:
                parser.error("Please specify the string of characters to be included")
        if not options.limit:
                parser.error("Please specify the limit of string")
        return options

options = mainFunc()

def crunch1(s, l):
        print("WORDLIST")
        list1 = list(map("".join, itertools.product(s, repeat=int(l))))
        for i in range(len(list1)):
                print(list1[i])


crunch1(options.string, options.limit)



