import sqlite3
import random
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_related_nouns(adjective):
    """
    Finds nouns related to the given adjective from a local SQLite database.
    """
    try:
        # Attempt to connect to the database
        conn = sqlite3.connect('associations.db')
        cursor = conn.cursor()
        
        # Execute the query
        query = "SELECT noun FROM associations WHERE adjective=?"
        cursor.execute(query, (adjective,))
        nouns = cursor.fetchall()
        
        # Check if there are any results
        if not nouns:
            logging.warning(f"No nouns found related to '{adjective}'.")
            return []
        
        return [noun[0] for noun in nouns]
    
    except sqlite3.Error as e:
        # Handle potential errors in the database connection or query process
        logging.error(f"Error in database query: {e}")
        return []
    
    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()

def main():
    red_cards = ["Whales","Jail","NASA","Root Beer","Ben Stiller","Fast Food","Hangnails","Microsoft","Wrestling","Worms","Cookies","Rooms","alien abductions","youtube","my 21st birthday","bonfire","gang members",
                 "dark alleys","my bank account","the electric chair","bounty hunters","the sound of music","commuting","a bikini","homeless shelters","leeches","electricity",
                 "hell","a riot","a locker room","flying monkeys","remote controls"]
    
    green_card = input("Please enter a Green Apple card (adjective): ")
    
    related_nouns = get_related_nouns(green_card)
    
    if related_nouns:
        chosen_noun = random.choice(related_nouns)
        print(f"The chosen noun for '{green_card}': {chosen_noun}")
    else:
        # If no related nouns are found, randomly select a fallback noun as an alternative
        fallback_noun = random.choice(red_cards)
        print(f"No direct related nouns found for '{green_card}', randomly selected a fallback noun: {fallback_noun}")

if __name__ == "__main__":
    main()
