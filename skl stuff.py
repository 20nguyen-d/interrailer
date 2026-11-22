import re

raw_data = """
Abdelghaffar, Samy  12MGN	
Abdulsalam, Faeeson  12DJG	
Abrol, Karan  12MGN	
Achu-Mofor, Harvey  12JDF	
Addo, Coco  12JEA	
Adedayo, Kanyin  12ECG	
Adedayo-Akinola, Owen  12JEA	
Adekoya, Angel  12MGN	
Adeoya, Igwe  12HJO	
Adhikari, Ashna  12HJO	
Ahmad, Aliza  12ECG	
Akhtar, Zakariya  12ECG	
Akinyele, Michael  12JEA	
Aloomian, Amelia  12JJ	
Alwan, Sienna  12DJG	
Amenyo, Selasi  12JJ	
Amoako, Baaba  12HJO	
Andruszkiewicz Ayala, Zonnia  12JEA	
Arendt, Tymon  12JEA	
Ashcroft-To, Reed  12AJD	
Asker, Mim  12DJG	
Atwal, Aman  12AJD	
Austin, Harry  12CBE	
Baker, Claudia  12JJ	
Balint, Lara  12JDF	
Balogun, Jonathan  12HJO	
Banks, Dylan  12HJO	
Barnes, Joel  12AJD	
Baruwa, Jericho  12CBE	
Beard, Corey  12JDF	
Benedict, William  12JJ	
Bennett, Liam  12JDF	
Berglund, Alfred  12HJO	
Bharathi, Darshan  12DJG	
Blair-Hicks, Jonah  12CBE	
Box, Molly  12AJD	
Boyd, James  12JEA	
Branch, Jaelah  12ECG	
Brett, Sam  12MGN	
Brighton, Will  12AJD	
Bryan, Lewis  12HJO	
Brzeg, Jacek  12JJ	
Chance, Jude  12CBE	
Chongbang, Nimisha  12AJD	
Chu, Steven  12MGN	
Chukwu-Ike, Shammael  12JDF	
Ciurca, Lydia  12DJG	
Clements, Bess  12JJ	
Colaiacomo, Alice  12JDF	
Cox, Ellie  12JEA	
Cox, Tyler  12JJ	
Cunningham, Shay  12DJG	
Dahir, Jibril  12HJO	
Dalrymple-Hayfron, Zach  12HJO	
Danilczuk, Jerzy  12MGN	
Darvishi, Ariana  12DJG	
Davidson, Adam  12MGN	
Davis, Jessica  12JJ	
De Jongh Martin, Diego  12JDF	
De Mel, Devin  12MGN	
De Souza-Plans, Rafael  12DJG	
Djekou, Mykaela  12ECG	
Doskenova, Adel  12JEA	
Durand, Daniel  12DJG	
El-Labban, Adam  12JEA	
Emmanuel, David-Prince  12ECG	
Escobar, Abigail  12DJG	
Eshfaqur, Eshaan  12HJO	
Evans, Layla  12DJG	
Evans, Rowan  12ECG	
Faola, Anthony  12MGN	
Farram, Sidney  12DJG	
Filer, Holly  12AJD	
Flottweg, Jacob  12AJD	
Foley, Jessica  12JJ	
Fortt, Lucy  12AJD	
Fosh, Sophie  12AJD	
Furlong, Charlie  12AJD	
Gabriel Leven, Hailey  12JEA	
Gbanha-Bawa, Bawa  12JEA	
Ghaffar, Zayan  12JDF	
Gordynska, Christine  12MGN	
Gorman, Isabelle  12CBE	
Griffin, Lev  12HJO	
Grogan, Billy  12JJ	
Grogan, George  12HJO	
Gurung, Siddharth  12MGN	
Gutaj, Endri  12MGN	
Hazlewood, Sophia  12HJO	
Hewitt, Eva  12ECG	
Hill, Olivia  12AJD	
Houston, Ronan  12JJ	
Hoyte, Yuri  12DJG	
Huang, Sophie  12MGN	
Huggett, Isabella  12DJG	
Hundal, Manveer  12DJG	
Hyde, Zosia  12AJD	
Ismail, Danyaal  12AJD	
Izekor, Marvel  12JJ	
James, Stephen  12JDF	
Jaroszewicz, Natalia  12JJ	
Jeffrey, Theo  12CBE	
Jia, Tom  12AJD	
Johnson, Madison  12DJG	
Jusu, Samuel  12ECG	
Kaminska, Nel  12AJD	
Karki, Aashraya  12AJD	
Karki, Samir  12JJ	
Kelly, Sadie  12ECG	
Kenny, Cameron  12JDF	
Kidby, Rebecca  12MGN	
Kimmakon, Rachel  12ECG	
King, Phillip  12MGN	
Kitchener, Harry  12JJ	
Knights, Olivia  12JEA	
Kombo, Nimi  12JJ	
Koneswaran, Thipiga  12CBE	
Koziol, Dominik  12JJ	
Krishnan, Anshika  12MGN	
Kundi, Ajeet  12JEA	
Kyriakakis, Stelios  12JJ	
Lai, Angel  12JJ	
Laing, Ariana  12HJO	
Laming, Millie  12JEA	
Lear, Daniel  12JEA	
Luckman, Louis  12JEA	
Luong, Angela  12CBE	
Luu, Alex  12ECG	
Machida, Ayaka  12DJG	
MacIntyre-Smith, George  12HJO	
Maitanmi, Kanyinsola  12JDF	
Malik, Abdullah  12CBE	
Manolakou, Astarti  12HJO	
Marian, Nikhil  12JDF	
Matharu, Nimrat  12ECG	
Matharu, Rohan  12CBE	
Matin-Barbera, Alex  12ECG	
Matthews, Dexter  12MGN	
McCann, Caleb  12CBE	
McNamara, Sunny  12HJO	
Mebtouche, Ryan  12JDF	
Mecaj, Elin  12MGN	
Meltser, Pauline  12JDF	
Mensa-Bonsu, Jade  12CBE	
Mian, Zaki  12ECG	
Mikalauskas, Adrijus  12JEA	
Mitchev, Yoan  12CBE	
Mitkova, Darina  12DJG	
Moreton, Liv  12ECG	
Mukasa, Noah  12CBE	
Muslu, Hina  12CBE	
Musov, Berad  12DJG	
Nalepa, Caspar  12HJO	
Newton, Eloise  12HJO	
Nguyen, Diep Anh  12CBE	
Nguyen, Mia  12JJ	
Nollah, Jemima  12CBE	
Nugent, Aaron  12CBE	
Nugent, Daniel  12MGN	
Nwanebo, Chuks  12AJD	
Nwonye, Georgia  12MGN	
Odion, Wesley  12DJG	
Odutayo, Fope  12HJO	
O'Grady-Hills, Keir  12ECG	
O'Grady-Hills, Lewis  12DJG	
Okafor, Chibu  12JEA	
Olanrewaju, Rotimi  12ECG	
Olsen, Jemimah  12JEA	
Omoyajowo, Jomiloju  12JJ	
Orimoloye, Tobi  12AJD	
Osei-Tutu, Caitlyn  12CBE	
Oshogwe, Prince  12JEA	
Owen, Raef  12DJG	
Oyeleye, Ibukun  12AJD	
Pai, Anagha  12AJD	
Pang, Kobe  12ECG	
Pardo, Sebastian  12DJG	
Patel, Krishaal  12HJO	
Pathak, Nirali  12JEA	
Pathmaruban, Rohisan  12MGN	
Paudyal, Reason  12HJO	
Paul-Taiwo, Omolade  12JEA	
Peters, Lucas  12MGN	
Petrescu, Sophia  12JJ	
Pindoria, Yuv  12ECG	
Pooley, Samuel  12JDF	
Porte, Lucy  12JEA	
Potocnik Hahonina, Anna  12JDF	
Quinn, Daniel  12DJG	
Ragg, Daniel  12CBE	
Raiyan, Ahmed  12MGN	
Ranchod, Amiya  12HJO	
Raphael, Isabelle  12JEA	
Rawal, Josh  12JDF	
Richardson, Macie  12AJD	
Roach, Shay  12AJD	
Roka, Pratosh  12JEA	
Rooney-Douillet, Kate  12JJ	
Rygielska, Sofie  12JJ	
Sackey-James, Reuben  12DJG	
Sahni, Shudhit  12JDF	
Sakyi, Sarah  12MGN	
Sehota, Arjan  12CBE	
Selfi, Zahra  12ECG	
Sharma, Aaron  12JEA	
Sirco, Emily  12MGN	
Smith, Cameron  12CBE	
Smith, Hannah  12CBE	
Solomon-Knox, Persia  12AJD	
Sottin, Joshua  12JEA	
Spencer-Lewis, Bea  12CBE	
Spicer, Louis  12HJO	
Stanchev, Alex  12JJ	
Steininger, Finlay  12MGN	
Stoyanova, Anastasia  12HJO	
Suresh, Austin  12CBE	
Taflaj, Maxim  12CBE	
Talukder, Nadid  12JDF	
Tanner, Keiton  12ECG	
Thapa, Prachi  12DJG	
Thapa, Purnima  12CBE	
Tokarski, Sebastian  12AJD	
Tourral-Hopkins, Maia  12JDF	
Tran, Ayana  12DJG	
Tukala, Deslee  12AJD	
Turner, Maeve  12ECG	
Tyler, Ella  12ECG	
Underhill, Henry  12JDF	
Unsworth, Ruby  12AJD	
Uttridge, Finley  12JDF	
Vacarciuc, Oscar  12JJ	
Vaid, Amar  12JJ	
Vedamuthu, Adi  12CBE	
Vekeria, Aydan  12ECG	
Viza-Goghiu, Marco  12JDF	
Vorotovic, Zeta  12ECG	
Vrionides, James  12ECG	
Wahba, Anastasia  12JDF	
Walker, Zack  12HJO	
Walton, Fynn  12HJO	
Ward, Isabella  12JDF	
Ward, Sam  12DJG	
White, Bethany  12HJO	
Wilmot, Sebastian  12JEA	
Wynne, Conor  12AJD	
"""

names = []

for line in raw_data.splitlines():
    line = line.strip()

    if line == "":
        continue
    line = re.sub(r"\s+12\S+$", "", line)
    last_name, first_name = line.split(",", 1)

    names.append([first_name.strip(), last_name.strip()])

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def isPrime(num):

    flag = False

    if num == 0 or num == 1:
        return False
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break

        return flag == False

def getTotal(name):
    total = 0
    name = name.lower()
    print(name)
    for x in name:
        if x in alphabet:
            total += alphabet.index(x) + 1
    return total

def firstAndLast():
    nameTotals = []
    for x in names:
        nameTotals.append(getTotal(str(x[0] + x[1])))

    for x in range(len(nameTotals)):
        if isPrime(nameTotals[x]):
            print(names[x], nameTotals[x])

def firstOnly():
    nameTotals = []
    for x in names:
        nameTotals.append(getTotal(str(x[0])))

    for x in range(len(nameTotals)):
        if isPrime(nameTotals[x]):
            print(names[x], nameTotals[x])

print(firstAndLast())

print(getTotal('nguyenlelamanh'))