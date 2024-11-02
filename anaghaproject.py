import pickle
print("Welcome to  2 states app")


def Telangana():
    print("WELCOME TO TELANGANA")
    with open("C:/Users/yadav/OneDrive/Desktop/Telangana.txt", "r", encoding="utf-8", errors='replace') as file:
        content = file.read()
        print(content)

    
def Jharkhand():
    print("WELCOME TO JHARKHAND")
    file=open("C:/Users/yadav/AppData/Local/Programs/Python/Python310/jharkhand_info.pkl","rb")
    try:
        while True:
            content=pickle.load(file)
            print(content)
    except EOFError:
        file.close()
         
    

def Intro():
    c = '''Here’s a brief introduction to both Telangana and Jharkhand:

Telangana
Location: Telangana is located in the southern part of India and is bordered by Maharashtra to the north, Chhattisgarh to the east, and Andhra Pradesh to the south and west.

History: Telangana was formed as a separate state on June 2, 2014, following a prolonged movement for statehood. It was previously a part of the state of Andhra Pradesh. The demand for a separate state stemmed from cultural and economic disparities.

Culture: The culture of Telangana is rich and diverse, with influences from various historical periods, including the Kakatiya dynasty and the Nizams of Hyderabad. The state is known for its folk dances, music, and festivals like Bathukamma and Bonalu.

Economy: Telangana has a mixed economy, with agriculture, industry, and services playing vital roles. The state is known for its IT industry, particularly in Hyderabad, which is often referred to as "Cyberabad."

Language: Telugu is the official language, with Urdu also widely spoken, reflecting the cultural diversity of the region.

Jharkhand
Location: Jharkhand is situated in eastern India and shares borders with Bihar to the north, West Bengal to the east, Odisha to the south, and Chhattisgarh to the west.

History: Jharkhand was carved out of the state of Bihar on November 15, 2000, primarily to promote the interests of the tribal population and to address regional disparities in development.

Culture: The culture of Jharkhand is predominantly influenced by the indigenous tribes, with a rich tradition of music, dance, and handicrafts. Major festivals include Sarhul, Tana Jhulan, and Karma.

Economy: The economy of Jharkhand is resource-rich, with significant reserves of minerals such as coal, iron ore, and uranium. The state is a major contributor to India’s mineral production and has a growing industrial sector.

Language: Hindi is the official language, but several regional languages and dialects are spoken, including Santhali, Mundari, and Ho, reflecting the state's tribal diversity.

Both states have distinct identities, cultural heritage, and economic significance in India, contributing to the country's diversity and growth.'''
    print(c)



def mainn():
    a=int(input("Enter 1 to start/Rerun: "))
    if(a==1):
        print("1.Telangana")
        print("2.Jharkhand")
        print("3.Intro")
        print("4.EXIT")
    
        b=int(input("Select 1 for Telangana and 2 for Jharkhand 3 for Intro 4 for exit: "))
        if(b==1):
            Telangana()
        elif(b==2):
            Jharkhand()
        elif(b==3):
            Intro()
        else:
            print("exiting")
            return
        mainn()
        
    else:
        return 0
mainn()
    
