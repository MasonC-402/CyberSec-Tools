# Written by Mason Clemons - Takes input of topics and training material links from the internet and parses them into a json file for easy retrieval from other scripts that will be useful in the future

# Python 3.11 with tkinter and the python json library as the only dependencies
# imports duh
import tkinter as tk 
import json 

# This function grabs the topic and link from input and saves it to memory:
     def save_to_json(): 
    topic = topicInput.get() 
    link = linkInput.get()


    # Simple data structure for the json file to hold the training topic and the internet or file link to be held in this json file for future recall     
    data = {
            'topic': topic, 
            'link': link 
        } 

    # keeps and checks that the json file is open and dumps/writes the data into the next available line    
    with open('data.json', 'a') as file: 
        json.dump(data, file)
        file.write('\n') 


    # these two statements delete the previous input data from variables meant to hold the original input
    topicInput.delete(0, tk.END) 
    linkInput.delete(0, tk.END) 
    
root **of**= tk.Tk() 
root.title("Data Entry") root.geometry("300x150") topic_label = tk.Label(root, text="Topic:") topic_label.pack() topic_entry = tk.Entry(root)

