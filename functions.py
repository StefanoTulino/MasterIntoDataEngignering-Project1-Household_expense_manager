import csv
import os
import datetime


"""
Constant
"""
FILENAME="household expense manager.csv"

"""
This function verify if is a file
"""
def check_exist_file():
    if os.path.isfile(FILENAME):
        return True
        

"""
This function verify if the file is not empty
"""
def is_not_empty_file():
    if os.path.getsize(os.path.basename(FILENAME))!=0:
        return True


"""
This function writes to a csv file

:param date= date entered
:param description= description entered
:param amount= amount entered
"""
def writing_to_csv_file(date,description,amount):
    with open(FILENAME,"a+", newline='\n') as csv_file:
                columns=["date","description","amount"]
                
                """
                Writing on csv file
                """
                csv_writer= csv.DictWriter(csv_file,fieldnames=columns)
                
                """
                Check if the file is empty
                """
                if  is_not_empty_file():
                        csv_writer.writerow({"date":date,"description":description,"amount":amount})
                else:
                    """
                    Write header of the csv file
                    """
                    csv_writer.writeheader()
                    csv_writer.writerow({"date":date,"description":description,"amount":amount})


"""
This function reads to a csv file

:param date_selected_str= date entered
"""
def reading_to_csv_file(date_selected_str):
    total_amount=0
    
    """
    Convert a string to a date.
    Y for year complete(example 2024)
    """
    date_selected= datetime.datetime.strptime(date_selected_str,"%Y-%m")
    
    """
    Reading from a csv file
    """
    with open(FILENAME) as csv_file:
        csv_reader= csv.reader(csv_file)
        for i,row in list(enumerate(csv_reader)):
            if i!=0:
                date_csv= datetime.datetime.strptime(row[0],"%Y-%m-%d %H:%M:%S")
                if date_selected.year==date_csv.year and date_selected.month==date_csv.month:
                    total_amount+= float(row[2])
                    
        if total_amount>0:
            print(f"L'importo totale per la data dell'anno {date_selected.year}-{str(date_selected.month).zfill(2)} è = ",total_amount)  
        else:
            print(f"Per il periodo selezionato, ovvero {date_selected.year}- {str(date_selected.month).zfill(2)} NON è presente nessuna spesa")


"""
This function returns the 10 transactions with the largest amount

:param None
"""
def reading_10max_transaction():
    dict_csv={}
    res={}
    with open(FILENAME) as csv_file:
        """
        Reading from a csv file nd get a DictReader object
        """
        dict_csv= csv.DictReader(csv_file)
         
        """
        Use of a function sorted, that return a list with the first 10 items sorted by amount
        """
        res= sorted(dict_csv, key=lambda row: float(row['amount']), reverse=True)[:10] 
        if(len(res)<10):
            print("Ci sono meno di 10 transazioni") 
        for i,row in list(enumerate(res)):
            print(f"La transazione nr. {i+1} ha i seguenti dati:", row["date"], row["description"], row["amount"])