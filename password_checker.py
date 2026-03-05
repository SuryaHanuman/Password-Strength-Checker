import getpass,string,math
def load_passwds():
    print("Loading database... please wait.")
    try:
        with open("common.txt","r",encoding="latin-1") as f:
            return {line.strip() for line in f}
    except Exception as e:
        print("error: ",e)
        return set()

Leaked_passwords=load_passwds()
def is_leaked(password) -> bool:
    return password in Leaked_passwords

#to check the password whether it is leaked or not
def is_weak(password: str):
    score=0
    if len(password)>=8:
        score+=1
    score+= 1 if any(c in string.ascii_uppercase for c in password) else 0
    score+=1 if any(c in string.ascii_lowercase for c in password) else 0
    score+=1 if any(c in string.digits for c in password) else 0
    score+=1 if any(c in string.punctuation for c in password) else 0
    if score>=4:
        return "strong"
    elif score==3:
        return "moderate"
    else:
        return "weak"
    
#----antropy-----
def cal_entropy(password):
    if not password: return 0
    score=0
    if any(c in string.ascii_uppercase for c in password):
        score+= 26 
    if any(c in string.ascii_lowercase for c in password): 
        score+= 26
    if any(c in string.digits for c in password):
        score+=10 
    if any(c in string.punctuation for c in password):
        score+=32  
    if score == 0:
        return 0
    entropy = len(password) * math.log2(score)
    return round(entropy,2)

#---time calculation-----
def cal_time(entropy):
    guess_per_second=1_000_000_000
    combinations = 2 ** entropy
    seconds = combinations / guess_per_second
    if seconds < 60:
        return "Instantly crackable"
    elif seconds < 3600:
        return f"{round(seconds/60,2)} minutes"
    elif seconds < 86400:
        return f"{round(seconds/3600,2) } hours"
    elif seconds < 31536000:
        return f"{round(seconds/86400,2)} days"
    else:
        return f"{round(seconds/31536000,2)} years"

#--main logic--
print("Make sure your password contains:")
print("- At least 8 characters")
print("- Upper and lower case letters")
print("- Digits and special characters")
while True:

    password = getpass.getpass("Enter password (or type 'exit' to quit): ")

    if password.lower() == "exit":
        print("Exiting...")
        break

    if len(password) < 8:
        print("Password can't be less than 8 characters")

    elif is_leaked(password):
        print("This password is already leaked")

    else:
        strength = is_weak(password)
        entropy = cal_entropy(password)
        time = cal_time(entropy)

        print("Strength:", strength)
        print("Entropy:", entropy)
        print("Estimated time to crack:", time)

    print("--------")