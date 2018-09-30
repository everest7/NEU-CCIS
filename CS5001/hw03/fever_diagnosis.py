def megigitis():
    print("Possibilities include megigitis")

def digestive_infection():
    print("Possibilities include digestive tract infection")

def pneumonia_infection():
    print("Possibilities include pneumonia or infection of airways")

def viral_infection():
    print("Possibilities include viral infection")

def throat_infection():
    print("Possibilities include throat infection")

def kidney_infection():
    print("Possibilities include kidney infection")

def urinary_infection():
    print("Possibilities include urinary tract infection")

def sunstroke_heat():
    print("Possibilities include sunstroke or heat exhaustion")

def insufficient_info():
    print("Insufficient information to list possibilities")

def aching_bones_joints():
    choice = input("Do you have aching bones or aching joints?(y/n)")
    if choice == 'y':
        viral_infection()
    else:
        choice = input("Do you have a rash?(y/n)")
        if choice == 'y':
            insufficient_info()
        else:
            choice = input("Do you have a sore throat?(y/n)")
            if choice == 'y':
                throat_infection()
            else:
                choice = input("Do you have back pain just above the waist with chills and fever?(y/n)")
                if choice == 'y':
                    kidney_infection()
                else:
                    choice = input("Do you have pain urinating or are urinating more often?(y/n)")
                    if choice == 'y':
                        urinary_infection()
                    else:
                        choice = input("Have you spent the day in the sun or in the conditions?(y/n)")
                        if choice == 'y':
                            sunstroke_heat()
                        else:
                            insufficient_info()    

   


choice = input("Are you coughing?(y/n)")
if choice == 'y':
    choice = input("Are you short of breath or wheezing or coughing up phlegm(y/n)")
    if choice == 'y':
        pneumonia_infection()
    else:
        choice = input("Do you have a headache?(y/n)")
        if choice == 'y':
            viral_infection()
        else:
            aching_bones_joints()
else:
    choice = input("Do you have a headache?(y/n)")
    if choice == 'y':
        choice = input("Are you experiencing any of the following:pain when bending your head forward, nausea or vomiting,\
        bright light hurting your eyes,drowsiness or confusion?(y/n)")
        if choice == 'y':
            megigitis()
        else:
            choice = input("Are you vomiting or had diarrhea?(y/n)")
            if choice == 'y':
                digestive_infection()
            else:
                aching_bones_joints()
    else:
        aching_bones_joints()


