from game_data import data
import random
import art

def play():
    s_choice=random.choice(data)
    won=True
    count=0
    while won:
        f_choice=s_choice
        s_choice=random.choice(data)
        if f_choice==s_choice:
            s_choice=random.choice(data)
        f_name=f_choice["name"]
        f_description=f_choice["description"]
        f_country=f_choice["country"]
        f_followers=f_choice["follower_count"]
        s_name=s_choice["name"]
        s_description=s_choice["description"]
        s_country=s_choice["country"]
        s_followers=s_choice["follower_count"]
        print(f"Compare A: {f_name}, {f_description}, from {f_country}")
        print(art.versus)
        print(f"Compare B: {s_name}, {s_description}, from {s_country}")
        choice=input("Who has more followers? Type 'A' or 'B':").lower()
        if f_followers> s_followers and choice=="a":
            count+=1
            print(f"You're right! Your current Score: {count}")
        elif choice=="b" and s_followers>f_followers:
            count+=1
            print(f"You're right! Your current Score: {count}")
        else:
            won=False
            print("You lost!")
            print(f"Your total score: {count}")
            
play()    
            



