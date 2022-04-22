stop_words = ['able', 'about', 'above', 'abroad', 'according', 'accordingly',
        'across', 'actually', 'adj', 'after', 'afterwards', 'again', 'against',
        'ago', 'ahead', 'aint', 'all', 'allow', 'allows', 'almost', 'alone',
        'along', 'alongside', 'already', 'also', 'although', 'always', 'am',
        'amid', 'amidst', 'among', 'amongst', 'an', 'and', 'another', 'any',
        'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways',
        'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are',
        'arent', 'around', 'as', 'as', 'aside', 'ask', 'asking', 'associated',
        'at', 'available', 'away', 'awfully', 'back', 'backward', 'backwards',
        'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been',
        'before', 'beforehand', 'begin', 'behind', 'being', 'believe', 'below',
        'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both',
        'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant', 'cant',
        'caption', 'cause', 'causes', 'certain', 'certainly', 'changes',
        'clearly', 'cmon', 'co', 'co', 'com', 'come', 'comes', 'concerning',
        'consequently', 'consider', 'considering', 'contain', 'containing',
        'contains', 'corresponding', 'could', 'couldnt', 'course', 'cs',
        'currently', 'dare', 'darent', 'definitely', 'described', 'despite',
        'did', 'didnt', 'different', 'directly', 'do', 'does', 'doesnt',
        'doing', 'done', 'dont', 'down', 'downwards', 'during', 'each', 'edu',
        'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end',
        'ending', 'enough', 'entirely', 'especially', 'et', 'etc', 'even',
        'ever', 'evermore', 'every', 'everybody', 'everyone', 'everything',
        'everywhere', 'ex', 'exactly', 'example', 'except', 'fairly', 'far',
        'farther', 'few', 'fewer', 'fifth', 'first', 'five', 'followed',
        'following', 'follows', 'for', 'forever', 'former', 'formerly',
        'forth', 'forward', 'found', 'four', 'from', 'further', 'furthermore',
        'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going',
        'gone', 'got', 'gotten', 'greetings', 'had', 'hadnt', 'half',
        'happens', 'hardly', 'has', 'hasnt', 'have', 'havent', 'having', 'he',
        'hed', 'hell', 'hello', 'help', 'hence', 'her', 'here', 'hereafter',
        'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes',
        'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit',
        'however', 'hundred', 'id', 'ie', 'if', 'ignored', 'ill', 'im',
        'immediate', 'in', 'inasmuch', 'inc', 'inc', 'indeed', 'indicate',
        'indicated', 'indicates', 'inner', 'inside', 'insofar', 'instead',
        'into', 'inward', 'is', 'isnt', 'it', 'itd', 'itll', 'its', 'its',
        'itself', 'ive', 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'known',
        'knows', 'last', 'lately', 'later', 'latter', 'latterly', 'least',
        'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'likewise',
        'little', 'look', 'looking', 'looks', 'low', 'lower', 'ltd', 'made',
        'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'maynt', 'me',
        'mean', 'meantime', 'meanwhile', 'merely', 'might', 'mightnt', 'mine',
        'minus', 'miss', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs',
        'much', 'must', 'mustnt', 'my', 'myself', 'name', 'namely', 'nd',
        'near', 'nearly', 'necessary', 'need', 'neednt', 'needs', 'neither',
        'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 'nine',
        'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone',
        'noone', 'nor', 'normally', 'not', 'nothing', 'notwithstanding',
        'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh',
        'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'ones', 'only',
        'onto', 'opposite', 'or', 'other', 'others', 'otherwise', 'ought',
        'oughtnt', 'our', 'ours', 'ourselves', 'out', 'outside', 'over',
        'overall', 'own', 'particular', 'particularly', 'past', 'per',
        'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably',
        'probably', 'provided', 'provides', 'que', 'quite', 'qv', 'rather',
        'rd', 're', 'really', 'reasonably', 'recent', 'recently', 'regarding',
        'regardless', 'regards', 'relatively', 'respectively', 'right',
        'round', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second',
        'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems',
        'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously',
        'seven', 'several', 'shall', 'shant', 'she', 'shed', 'shell', 'shes',
        'should', 'shouldnt', 'since', 'six', 'so', 'some', 'somebody', 'someday',
        'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat',
        'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying',
        'still', 'sub', 'such', 'sup', 'sure', 'take', 'taken', 'taking',
        'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that',
        'thatll', 'thats', 'thats', 'thatve', 'the', 'their', 'theirs', 'them',
        'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby',
        'thered', 'therefore', 'therein', 'therell', 'therere', 'theres',
        'theres', 'thereupon', 'thereve', 'these', 'they', 'theyd', 'theyll',
        'theyre', 'theyve', 'thing', 'things', 'think', 'third', 'thirty',
        'this', 'thorough', 'thoroughly', 'those', 'though', 'three',
        'through', 'throughout', 'thru', 'thus', 'till', 'to', 'together',
        'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try',
        'trying', 'ts', 'twice', 'two', 'un', 'under', 'underneath', 'undoing',
        'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up',
        'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using',
        'usually', 'v', 'value', 'various', 'versus', 'very', 'via', 'viz',
        'vs', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome',
        'well', 'well', 'went', 'were', 'were', 'werent', 'weve', 'what',
        'whatever', 'whatll', 'whats', 'whatve', 'when', 'whence', 'whenever',
        'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres',
        'whereupon', 'wherever', 'whether', 'which', 'whichever', 'while',
        'whilst', 'whither', 'who', 'whod', 'whoever', 'whole', 'wholl',
        'whom', 'whomever', 'whos', 'whose', 'why', 'will', 'willing', 'wish',
        'with', 'within', 'without', 'wonder', 'wont', 'would', 'wouldnt',
        'yes', 'yet', 'you', 'youd', 'youll', 'your', 'youre', 'yours',
        'yourself', 'yourselves', 'youve', 'zero', 'a', 'hows', 'i', 'whens',
        'whys', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'uucp', 'w', 'x', 'y', 'z', 'i', 'www',
        'amount', 'bill', 'bottom', 'call', 'computer', 'con', 'couldnt',
        'cry', 'de', 'describe', 'detail', 'due', 'eleven', 'empty', 'fifteen',
        'fifty', 'fill', 'find', 'fire', 'forty', 'front', 'full', 'give',
        'hasnt', 'herse', 'himse', 'interest', 'itse', 'mill', 'move', 'myse',
        'part', 'put', 'show', 'side', 'sincere', 'sixty', 'system', 'ten',
        'thick', 'thin', 'top', 'twelve', 'twenty', 'abst', 'accordance',
        'act', 'added', 'adopted', 'affected', 'affecting', 'affects', 'ah',
        'announce', 'anymore', 'apparently', 'approximately', 'aren', 'arent',
        'arise', 'auth', 'beginning', 'beginnings', 'begins', 'biol',
        'briefly', 'ca', 'date', 'ed', 'effect', 'etal', 'ff', 'fix', 'gave',
        'giving', 'heres', 'hes', 'hid', 'home', 'id', 'im', 'immediately',
        'importance', 'important', 'index', 'information', 'invention', 'itd',
        'keys', 'kg', 'km', 'largely', 'lets', 'line', 'll', 'means', 'mg',
        'million', 'ml', 'mug', 'na', 'nay', 'necessarily', 'nos', 'noted',
        'obtain', 'obtained', 'omitted', 'ord', 'owing', 'page', 'pages',
        'poorly', 'possibly', 'potentially', 'pp', 'predominantly', 'present',
        'previously', 'primarily', 'promptly', 'proud', 'quickly', 'ran',
        'readily', 'ref', 'refs', 'related', 'research', 'resulted',
        'resulting', 'results', 'run', 'sec', 'section', 'shed', 'shes',
        'showed', 'shown', 'showns', 'shows', 'significant', 'significantly',
        'similar', 'similarly', 'slightly', 'somethan', 'specifically',
        'state', 'states', 'stop', 'strongly', 'substantially', 'successfully',
        'sufficiently', 'suggest', 'thered', 'thereof', 'therere', 'thereto',
        'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til',
        'tip', 'ts', 'ups', 'usefully', 'usefulness', 've', 'vol', 'vols',
        'wed', 'whats', 'wheres', 'whim', 'whod', 'whos', 'widely', 'words',
        'world', 'youd', 'youre']


