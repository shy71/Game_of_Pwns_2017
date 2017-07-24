import urllib2
import re
import sys
countPerson={}
def roman_integer(roman):
    roman = roman.upper() # for taking care of upper or lower case letters
    integer_rep = 0
    roman_to_integer_map = tuple()
    roman_to_integer_map = (('M',1000),
                            ('CM',900),
                            ('D',500),
                            ('CD',400),
                            ('C',100),
                            ('XC',90),
                            ('L',50),
                            ('XL',40),
                            ('X',10),
                            ('IX',9),
                            ('V',5),
                            ('IV',4),
                            ('I',1))
    roman_numeral_pattern = re.compile("""
    ^                   # beginning of string
    M{0,4}              # thousands - 0 to 4 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    """ ,re.VERBOSE)

    if not roman_numeral_pattern.search(roman):
        return 0
    index = 0
    for numeral, integer in roman_to_integer_map:
        while roman[index:index+len(numeral)] == numeral:
            #print numeral, integer, 'matched'
            integer_rep += integer
            index += len(numeral)
    return integer_rep
def findName(text):
	#print text
	return re.search('<div>([A-Z|\ |\']+)</div>',text).group(1).replace(' ','_')

def getPage(url,path):
	try:
		page=urllib2.urlopen(url).read()
		name=findName(page)
		if name in countPerson:
			numName=countPerson[name]+1		
		else:
			numName=1
		countPerson[name]=numName
		
		f=open(path+name+'_'+str(numName)+'.html','wb')
		f.write(page)
	except:
		print 'Error at '+url
def getBook(book,len,path):
	getPage('http://topnovel.net/George_R.R._Martin/'+book+'/index.html',path+book+'/')
	for i in range(len)[1:]:
		getPage('http://topnovel.net/George_R.R._Martin/'+book+'/index_'+str(i+1)+'.html',path+book+'/')
#getBook(sys.argv[1],sys.argv[2],'D:/CTFBook/')


def tranlateLoc(loc,path):
	try:
		book=loc[0][0]
		name=loc[1][0]
		indexName=roman_integer(loc[2][0])
		index=int(loc[3][0])
		f=open(path+book+'/'+name+'_'+str(indexName)+'.html','rb')
		return f.read()[index+3] #Added 3 to index
	except Exception as error:
		print 'Error - ',loc,error
def processArr(arr,path):
	result=[tranlateLoc(item,path) for item in arr]
	print result
	print ''.join(result)
	return result
arr=[
[['A_Dance_with_Dragons'],['DAENERYS'],['IV'],[41149]],
[['A_Storm_of_Swords'],['DAENERYS'],['IV'],[52085]],
[['A_Feast_for_Crows'],['BRIENNE'],['VI'],[39109]],
[['A_Clash_of_Kings'],['DAVOS'],['I'],[44988]],
[['A_Clash_of_Kings'],['TYRION'],['II'],[36009]],
[['A_Dance_with_Dragons'],['DAENERYS'],['IV'],[41149]],
[['A_Storm_of_Swords'],['JON'],['III'],[33534]],
[['A_Storm_of_Swords'],['JON'],['V'],[39518]],
[['A_Clash_of_Kings'],['TYRION'],['III'],[37386]],
[['A_Clash_of_Kings'],['DAVOS'],['I'],[45006]],
[['A_Storm_of_Swords'],['JON'],['III'],[33509]],
[['A_Storm_of_Swords'],['JON'],['III'],[33529]],
[['A_Dance_with_Dragons'],['DAENERYS'],['IV'],[41153]],
[['A_Dance_with_Dragons'],['BRAN'],['II'],[31598]],
[['A_Storm_of_Swords'],['ARYA'],['VII'],[40723]],
[['A_Clash_of_Kings'],['TYRION'],['II'],[36009]],
[['A_Storm_of_Swords'],['ARYA'],['II'],[42898]],
[['A_Feast_for_Crows'],['CERSEI'],['III'],[40671]],
[['A_Clash_of_Kings'],['TYRION'],['IV'],[44377]],
[['A_Dance_with_Dragons'],['REEK'],['I'],[27168]],
[['A_Storm_of_Swords'],['TYRION'],['IV'],[41538]],
[['A_Storm_of_Swords'],['TYRION'],['V'],[35096]], 
[['A_Dance_with_Dragons'],['JON'],['III'],[41951]], 
[['A_Feast_for_Crows'],['ALAYNE'],['II'],[69488]],
[['A_Feast_for_Crows'],['BRIENNE'],['IV'],[55693]],
[['A_Clash_of_Kings'],['TYRION'],['V'],[38202]],
[['A_Dance_with_Dragons'],['TYRION'],['III'],[33921]],
[['A_Storm_of_Swords'],['DAENERYS'],['II'],[54348]],
[['A_Storm_of_Swords'],['BRAN'],['II'],[36222]],
[['A_Clash_of_Kings'],['JON'],['III'],[54485]],
[['A_Dance_with_Dragons'],['TYRION'],['VI'],[52480]],
[['A_Clash_of_Kings'],['THEON'],['III'],[24520]],
[['A_Feast_for_Crows'],['JAIME'],['I'],[42973]],
[['A_Feast_for_Crows'],['BRIENNE'],['III'],[48886]],
[['A_Feast_for_Crows'],['JAIME'],['III'],[56083]], 
[['A_Clash_of_Kings'],['JON'],['IV'],[29298]],
[['A_Feast_for_Crows'],['JAIME'],['III'],[56231]],
[['A_Dance_with_Dragons'],['DAVOS'],['III'],[33099]],
[['A_Clash_of_Kings'],['CATELYN'],['V'],[42797]],
[['A_Storm_of_Swords'],['DAVOS'],['III'],[29714]],
[['A_Dance_with_Dragons'],['DAVOS'],['III'],[33099]],
[['A_Clash_of_Kings'],['CATELYN'],['III'],[38483]],
[['A_Dance_with_Dragons'],['DAENERYS'],['IV'],[41128]],
[['A_Storm_of_Swords'],['JON'],['I'],[38623]],
[['A_Dance_with_Dragons'],['TYRION'],['VI'],[2]],
[['A_Clash_of_Kings'],['TYRION'],['IX'],[40326]],
[['A_Feast_for_Crows'],['SANSA'],['I'],[42098]]]

processArr(arr,'D:/CTFBook/')






