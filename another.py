import random as rd
import time
import msvcrt

wallet = float(input("Enter amount to add into wallet: "))

if wallet <= 0:
    print("Please add amount")
else:
    # Function to check if a key is pressed
    def is_key_pressed():
        return msvcrt.kbhit()
    
    while True:
        print("-------STAKE---------")
        bet = float(input("Enter bet: "))

        if bet > wallet:
            print("Bet isn't sufficient")
        else:
            multiplier = [1, 10, 100, 1000, 10000]
            chances = [30, 55, 19, 0.99, 0.01]

            choice = rd.random()

            total = choice * (rd.choices(multiplier, chances)[0])
            if total < 1:
                total = 1
            else:
                total = round(total, 2)

            auto_cashout = float(input("Auto cashout at: "))
            print("Press 'c' to cashout")
            print("Game will start in 5 seconds")
            time.sleep(5)

            start = 1.00
            cashed = False
            while start <= total:
                print(f"{start:.2f}")
                time.sleep(0.01)
                if is_key_pressed():
                    key = msvcrt.getch().decode()
                    if key.lower() == 'c':
                        cashout_amount = bet * start
                        cashed = True
                        print(f"Cashed out at {start:.2f}. Added {cashout_amount:.2f} to wallet.")
                        wallet += cashout_amount
                        break
                
                if(start>=auto_cashout):
                        cashout_amount = bet * start
                        cashed = True
                        print(f"Cashed out at {start:.2f}. Added {cashout_amount:.2f} to wallet.")
                        wallet += cashout_amount
                        break
                start += 0.01
            
            if cashed==False:
                wallet -= bet
            
            print(f"Crashed at {total:.2f}")

        print(f"Current wallet balance: {wallet:.2f}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Exiting game.")
            time.sleep(2)
            break

print("Thank you!")
