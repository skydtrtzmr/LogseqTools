from operator import contains
import os
import re
from queue import PriorityQueue
from turtle import title



def fileOperate(type,input_dir,output_dir):
     for root, dirs, files in os.walk(input_dir):
        for file in files:
            if '.md' in file:
                if(type=="task1"):
                    task1(file,root,output_dir)
                if(type=="task3"):
                  task3(file,root,output_dir)


def task1(file_name,input_dir,output_dir):

    if ("管综%2F数学%2F题库%2F真题" not in file_name) and ("管综%2F逻辑%2F题库%2F真题" not in file_name):
        return
    year_month = ""
    year_index=file_name.find("年")
    month_index=file_name.find("月")
    if year_index!=-1:
        if "经综" in file_name:
            year_month+="J"
        year_month+=file_name[year_index-4:year_index]
    if month_index!=-1:
        year_month+="."+file_name[month_index-2:month_index]
    # print(os.path.join(input_dir,file_name))
    # print(os.path.join(output_dir,file_name))
    with open(os.path.join(input_dir,file_name),'r',encoding='utf_8') as raw_file, \
    open(os.path.join(output_dir,file_name),'w',encoding='utf_8') as new_file:   
        list_block = []  
        for line in raw_file:
            if line[0]=='-':                
                if "::" in line:
                    line="  " +line.strip("- ")
                for new_line in list_block:
                    # print(new_line)
                    new_file.writelines(new_line)
                list_block=[]
            ret=re.match("^(\s\s[0-9]+(\.|．))",line)
            # print(ret)
            if ret!=None:
                list_block.insert(0,"- "+year_month+"-"+ret.group().strip()[0:-1].zfill(2)+"\n")
                # print(ret.group().strip()[0:-1].zfill(2))
            else:
                if "**【答案】**" in line:
                    list_block.append("  #card\n")
                if "#card" not in line:
                    list_block.append(line)
        for new_line in list_block:
            new_file.writelines(new_line)

def task3(file_name,input_dir,output_dir):
    begin=True
    propertys=["题型大类","知识点","技巧","难度","错因"]
    replace={"题型":"题型大类"}
   # propertys.sort(reverse=True)
    if ("管综%2F数学%2F题库%2F真题" not in file_name) and ("管综%2F逻辑%2F题库%2F真题" not in file_name):
        return
    with open(os.path.join(input_dir,file_name),'r',encoding='utf_8') as raw_file, \
    open(os.path.join(output_dir,file_name),'w',encoding='utf_8') as new_file:   
        list_block = []  
        map_property={}
        for line in raw_file:
            if line[0]=='-':
                if not begin:
                    for property in reversed(propertys):
                        if property in map_property:
                            list_block.insert(1,"  "+property+"::"+map_property[property]+'\n')
                        else:
                            list_block.insert(1,"  "+property+"::"+"\n")
                begin=False
                for new_line in list_block:
                    new_file.writelines(new_line)
                list_block=[]
                map_property={}
            ret=re.match("^(\s\s\w+::)",line)
            if ret!=None:
                index=line.strip().find("::")
                key=line.strip()[0:index]
                value=line.strip()[index+2:]
                if key=="tags":
                    continue
                #替换key
                if key in replace:
                    key=replace[key]
                if key in propertys:
                    map_property[key]=value
                    continue
                list_block.append("  "+key+"::"+value+"\n")        
            else:
                list_block.append(line)
        for new_line in list_block:
            new_file.writelines(new_line)
         
                  
# fileOperate("task1","D:\\★Ruru★\\MyNotes\\📐Maths\\pages","D:\\★Ruru★\\MyNotes\\📐Maths\\rawPages")

# fileOperate("task3","D:\\★Ruru★\\MyNotes\\📐Maths\\rawPages","D:\\★Ruru★\\MyNotes\\📐Maths\\pages")

fileOperate("task1","D:\\★Ruru★\\MyNotes\\🧿Logic\\pages","D:\\★Ruru★\\rawPages")

fileOperate("task3","D:\\★Ruru★\\rawPages","D:\\★Ruru★\\MyNotes\\🧿Logic\\pages")


