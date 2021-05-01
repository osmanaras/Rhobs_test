
The script allows to run the below exercices devlopped in pyhon for an internship test.

1. The number of listeners by music.
2. The average age by music.
3. The pyramid age: the function should take 2 parameters a city and slice size. Compute the pyramid only for that city. The slice size is the number of years by which you aggregate people (for example 10 by 10 or  3y by 3y).


Script parameters : 
	--run : run the exercice. this paramater can take the follows values exo1, exo2, exo3 and all
	--dataPath : the json file path which contains the datas
	--city : the of a city, need only when you want to run exo3. By defaulft is equal to Gay
	--slice : fix the slice for the age. By default is equal to 10


EXAMPLE : 

python interview_test.py --dataPath path/to/json/data.json --run all --city 'Gay' --slice 5

Result :


Exercice 1 : The number of listeners by music.

Result :
{'country': 18971, 'blues': 20817, 'hiphop': 28043, 'metal': 27774, 'rock': 34472, 'disco': 34297, 'pop': 32249, 'reggae': 19127, 'jazz': 24304, 'gabber': 18525, 'trance': 18173, 'eurodance': 23487, 'classical': 21306}


Exercice 2 : The average age by music.

Result :
{'country': 42, 'blues': 50, 'hiphop': 39, 'metal': 38, 'rock': 43, 'disco': 43, 'pop': 41, 'reggae': 39, 'jazz': 47, 'gabber': 38, 'trance': 40, 'eurodance': 39, 'classical': 47}


Exercice 3 : The pyramid age: the function should take 2 parameters a city and slice size. Compute the pyramid only for that city. The slice size is the number of years by which you aggregate people

Result :
{'Age': ['0-5', '6-10', '11-15', '16-20', '21-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51-55', '56-60', '61-65', '66-70', '71-75', '76-80', '81-85', '86-90', '91-95', '96-100', '101-105'], 'Pop': [0, 7, 92, 330, 476, 439, 546, 355, 345, 289, 227, 215, 200, 212, 152, 163, 48, 39, 20, 22, 2]}