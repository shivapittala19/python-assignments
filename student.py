
import json

with open('demo.json','r') as fh:
    json_str=fh.read()

    json_value=s=json.loads(json_str)


d=json_value

#show details in aplphabetical order
def alphaorder(arg):
    for key,value in sorted(arg.items()):
        print(key,value)

#Giving ranks to students based on total marks

def rank(arg):
    i=1
    for key,value in sorted(arg.items(),key=lambda x:x[1]['maths']+x[1]['physics']+x[1]['chemistry'],reverse=True):
        print("Rank of {}:{} is {}".format(key,value,i))
        i+=1

#length of the dictinoary
def length(arg):
    count=0
    for i in arg.items():
        count+=1
    return count

#Averag marks of student in each subject
def avgmarks(arg):
    maths_marks,physics_marks,chemistry_marks=0,0,0
    for i in dict(arg.items()):
        maths_marks+=arg[i]['maths']
        physics_marks+=arg[i]['physics']
        chemistry_marks+=arg[i]['chemistry']
    len_dict=length(arg)
    
    avg_maths,avg_physics,avg_chemistry=maths_marks/len_dict,physics_marks/len_dict,chemistry_marks/len_dict
    total_marks=maths_marks+physics_marks+chemistry_marks

    avg_total_marks=round(total_marks/3,2)
   
    print("Average marks in maths : {}".format(round(avg_maths,2)))
    print("Average marks in physics : {}".format(round(avg_physics,2)))
    print("Average marks in chemistry : {}".format(round(avg_chemistry,2)))
   
    print("avg marks",avg_total_marks)
    # students how scored above avg marks
    def above_avg(para):
        for key,value in para.items():
           
            if (para[key]['maths']+para[key]['physics']+para[key]['chemistry'])>avg_total_marks:
                print(key,value)

    # Show students who scored 10% above/below average (total) marks
    def above_below_avg(para):
        for key,value in para.items():
            sum1=para[key]['maths']+para[key]['physics']+para[key]['chemistry']
            if sum1>(11*avg_total_marks)/10 or sum1<(9*avg_total_marks)/10 :
                print(key,value)
    #Show students who scored above average scores in maths but below average in physics
    def above_avg_maths_below_avg_physics(para):
        for key,value in para.items():
            if para[key]['maths']>avg_maths and para[key]['physics']<avg_physics:
                print(key,value)
    #Number of students who scored above average in all subjects
    def above_avg_mpc(para):
        for key,value in para.items():
            if para[key]['maths']>avg_maths and para[key]['physics']>avg_physics and para[key]['chemistry']>avg_chemistry:
                print(key,value)
        


    #above_avg(arg)
    #above_below_avg(arg)
    #above_avg_maths_below_avg_physics(arg)
    above_avg_mpc(arg)


#ask user to take input subject and sort student based on marks sscored in that subject
def subject(arg):
    print("Sorting based on the subject:")
    print("1:for maths,2 for physcics and 3 for chemistry:")
    ch=int(input())
    while True:
        if ch==1:
            for key,value in sorted(arg.items(),key=lambda x:x[1]['maths'],reverse=True):
                print(key,value)

            break
        elif ch==2:
            for key,value in sorted(arg.items(),key=lambda x:x[1]['physics'],reverse=True):
                print(key,value)
            break
        elif ch==3:
            for key,value in sorted(arg.items(),key=lambda x:x[1]['chemistry'],reverse=True):
                print(key,value)
            break
        else:
            print("select the correct entry:")


    

#alphaorder(d)
#rank(d)
avgmarks(d)
#subject(d)
   