def Word_Order_Frequency_One_Book (Book, Word_Order, File_Output):

    if Word_Order!=1 and Word_Order!=2:
        print("Error! | Word Order must be 1 or 2!")
        return
        
    try:
        book_f = open(Book,'r',encoding='utf-8-sig') # open the file
        word_list = [] # create a list for storing words in file Book
        finish_words = '*** END OF THE PROJECT GUTENBERG EBOOK'
        start_words = '*** START OF THE PROJECT GUTENBERG EBOOK'
        
        for line in book_f: # find the start of the book
            if line.find(start_words)==0:
                break
        for line in book_f:
            if line.find(finish_words)==0: # if line is end of book, break
                break
            line = list(line.split()) 
            if len(line)!=0: # if the line read is not empty or only contains linefeed(\n)
                words_wanted = [] # create a temporary list to choose which words to add in word_list
                for i in range(len(line)): # scroll line to focus on words
                    control=0
                    line[i] = (line[i]).lower() # lower the word
                    strtolist = list(line[i]) # create a temporary list to edit a word string easily.
                    temp = [] # create a temporary list to keep edited word.
                    for k in range(len(strtolist)): # arrange the word's list to only contain alphabetic characters
                        if ord(strtolist[k])>=ord('a') and ord(strtolist[k])<=ord('z'):
                            temp.append(strtolist[k])
                    temp = ''.join([str(item) for item in temp]) # turn the list temp into string
                    for j in stop_words: # remove the stop words
                        if temp==j:
                            control=1
                    if control==0 and temp!='':
                        words_wanted.append(temp) # append temp in the list words_wanted
                word_list+= words_wanted
        book_f.close() # close the file
        
        freq = {} # create a dictionary to store words and counts
        
        if Word_Order==1: 
            word_list.sort() # sort the word_list to make counting easier.
            i=0
            while i<len(word_list)-1:
                k=i
                count=0
                while k<len(word_list) and word_list[i]==word_list[k]:
                    count+=1
                    k+=1
                freq.update({word_list[i] : count}) # after counting a word, update the freq dict to store frequency of the word.
                i = k   
        
        elif Word_Order==2:
            word_list2 = [] # create another word list to store strings of two words
            for i in range(0,len(word_list)//2): 
                tmp = word_list[2*i] + " " + word_list[2*i+1]
                word_list2.append(tmp)
            word_list2.sort() # sort to make counting easier
            i=0
            while i<len(word_list2)-1:
                k=i
                count=0
                while k<len(word_list) and word_list2[i]==word_list2[k]:
                    count+=1
                    k+=1
                freq.update({word_list2[i] : count}) # after counting string of two words, update the freq dict to store frequency of the string.
                i = k
            
        freq = dict(sorted(freq.items(), key=lambda x: x[1],reverse=True)) # sort dictionary in descending order according to frequency of words
        
        # and lastly, print the results to file
        out = open(File_Output, 'w',encoding='utf-8')
        out.write("|    WORD        |                 WORD                      |\n")
        out.write("|    ORDER       |                 ORDER                     |\n")
        out.write("|    FREQUENCY   |                 SEQUENCE                  |\n")
        out.write("-----------------|--------------------------------------------\n")
        for key in freq:
            out.write("\t")
            out.write("{:9}".format(freq[key]))
            out.write("|")
            out.write("{:9}".format(key))
            out.write("\n")
        out.close()
        
        
    except FileNotFoundError:
        print("No such file or directory: ", Book)
    except:
        print("An error occured.")
    
    



################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################



def Word_Order_Frequency_Two_Books (Book_1, Book_2, Word_Order, File_Output):
    
    if Word_Order!=1 and Word_Order!=2:
        print("Error! | Word Order must be 1 or 2!")
        return
    
    '''
    - create three lists:
            one to store all words in both books
            one to store all words in Book_1
            one to store all words in Book_2
    '''
    word_list = []
    word_list1 = []
    word_list2 = []
    
    finish_words = '*** END OF THE PROJECT GUTENBERG EBOOK'
    start_words = '*** START OF THE PROJECT GUTENBERG EBOOK'
    
    ### READING THE FIRST BOOK ###
    try:
        book_f = open(Book_1,'r',encoding='utf-8-sig') # open the file
        for line in book_f: # find the start of the book
            if line.find(start_words)==0:
                break
        for line in book_f:
            if line.find(finish_words)==0: # if line is end of book, break
                break
            line = list(line.split())
            if len(line)!=0: # if the line read is not empty or only contains linefeed(\n)
                words_wanted = [] # create a temporary list to choose which words to add in word_list
                for i in range(len(line)): # scroll line to focus on words
                    control=0
                    line[i] = (line[i]).lower() # lower the word
                    strtolist = list(line[i]) # create a temporary list to edit a word string easily.
                    temp = [] # create a temporary list to keep edited word.
                    for k in range(len(strtolist)): # arrange the word's list to only contain alphabetic characters
                        if ord(strtolist[k])>=ord('a') and ord(strtolist[k])<=ord('z'):
                            temp.append(strtolist[k])
                    temp = ''.join([str(item) for item in temp]) # turn the list temp into string
                    for j in stop_words: # remove the stop words
                        if temp==j:
                            control=1
                    if control==0 and temp!='':
                        words_wanted.append(temp) # append temp in the list words_wanted
                word_list1+= words_wanted    
        book_f.close() # close the file
        
    except FileNotFoundError:
        print("Error! No such file or directory: ", Book_1)
        return
    except:
        print("An error occured.")
        return
    
    ### READING THE SECOND BOOK ###
    try:
        book_f = open(Book_2,'r',encoding='utf-8-sig') # open the file
        for line in book_f: # find the start of the book
            if line.find(start_words)==0:
                break
        for line in book_f:
            if line.find(finish_words)==0: # if line is end of book, break
                break
            line = list(line.split()) 
            if len(line)!=0: # if the line read is not empty or only contains linefeed(\n)
                words_wanted = [] # create a temporary list to choose which words to add in word_list
                for i in range(len(line)): # scroll line to focus on words
                    control=0
                    line[i] = (line[i]).lower() # lower the word
                    strtolist = list(line[i]) # create a temporary list to edit a word string easily.
                    temp = [] # create a temporary list to keep edited word.
                    for k in range(len(strtolist)): # arrange the word's list to only contain alphabetic characters
                        if ord(strtolist[k])>=ord('a') and ord(strtolist[k])<=ord('z'):
                            temp.append(strtolist[k])
                    temp = ''.join([str(item) for item in temp]) # turn the list temp into string
                    for j in stop_words: # remove the stop words
                        if temp==j:
                            control=1
                    if control==0 and temp!='':
                        words_wanted.append(temp) # append temp in the list words_wanted
                word_list2+= words_wanted    
        book_f.close() # close the file
        
    except FileNotFoundError:
        print("No such file or directory: ", Book_2)
        return
    except:
        print("An error occured.")
        return
    
    '''
    - create three dictionaries:
            one to store the frequencies of the words in Book_1
            one to store the frequencies of the words in Book_2
            one to store the frequencies of all the words in Book_1 and Book_2
    '''
    freq_bk_2 = {}
    freq_bk_1 = {}
    freq_total = {}
    
    
    if Word_Order==1:
        word_list1.sort() # sort the word_list1 to make counting easier.
        i=0
        while i<len(word_list1)-1:
            k=i
            count=0
            while k<len(word_list1) and word_list1[i]==word_list1[k] :
                count+=1
                k+=1
            freq_bk_1.update({word_list1[i] : count}) # after counting a word, update the freq dict to store frequency of the word.
            i = k  
        
        word_list2.sort() # sort the word_list2 to make counting easier.
        i=0
        while i<len(word_list2)-1:
            k=i
            count=0
            while k<len(word_list2) and word_list2[i]==word_list2[k]:
                count+=1
                k+=1
            freq_bk_2.update({word_list2[i] : count}) # after counting a word, update the freq dict to store frequency of the word.
            i = k   
        
        
        word_list += word_list1
        word_list += word_list2
        word_list.sort() # put all the words in word_list1 and word_list2 and sort the word_list to make counting easier

        i=0
        while i<len(word_list)-1:
            k=i
            count=0
            while k<len(word_list) and word_list[i]==word_list[k]:
                count+=1
                k+=1
            freq_total.update({word_list[i] : count}) # after counting a word, update the freq dict to store frequency of the word.
            i = k
            
    if Word_Order==2:
        '''
        - create 2 word lists to store strings of two words
                one to store strings of word_list1
                one to store strings of word_list2
        '''
        word_list1_2 = []
        word_list2_2 = []
        
        for i in range(0,len(word_list1)//2):
            tmp = word_list1[2*i] + " " + word_list1[2*i+1]
            word_list1_2.append(tmp)
        word_list1_2.sort() # sort to make counting easier
        i=0
        while i<len(word_list1_2)-1:
            k=i
            count=0
            while k<len(word_list1_2) and word_list1_2[i]==word_list1_2[k]:
                count+=1
                k+=1
            freq_bk_1.update({word_list1_2[i] : count}) # after counting string of two words, update the freq dict to store frequency of the string.
            i = k
        
        for i in range(0,len(word_list2)//2):
            tmp = word_list2[2*i] + " " + word_list2[2*i+1]
            word_list2_2.append(tmp)
        word_list2_2.sort()# sort to make counting easier
        i=0
        while i<len(word_list2_2)-1:
            k=i
            count=0
            while k<len(word_list2_2) and word_list2_2[i]==word_list2_2[k]:
                count+=1
                k+=1
            freq_bk_2.update({word_list2_2[i] : count}) # after counting string of two words, update the freq dict to store frequency of the string.
            i = k
        
        word_list += word_list1_2
        word_list += word_list2_2
        word_list.sort() # put all the words in word_list1 and word_list2 and sort the word_list to make counting easier

        i=0
        while i<len(word_list)-1:
            k=i
            count=0
            while k<len(word_list) and word_list[i]==word_list[k]:
                count+=1
                k+=1
            freq_total.update({word_list[i] : count})  # after counting string of two words, update the freq dict to store frequency of the string.
            i = k
        
              
    freq_total = dict(sorted(freq_total.items(), key=lambda x: x[1],reverse=True))  # sort dictionary in descending order according to frequency of words
    
    # and lastly, print the results to file
    out = open(File_Output, 'w',encoding='utf-8')
    out.write("|    TOTAL       |    BOOK 1      |    BOOK 2      |               WORD                     |\n")
    out.write("|    ORDER       |    ORDER       |    ORDER       |               ORDER                    |\n")
    out.write("|    FREQUENCY   |    FREQUENCY   |    FREQUENCY   |               SEQUENCE                 |\n")
    out.write("-----------------|----------------|----------------|-----------------------------------------\n")
    
    for key in freq_total:
        out.write("\t")
        out.write("{:9}".format(freq_total[key]))
        out.write("|")
        out.write("{:16}".format(freq_bk_1.setdefault(key, 0)))
        out.write("|")
        out.write("{:16}".format(freq_bk_2.setdefault(key, 0)))
        out.write("|")
        out.write("{:40}".format(key))
        out.write("\n")
    out.close()
    

