import requests
import json,os

def function(user):
    user_id = b["availableCourses"][user-1]["id"]
    api2="https://saral.navgurukul.org/api/courses/"+str(user_id)+"/exercises"
    data=requests.get(api2)
#     convert_data=data.json()
    print(convert_data)
    with open("exercise.json","w")as fp:
        json.dump(convert_data,fp,indent=4)
    my_data=convert_data["data"]
    i=0
    while i<len(my_data):
        print(i+1,my_data[i]["name"])
        child = my_data[i]["childExercises"]
        slug = my_data[i]["slug"]
        if child ==[]:
            print("   ",slug)
        else:
            j=0
            while j<len(child):
                print("  ",str(i+1)+'.'+str(j+1),child[j]["name"])
                j+=1
        i+=1
    return my_data

def function_2(my_data):
    print("********Welcome in parent page**********")
    user1=int(input("Enter parent: "))
    user1 = user1-1
    print(my_data[user1]["name"])
    slug = my_data[user1]["slug"]
    if my_data[user1]["childExercises"]==[]:
        print(slug)
        slug_api = requests.get("https://saral.navgurukul.org/api/courses/"+str(user)+"/exercise/getBySlug?slug="+my_data[user1]["slug"])
        slug_data = slug_api.json()
        with open("slug_id.json","w") as f:
            json.dump(slug_data,f,indent=4)
        slug_input = input("Do you want slug (yes or no):").lower()
        if slug_input=="yes":
            print(slug_data["content"])
    else:
        i=0
        while i<len(my_data[user1]["childExercises"]):
            print('   '+str(i+1),my_data[user1]["childExercises"][i]["name"])
            i+=1
        print("**********Welcome in child page**********")
        child_input = int(input("Enter the question number: "))
        child_api = requests.get("https://saral.navgurukul.org/api/courses/"+str(user)+"/exercise/getBySlug?slug="+my_data[user1]["childExercises"][child_input-1]["slug"])
        child_data = child_api.json()
        with open("child_id.json","w") as f:
            json.dump(child_data,f,indent=4)
        print(child_data)

if not(os.path.exists("saral_course.json")):
    print("not exists")
    api="http://saral.navgurukul.org/api/courses"
    a=requests.get(api)
    b=a.json()
    with open("saral_course.json","w")as f:
        f.write(json.dumps(b,indent=4))
        f.close()
else:
    print("yes exists")
    with open('saral_course.json','r') as file:
        b=json.load(file)
        data=(b["availableCourses"])
    count=1
    for i in range(0,len(data)):
        course_name=data[i]["name"]
        course_id=data[i]["id"]
        print(count,course_name,course_id)
        count+=1
    print("**********Welcome in course page**********")
    user=int(input("Enter id number: "))
    c=function(user)
    function_2(c)
    while 1:
        print("1: (Up Navigation)\n2: (Previous Navigation)\n3: (Eixt)")
        x=input("Enter what you want to do: ")
        if x=="1":
            c=function(user)
            function_2(c)
        elif x=="2":
            function_2(c)
        else:
            print("Eixt")
            break
