from zapis import write_to_file
from odczyt import read_and_display_file
import os

if __name__ == "__main__":
    
    user_input = input("Wprowadź tekst do zapisania do pliku: ")
    file = os.path.join(os.path.dirname(__file__) , 'data','temp.txt')
    
    #print(file)
    
    # zapis    asdklasdkasldkads
    write_to_file(file,user_input)
    
    # odczyt 
    read_and_display_file(file)
    
    