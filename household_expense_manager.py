### TRACCIA:
# Gestore delle spese domestiche
#Realizzare un gestore delle spese domestiche in Python.
#Questa applicazione deve mostrare all’utente un menu con le operazioni da svolgere, che sono:
#[1] Aggiungi una transazione
#[2] Report mensile
#[3] Top 10 transazioni

#L’applicazione chiede all’utente di immettere il numero relativo alla funzione scelta.
#Se l’utente sceglie 1 gli viene chiesto di inserire la data della transazione in formato GG/MM/AAAA, la descrizione e l’importo. Tutto in un unico 
#input (es. 18/05/2024 Cena al ristorante 45).

#L’applicazione popola un file in formato CSV con questi dati e, una volta immessi, ritorna al menu principale.

#Se l’utente sceglie l’opzione 2 (report mensile), viene stampato a schermo l’importo totale transato ripartito per anno e mese, 
#come nell’esempio seguente:
#2024-05 324

#Se l’utente sceglie l’opzione 3 (top 10 transazioni) vengono stampate data, descrizione e importo delle 10 transazioni di importo maggiore, 
#come nell’esempio seguente:
#18/06/2023 Rata mutuo 1231


#----------------------------------------------------------------------------------------


import csv
import datetime
import functions as f


def answer_user1():
        try:
            insert_row=input("Inserire la data della transazione in formato GG/MM/AAAA, la descrizione e l’importo."+
            "Tutto su un'unica linea e con questo formato (es: 10/10/2010, Cena, 45)= ")
            
            date,description,amount= insert_row.split(", ")
            date= datetime.datetime.strptime(date,"%d/%m/%Y")            
            f.writing_to_csv_file(date,description,amount)
            
        except ValueError as v:
            print("I valori inseriti non sono nel formato corretto\n")
            print(v,"\n")
        except Exception as e:
            print(e,"\n")


def answer_user2():
    try:
        date_selected_str= input("Inserire l'anno ed il mese di cui ricevere il report mensile (formato AAAA-MM)= ")
        f.reading_to_csv_file(date_selected_str)
        
    except ValueError as v:
        print("I valori inseriti non sono nel formato corretto\n")
        print(v,"\n")
   
    except Exception as e:
        print(e,"\n")


def answer_user3():
    try:
       f.reading_10max_transaction()
                
    except Exception as e:
        print(e,"\n")


#------------------------------------------------

"""
MAIN
"""

"""
Variable
"""
answer_user_continue=True

while answer_user_continue:
    answer_user= input("\nScegli tra le seguenti opzioni (indicare uno dei numeri elencati tra parentesi quadre):\n"+ 
            "[1] Aggiungi una transazione\n"+"[2] Report mensile\n"+"[3] Top 10 transazioni\n"+"Qualunque altro numero per uscire= ")

# Request Number 1
    if answer_user == "1":
        answer_user1()

# Request Number 2
    elif answer_user == "2":
        if not f.check_exist_file():
            print("Il file non esiste: impossibile eseguire tale operazione")
            continue
        answer_user2()
        
# Request Number 3
    elif answer_user == "3":
        if not f.check_exist_file():
            print("Il file non esiste: impossibile eseguire tale operazione")
            continue
        answer_user3()
          
    else:
        print("Stai per uscire, Arrivederci")
        answer_user_continue=False