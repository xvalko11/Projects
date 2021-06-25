import re
import xml.etree.ElementTree as ET
import sys
import argparse

#chybove kody
class err_code:
    WRONG_PARAMETER = 10
    INPUT_FILE_ERROR = 11
    OUTPUT_FILE_ERROR =12
    WRONG_XML = 31
    XML_SYN_LEX = 32
    SEMANTIC_ERROR = 52
    WRONG_OPERAND_TYPE = 53
    NON_EXISTENT_VAR = 54
    NON_EXISTENT_FRAME = 55
    MISSING_VALUE = 56
    WRONG_OPERAND_VALUE = 57
    STRING_ERROR = 58

#trieda predstavuje premennu ulozenu v ramci
class Variable:
    def __init__(self,name,frame,type_of_var,value):
        self.name=name
        self.type_of_var=type_of_var
        self.value=value
        self.frame=frame #iba pri pridavani novej premennej

#trieda predstavuje ramce - globalny, docasny a lokalny
#obsahuje funkcie na pracu s ramcami a ich premennymi
class Frame:
    def __init__(self):
        self.stack=[]
        self.GF={}
        self.TF=None
        self.LF=None

    def createframe(self):
        self.TF={}

    def pushframe(self):
        if(self.TF is None):
            sys.exit(err_code.NON_EXISTENT_FRAME)
        else:
            self.stack.append(self.TF)
            self.LF=self.TF
            self.TF=None
    
    #funkcia presimoe vrcholovy ramec LF zo zasobniku stack do TF
    def popframe(self):
        if(self.LF is None):
            sys.exit(err_code.NON_EXISTENT_FRAME)
        self.TF=self.LF
        self.stack.pop()
        if(len(self.stack)!=0):
            self.LF=self.stack.pop()
            self.stack.append(self.LF)
        else:
            self.LF=None

    #funkcia overi ci dany ramec existuje
    def exists(self,name):
        if(name == 'LF'):
            if(self.LF is None):
                sys.exit(err_code.NON_EXISTENT_FRAME)
        elif(name == 'TF'):
            if(self.TF is None):
                sys.exit(err_code.NON_EXISTENT_FRAME)
        elif(name == 'GF'):
            if(self.GF is None):
                sys.exit(err_code.NON_EXISTENT_FRAME)
        else:
            sys.exit(32)
    
    #funkcia skontroluje ci uz dana var na danom frame neexistuje a ak nie tak ju tam prida
    def add_var(self,variable):
        if(variable.frame == 'LF'):
            if(variable.name in self.LF):
                sys.exit(err_code.SEMANTIC_ERROR)
            else:
                self.LF[variable.name]=variable
        elif(variable.frame == 'TF'):
            if(variable.name in self.TF):
                sys.exit(err_code.SEMANTIC_ERROR)
            else:
                self.TF[variable.name]=variable
        elif(variable.frame == 'GF'):
            if(variable.name in self.GF):
                sys.exit(err_code.SEMANTIC_ERROR)
            else:
                self.GF[variable.name]=variable
    
    #funkcia skontroluje ci zadana premena target_var_name v ramci frame existuje a ak ano priradi jej hodnotu variable
    def update_var(self,target_var_name,frame,variable):
        if(frame == 'LF'):
            if not(target_var_name in self.LF):
                sys.exit(err_code.NON_EXISTENT_VAR)
            else:
                self.LF[target_var_name]=variable
        elif(frame == 'TF'):
            if not(target_var_name in self.TF):
                sys.exit(err_code.NON_EXISTENT_VAR)
            else:
                self.TF[target_var_name]=variable
        elif(frame == 'GF'):
            if not(target_var_name in self.GF):
                sys.exit(err_code.NON_EXISTENT_VAR)
            else:
                self.GF[target_var_name]=variable
    
    #funkcia vracia premennu variable z daneho ramca frame ak existuje
    def get_var(self,frame,name):
        if(frame == 'LF'):
            if not(name in self.LF):
                sys.exit(err_code.NON_EXISTENT_VAR)
            else:
                variable=self.LF[name]          
        elif(frame == 'TF'):
            if not(name in self.TF):
                sys.exit(err_code.NON_EXISTENT_VAR)
            else:
                variable=self.TF[name]
        elif(frame == 'GF'):
            if not(name in self.GF):
                sys.exit(err_code.NON_EXISTENT_VAR)
            else:
                variable=self.GF[name]
        return variable
                



#trieda predstavuje label
class Label:
    def __init__(self, name, order):
        self.name=name
        self.order=order

#trieda predstavuje argument instrukcie
class Argument:
    def __init__(self, type_of_arg, value,arg_order):
        self.type_of_arg=type_of_arg
        self.value=value
        self.arg_order=arg_order

#trieda predstavuje instrukciu a obsahuje list jej argumentov
class Instruction:
    def __init__(self ,order, opcode):
        self.order=order
        self.opcode=opcode
        self.arguments=[]
    
    #funkcia sluzi na pridavanie argumentov
    def add_argument(self, type_of_arg, value,arg_order):
        if(type_of_arg=='string') and value is None:
            self.arguments.append(Argument(type_of_arg, '', arg_order))
        else:
            self.arguments.append(Argument(type_of_arg, value, arg_order))

#funkcia sluzi na spracovanie argumentov scriptu
def parse_args():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument('--input', type=argparse.FileType('r'))
    parser.add_argument('--source', type=str)
    args = parser.parse_args()
    if args.source and args.input:
        try:
            input_src=args.input
        except IOError: #nepodarilo sa otvorit subor
            sys.exit(err_code.INPUT_FILE_ERROR)
        return args.source, input_src
    elif args.source:
        return args.source,None
    elif args.input:
        try:
            input_src=args.input
        except IOError: #nepodarilo sa otvorit subor
            sys.exit(err_code.INPUT_FILE_ERROR)
        return sys.stdin, input_src
    else:
        sys.exit(err_code.WRONG_PARAMETER)

#funkcia skontroluje spravnost poctu argumentov
def check_nof_args(arguments):
    if(len(arguments) == 3):          #unikatne poradie argumentov
        if(arguments[0].arg_order == arguments[1].arg_order) or (arguments[0].arg_order == arguments[2].arg_order) or (arguments[1].arg_order == arguments[2].arg_order):
            sys.exit(err_code.XML_SYN_LEX)
    if(len(arguments) == 2):          #unikatne poradie argumentov a pripadny chybajuci argument 
        if(arguments[0].arg_order == 2) or (arguments[0].arg_order == 3) :
            sys.exit(err_code.XML_SYN_LEX)
        if(arguments[0].arg_order == arguments[1].arg_order):
            sys.exit(err_code.XML_SYN_LEX)
    if(len(arguments) == 1):          #namiesto arg1 pride arg2 alebo arg3 
        if(arguments[0].arg_order == 2) or (arguments[0].arg_order == 3):
            sys.exit(err_code.XML_SYN_LEX)

def regex_type(value):
    if(re.match(r'^int|string|bool$',str(value)) is None):
        sys.exit(err_code.XML_SYN_LEX)

def regex_label(value):
    if(re.match(r'^([A-Ža-ž0-9_\-\$&%\*!?]+)$',str(value)) is None):
        sys.exit(err_code.XML_SYN_LEX)

def regex_var(value):
    if(re.match(r'^(LF|GF|TF)@[_\-$&%*!?A-Ža-ž][_\-$&%*!?A-Ža-ž0-9]*$',str(value)) is None):
        sys.exit(err_code.XML_SYN_LEX)

def regex_symb(value,expected_type):
    if(expected_type == 'var'):
        regex_var(value)
    elif(expected_type == 'string'):
        if(re.match(r'^(([^\s\#\\\\]|\\[0-9]{3})*$)',str(value)) is None):
            sys.exit(err_code.XML_SYN_LEX)
    elif(expected_type == 'bool'):
        if(re.match(r'^(true|false)$',str(value)) is None):
            sys.exit(err_code.XML_SYN_LEX)
    elif(expected_type == 'nil'):
        if(re.match(r'^nil$',str(value)) is None):
            sys.exit(err_code.XML_SYN_LEX)
    elif(expected_type == 'int'):
        if(re.match(r'^([+-]?\d*)$',str(value)) is None):
            sys.exit(err_code.XML_SYN_LEX)
        try:
            int(value)
        except Exception:
            sys.exit(err_code.XML_SYN_LEX)
    else:
        sys.exit(err_code.XML_SYN_LEX)

#funkcia skontroluje spravny pocet a spravne typy argumentov
def check_instruction(instruction):
    check_nof_args(instruction.arguments)
    if(instruction.opcode in ['CREATEFRAME','PUSHFRAME','POPFRAME','RETURN','BREAK']): # ziadny argument
        if(len(instruction.arguments)>0):
            sys.exit(err_code.XML_SYN_LEX)
    elif(instruction.opcode in ['DEFVAR','POPS']): #var
        if(len(instruction.arguments)!=1):
            sys.exit(err_code.XML_SYN_LEX)
        if(instruction.arguments[0].type_of_arg != 'var'):
            sys.exit(err_code.WRONG_OPERAND_TYPE)
        regex_var(instruction.arguments[0].value)
    elif(instruction.opcode in ['CALL','LABEL','JUMP']): #label
        if(len(instruction.arguments)!=1):
            sys.exit(err_code.XML_SYN_LEX)
        if(instruction.arguments[0].type_of_arg != 'label'):
            sys.exit(err_code.WRONG_OPERAND_TYPE)
        regex_label(instruction.arguments[0].value)
    elif(instruction.opcode in ['PUSHS','WRITE','EXIT','DPRINT']): #symb
        if(len(instruction.arguments)!=1):
            sys.exit(err_code.XML_SYN_LEX)
        regex_symb(instruction.arguments[0].value,instruction.arguments[0].type_of_arg)
    elif(instruction.opcode in ['MOVE','INT2CHAR','STRLEN','TYPE']): #var symb
        if(len(instruction.arguments)!=2):
            sys.exit(err_code.XML_SYN_LEX)
        if(instruction.arguments[0].type_of_arg != 'var'):
            sys.exit(err_code.WRONG_OPERAND_TYPE)
        regex_var(instruction.arguments[0].value)
        regex_symb(instruction.arguments[1].value,instruction.arguments[1].type_of_arg)
    elif(instruction.opcode == 'NOT'): # VAR BOOL
        if(len(instruction.arguments)!=2):
            sys.exit(err_code.XML_SYN_LEX)
        if(instruction.arguments[0].type_of_arg != 'var'):
            sys.exit(err_code.WRONG_OPERAND_TYPE)
        regex_var(instruction.arguments[0].value)
        if(instruction.arguments[1].type_of_arg not in ['bool','var']):
            sys.exit(err_code.WRONG_OPERAND_TYPE)
        regex_symb(instruction.arguments[1].value,instruction.arguments[1].type_of_arg)
    elif(instruction.opcode == 'READ'): #var type
        if(len(instruction.arguments)!=2):
            sys.exit(err_code.XML_SYN_LEX)
        if(instruction.arguments[0].type_of_arg != 'var'):
            sys.exit(err_code.WRONG_OPERAND_TYPE)
        regex_var(instruction.arguments[0].value)
        if(instruction.arguments[1].type_of_arg != 'type'):
            sys.exit(err_code.WRONG_OPERAND_TYPE)
        regex_type(instruction.arguments[1].value)
    elif(instruction.opcode in ['ADD','SUB','MUL','IDIV']): #var int int
        if(len(instruction.arguments)!=3):
            sys.exit(err_code.XML_SYN_LEX)
        if(instruction.arguments[0].type_of_arg != 'var'):
            sys.exit(err_code.WRONG_OPERAND_TYPE)
        regex_var(instruction.arguments[0].value)
        if(instruction.arguments[1].type_of_arg not in ['int','var']):
            sys.exit(err_code.WRONG_OPERAND_TYPE)
        if(instruction.arguments[2].type_of_arg not in ['int','var']):
            sys.exit(err_code.WRONG_OPERAND_TYPE)
        regex_symb(instruction.arguments[1].value,instruction.arguments[1].type_of_arg)
        regex_symb(instruction.arguments[2].value,instruction.arguments[2].type_of_arg)
    elif(instruction.opcode in ['LT','GT','EQ','STRI2INT','CONCAT','GETCHAR','SETCHAR']): #var symb symb
        if(len(instruction.arguments)!=3):
            sys.exit(err_code.XML_SYN_LEX)
        if(instruction.arguments[0].type_of_arg != 'var'):
            sys.exit(err_code.WRONG_OPERAND_TYPE)
        regex_var(instruction.arguments[0].value)
        regex_symb(instruction.arguments[1].value,instruction.arguments[1].type_of_arg)
        regex_symb(instruction.arguments[2].value,instruction.arguments[2].type_of_arg)  
    elif(instruction.opcode in ['AND','OR']): #var symb symb - symb iba bool
        if(len(instruction.arguments)!=3):
            sys.exit(err_code.XML_SYN_LEX)
        if(instruction.arguments[0].type_of_arg != 'var'):
            sys.exit(err_code.WRONG_OPERAND_TYPE)
        if(instruction.arguments[1].type_of_arg not in ['bool','var']):
            sys.exit(err_code.WRONG_OPERAND_TYPE)
        if(instruction.arguments[2].type_of_arg not in ['bool','var']):
            sys.exit(err_code.WRONG_OPERAND_TYPE)
        regex_symb(instruction.arguments[1].value,instruction.arguments[1].type_of_arg)
        regex_symb(instruction.arguments[2].value,instruction.arguments[2].type_of_arg)
    elif(instruction.opcode in ['JUMPIFEQ','JUMPIFNEQ']): #label symb symb
        if(len(instruction.arguments)!=3):
            sys.exit(err_code.XML_SYN_LEX)
        if(instruction.arguments[0].type_of_arg != 'label'):
            sys.exit(err_code.WRONG_OPERAND_TYPE)
        regex_symb(instruction.arguments[1].value,instruction.arguments[1].type_of_arg)
        regex_symb(instruction.arguments[2].value,instruction.arguments[2].type_of_arg)  
    else:
        sys.exit(err_code.XML_SYN_LEX)

#funkcia overuje spravnost a parsuje XML source
#funkcia vracia zaplneny list objektov Instruction 
def parse_xml(xml_source):
    try:
        xml=ET.parse(xml_source)
    except IOError:
        sys.exit(err_code.INPUT_FILE_ERROR)
    except ET.ParseError:
        sys.exit(err_code.WRONG_XML)
    root=xml.getroot()
    if(root.tag != "program"):  #check na element program
        sys.exit(err_code.XML_SYN_LEX)
    if('language' not in root.attrib):
        sys.exit(err_code.XML_SYN_LEX)
    if(root.attrib['language'].upper() != 'IPPCODE21'):  #check na spravny atribut language
        sys.exit(err_code.XML_SYN_LEX)

    instruction_list=[]
    label_list=[]
    tmp_order_list=[]
    tmp_label_name_list=[]
    for instruction in root:
        if(instruction.tag != "instruction"): #nespravny tag
            sys.exit(err_code.XML_SYN_LEX)
        if(len(instruction.attrib) != 2): #neobsahuje opcode alebo order
            sys.exit(err_code.XML_SYN_LEX)
        if(re.match(r'^[1-9][0-9]*$',instruction.attrib['order']) is None): #order je zaporny alebo 0
            sys.exit(err_code.XML_SYN_LEX)
        if(int(instruction.attrib['order']) in tmp_order_list): #order sa nesmie opakovat
            sys.exit(err_code.XML_SYN_LEX)
        instruction_list.append(Instruction(instruction.attrib['order'],instruction.attrib['opcode'].upper()))
        tmp_order_list.append(int(instruction.attrib['order']))
        for program_args in instruction:
            if(program_args.tag=='arg1'):
                instruction_list[-1].add_argument(program_args.attrib['type'],program_args.text,1)
            elif(program_args.tag=='arg2'):
                instruction_list[-1].add_argument(program_args.attrib['type'],program_args.text,2)
            elif(program_args.tag=='arg3'):
                instruction_list[-1].add_argument(program_args.attrib['type'],program_args.text,3)
            else:
                sys.exit(err_code.XML_SYN_LEX)
        instruction_list[-1].arguments.sort(key=lambda x: x.arg_order) #zoradenie argumentov podla arg_order
        check_instruction(instruction_list[-1])
        if(instruction.attrib['opcode'].upper() == 'LABEL'): #odchytavanie labelov
            if(instruction_list[-1].arguments[0].value in tmp_label_name_list):
                sys.exit(err_code.SEMANTIC_ERROR)
            tmp_label_name_list.append(instruction_list[-1].arguments[0].value)
            label_list.append(Label(instruction_list[-1].arguments[0].value,len(instruction_list)-1))
    instruction_list.sort(key=lambda x: int(x.order)) #zoradenie instrukcii podla order

    return instruction_list,label_list

#funkcia pre instrukcie ADD, SUB, MUL, IDIV
def arithmetic_fnc(instruction):
    var_to_update=instruction.arguments[0].value.split("@")
    frame.exists(var[0])
    x1=0
    x2=0
    if(instruction.arguments[1].type_of_arg == 'var'):
        var_1=instruction.arguments[1].value.split("@")
        x1=frame.get_var(var_1[0],var_1[1])
        if(x1.type_of_var=='int'):
            x1=x1.value
        else:
            sys.exit(err_code.WRONG_OPERAND_TYPE)
    else:
        x1=int(instruction.arguments[1].value)
    if(instruction.arguments[2].type_of_arg == 'var'):
        var_2=instruction.arguments[2].value.split("@")
        x2=frame.get_var(var_2[0],var_2[1])
        if(x2.type_of_var=='int'):
            x2=x2.value
        else:
            sys.exit(err_code.WRONG_OPERAND_TYPE)
    else:
        x2=int(instruction.arguments[2].value)
    if(instruction.opcode == 'ADD'):
        result=int(x1)+int(x2)
    if(instruction.opcode == 'SUB'):
        result=int(x1)-int(x2)
    if(instruction.opcode == 'MUL'):
        result=int(x1)*int(x2)
    if(instruction.opcode == 'IDIV'):
        if(int(x2)==0):
            sys.exit(err_code.WRONG_OPERAND_VALUE)
        result=int(x1)//int(x2)
    frame.update_var(var_to_update[1],var_to_update[0],Variable(name=var_to_update[1],frame=var_to_update[0],type_of_var='int',value=result))

#funkcia pre instrukcie LT a GT
def lt_gt_fnc(instruction):
    var=instruction.arguments[0].value.split('@')
    frame.exists(var[0])
    x1=0
    x2=0
    if(instruction.arguments[1].type_of_arg == 'var'):
        var_1=instruction.arguments[1].value.split("@")
        x1=frame.get_var(var_1[0],var_1[1])
        if(x1.type_of_var=='nil'):
            sys.exit(err_code.WRONG_OPERAND_TYPE)
    else:
        x1=Variable(name=None,frame=None,value=instruction.arguments[1].value,type_of_var=instruction.arguments[1].type_of_arg)
        if(x1.type_of_var=='nil'):
            sys.exit(err_code.WRONG_OPERAND_TYPE)

    if(instruction.arguments[2].type_of_arg == 'var'):
        var_2=instruction.arguments[2].value.split("@")
        x2=frame.get_var(var_2[0],var_2[1])
        if(x2.type_of_var=='nil'):
            sys.exit(err_code.WRONG_OPERAND_TYPE)
    else:
        x2=Variable(name=None,frame=None,value=instruction.arguments[2].value,type_of_var=instruction.arguments[2].type_of_arg)
        if(x2.type_of_var=='nil'):
            sys.exit(err_code.WRONG_OPERAND_TYPE)
    if(x1.type_of_var != x2.type_of_var):
        sys.exit(err_code.WRONG_OPERAND_TYPE)
    if(x1.type_of_var == 'int'):
        x1=int(x1.value)
        x2=int(x2.value)
    else:
        x1=x1.value
        x2=x2.value
    if(instruction.opcode=='LT'):
        if(x1<x2):
            frame.update_var(var[1],var[0],Variable(var[1],var[0],'bool','true'))
        else:
            frame.update_var(var[1],var[0],Variable(var[1],var[0],'bool','false'))
    elif(instruction.opcode=='GT'):
        if(x1>x2):
            frame.update_var(var[1],var[0],Variable(var[1],var[0],'bool','true'))
        else:
            frame.update_var(var[1],var[0],Variable(var[1],var[0],'bool','false'))

#funkcia pre instrukciu EQ
def eq_fnc(instruction):
    var=instruction.arguments[0].value.split('@')
    frame.exists(var[0])
    x1=0
    x2=0
    if(instruction.arguments[1].type_of_arg == 'var'):
        var_1=instruction.arguments[1].value.split("@")
        x1=frame.get_var(var_1[0],var_1[1])
    else:
        x1=Variable(name=None,frame=None,value=instruction.arguments[1].value,type_of_var=instruction.arguments[1].type_of_arg)

    if(instruction.arguments[2].type_of_arg == 'var'):
        var_2=instruction.arguments[2].value.split("@")
        x2=frame.get_var(var_2[0],var_2[1])
    else:
        x2=Variable(name=None,frame=None,value=instruction.arguments[2].value,type_of_var=instruction.arguments[2].type_of_arg)

    if(x1.type_of_var != x2.type_of_var):
        if(x1.type_of_var == 'nil') or (x2.type_of_var == 'nil'):
            frame.update_var(var[1],var[0],Variable(var[1],var[0],'bool','false'))
        else:
            sys.exit(err_code.WRONG_OPERAND_TYPE)
    else:
        if(x1.type_of_var == 'int'):
            x1=int(x1.value)
            x2=int(x2.value)
        else:
            x1=x1.value
            x2=x2.value
        if(x1==x2):
            frame.update_var(var[1],var[0],Variable(var[1],var[0],'bool','true'))
        else:
            frame.update_var(var[1],var[0],Variable(var[1],var[0],'bool','false'))

#funkcia pre instrukcie AND a OR
def logic_fnc(instruction):
    var=instruction.arguments[0].value.split('@')
    frame.exists(var[0])
    if(instruction.arguments[1].type_of_arg == 'var'):
        var_1=instruction.arguments[1].value.split("@")
        x1=frame.get_var(var_1[0],var_1[1])
    else:
        x1=Variable(name=None,frame=None,value=instruction.arguments[1].value,type_of_var=instruction.arguments[1].type_of_arg)

    if(instruction.arguments[2].type_of_arg == 'var'):
        var_2=instruction.arguments[2].value.split("@")
        x2=frame.get_var(var_2[0],var_2[1])
    else:
        x2=Variable(name=None,frame=None,value=instruction.arguments[2].value,type_of_var=instruction.arguments[2].type_of_arg)
    
    if(x1.type_of_var != 'bool') or (x2.type_of_var != 'bool'):
        sys.exit(err_code.WRONG_OPERAND_TYPE)
    else:
        if(instruction.opcode == 'AND'):
            if(x1.value == 'true') and (x2.value == 'true'):
                frame.update_var(var[1],var[0],Variable(var[1],var[0],'bool','true'))
            else:
                frame.update_var(var[1],var[0],Variable(var[1],var[0],'bool','false'))
        elif(instruction.opcode == 'OR'):
            if(x1.value == 'true') or (x2.value == 'true'):
                frame.update_var(var[1],var[0],Variable(var[1],var[0],'bool','true'))
            else:
                frame.update_var(var[1],var[0],Variable(var[1],var[0],'bool','false'))

#funkcia pre instrukciu NOT
def not_fnc(instruction):
    var=instruction.arguments[0].value.split('@')
    frame.exists(var[0])
    if(instruction.arguments[1].type_of_arg == 'var'):
        var_1=instruction.arguments[1].value.split("@")
        x1=frame.get_var(var_1[0],var_1[1])
    else:
        x1=Variable(name=None,frame=None,value=instruction.arguments[1].value,type_of_var=instruction.arguments[1].type_of_arg)
    
    if(x1.type_of_var != 'bool'):
        sys.exit(err_code.WRONG_OPERAND_TYPE)
    else:
        if(x1.value == 'true'):
            frame.update_var(var[1],var[0],Variable(var[1],var[0],'bool','false'))
        else:
            frame.update_var(var[1],var[0],Variable(var[1],var[0],'bool','true'))

#funkcia pre instrukciu int2char
def int2char_fnc(instruction):
    var=instruction.arguments[0].value.split('@')
    frame.exists(var[0])
    if(instruction.arguments[1].type_of_arg == 'var'):
        var_1=instruction.arguments[1].value.split("@")
        x1=frame.get_var(var_1[0],var_1[1])
    else:
        x1=Variable(name=None,frame=None,value=instruction.arguments[1].value,type_of_var=instruction.arguments[1].type_of_arg)
    try:
        result=chr(int(x1.value))
    except Exception:
        sys.exit(err_code.STRING_ERROR)
    frame.update_var(var[1],var[0],Variable(var[1],var[0],'string',result))

#funkcia pre instrukciu STRI2INT
def stri2int_fnc(instruction):
    var=instruction.arguments[0].value.split('@')
    frame.exists(var[0])
    if(instruction.arguments[1].type_of_arg == 'var'):
        var_1=instruction.arguments[1].value.split("@")
        x1=frame.get_var(var_1[0],var_1[1])
    else:
        x1=Variable(name=None,frame=None,value=instruction.arguments[1].value,type_of_var=instruction.arguments[1].type_of_arg)
    if(instruction.arguments[2].type_of_arg == 'var'):
        var_2=instruction.arguments[2].value.split("@")
        x2=frame.get_var(var_2[0],var_2[1])
    else:
        x2=Variable(name=None,frame=None,value=instruction.arguments[2].value,type_of_var=instruction.arguments[2].type_of_arg)
    if(x1.type_of_var != 'string') or (x2.type_of_var !='int'):
        sys.exit(err_code.WRONG_OPERAND_TYPE)
    try:
        result=ord(x1.value[x2.value])
    except Exception:
        sys.exit(err_code.STRING_ERROR)
    frame.update_var(var[1],var[0],Variable(var[1],var[0],'int',result))

#funkcia pre instrukciu CONCAT
def concat_fnc(instruction):
    var=instruction.arguments[0].value.split('@')
    frame.exists(var[0])
    if(instruction.arguments[1].type_of_arg == 'var'):
        var_1=instruction.arguments[1].value.split("@")
        x1=frame.get_var(var_1[0],var_1[1])
    else:
        x1=Variable(name=None,frame=None,value=instruction.arguments[1].value,type_of_var=instruction.arguments[1].type_of_arg)
    if(instruction.arguments[2].type_of_arg == 'var'):
        var_2=instruction.arguments[2].value.split("@")
        x2=frame.get_var(var_2[0],var_2[1])
    else:
        x2=Variable(name=None,frame=None,value=instruction.arguments[2].value,type_of_var=instruction.arguments[2].type_of_arg)
    if(x1.type_of_var != 'string') or (x2.type_of_var !='string'):
        sys.exit(err_code.WRONG_OPERAND_TYPE)
    result=x1.value + x2.value
    frame.update_var(var[1],var[0],Variable(var[1],var[0],'string',result))

#funkcia pre instrukciu STRLEN
def strlen_fnc(instruction):
    var=instruction.arguments[0].value.split('@')
    frame.exists(var[0])
    if(instruction.arguments[1].type_of_arg == 'var'):
        var_1=instruction.arguments[1].value.split("@")
        x1=frame.get_var(var_1[0],var_1[1])
    else:
        x1=Variable(name=None,frame=None,value=instruction.arguments[1].value,type_of_var=instruction.arguments[1].type_of_arg)

    if(x1.type_of_var != 'string'):
        sys.exit(err_code.WRONG_OPERAND_TYPE) 
    result=len(x1.value)
    frame.update_var(var[1],var[0],Variable(var[1],var[0],'int',result))

#instrukcia READ
def read_fnc(instruction,input_src):
    var=instruction.arguments[0].value.split('@')
    frame.exists(var[0])
    type_of_var=instruction.arguments[1].value
    if(input_src is None):
        try:
            x1=input()
        except Exception:
            type_of_var='nil'
    else:
        try:
            x1=input_src.readline()
        except Exception:
            type_of_var='nil'

    if(type_of_var == 'nil'):
        x1='nil'
    elif(type_of_var == 'int'):
        try:
            x1=int(x1)
        except Exception:
            x1='nil'
            type_of_var='nil'
    elif(type_of_var=='bool'):
        try:
            if(x1.lower() == 'true'):
                x1='true'
            else:
                x1='false'
        except Exception:
            x1='nil'
            type_of_var='nil'
    frame.update_var(var[1],var[0],Variable(var[1],var[0],type_of_var,x1))

#instrukcia WRITE 
def write_fnc(instruction):
    if(instruction.arguments[0].type_of_arg == 'var'):
        var=instruction.arguments[0].value.split("@")
        frame.exists(var[0])
        x1=frame.get_var(var[0],var[1])
    else:
        x1=Variable(name=None,frame=None,value=instruction.arguments[0].value,type_of_var=instruction.arguments[0].type_of_arg)

    if(x1.type_of_var == 'nil'):
        print('', end='')
    elif(x1.type_of_var =='bool'):
        if(x1.value == 'true') or (x1.value == 'false'):
            print(x1.value,end='')
        else:
            sys.exit(err_code.WRONG_OPERAND_VALUE)
    elif(x1.type_of_var == 'int'):
        try:
            print(int(x1.value),end='')
        except Exception:
            sys.exit(err_code.WRONG_OPERAND_VALUE)
    elif(x1.type_of_var == 'string'):
        try:
            x1.value=re.sub(r'\\(\d{3})',lambda x:chr(int(x[1])), x1.value)
        except Exception:
            sys.exit(err_code.WRONG_OPERAND_VALUE)
        print(x1.value,end='')

#instrukcia GETCHAR
def getchar_fnc(instruction):
    var=instruction.arguments[0].value.split('@')
    frame.exists(var[0])
    if(instruction.arguments[1].type_of_arg == 'var'):
        var_1=instruction.arguments[1].value.split("@")
        x1=frame.get_var(var_1[0],var_1[1])
    else:
        x1=Variable(name=None,frame=None,value=instruction.arguments[1].value,type_of_var=instruction.arguments[1].type_of_arg)
    if(instruction.arguments[2].type_of_arg == 'var'):
        var_2=instruction.arguments[2].value.split("@")
        x2=frame.get_var(var_2[0],var_2[1])
    else:
        x2=Variable(name=None,frame=None,value=instruction.arguments[2].value,type_of_var=instruction.arguments[2].type_of_arg)
    if(x1.type_of_var != 'string') or (x2.type_of_var !='int'):
        sys.exit(err_code.WRONG_OPERAND_TYPE)
    try:
        result=x1.value[x2.value]
    except Exception:
        sys.exit(err_code.STRING_ERROR)
    frame.update_var(var[1],var[0],Variable(var[1],var[0],'string',result))

#instrukcia SETCHAR
def setchar_fnc(instruction):
    var=instruction.arguments[0].value.split('@')
    frame.exists(var[0])
    var=frame.get_var(var[0],var[1])
    if(var.type_of_var != 'string'):
        sys.exit(err_code.WRONG_OPERAND_TYPE)
    if(instruction.arguments[1].type_of_arg == 'var'):
        var_1=instruction.arguments[1].value.split("@")
        x1=frame.get_var(var_1[0],var_1[1])
    else:
        x1=Variable(name=None,frame=None,value=instruction.arguments[1].value,type_of_var=instruction.arguments[1].type_of_arg)
    if(instruction.arguments[2].type_of_arg == 'var'):
        var_2=instruction.arguments[2].value.split("@")
        x2=frame.get_var(var_2[0],var_2[1])
    else:
        x2=Variable(name=None,frame=None,value=instruction.arguments[2].value,type_of_var=instruction.arguments[2].type_of_arg)
    if(x1.type_of_var != 'int') or (x2.type_of_var !='string'):
        sys.exit(err_code.WRONG_OPERAND_TYPE)
    try:
        var.value[x1.value]=x2.value[0]
    except Exception:
        sys.exit(err_code.STRING_ERROR)
    frame.update_var(var.name,var.frame,var)

#instrukcia TYPE
def type_fnc(instruction):
    var=instruction.arguments[0].value.split('@')
    frame.exists(var[0])
    if(instruction.arguments[1].type_of_arg == 'var'):
        var_1=instruction.arguments[1].value.split("@")
        x1=frame.get_var(var_1[0],var_1[1])
    else:
        x1=Variable(name=None,frame=None,value=instruction.arguments[1].value,type_of_var=instruction.arguments[1].type_of_arg)
    if(x1.type_of_var in ['int','string','bool','nil']):
        frame.update_var(var[1],var[0],Variable(var[1],var[0],'string',x1.type_of_var))
    elif(x1.type_of_var is None):
        frame.update_var(var[1],var[0],Variable(var[1],var[0],'string',''))

#instrukcia JUMPIFEQ
def jumpifeq_fnc(instruction,label_list):
    if(instruction.arguments[1].type_of_arg == 'var'):
        var_1=instruction.arguments[1].value.split("@")
        x1=frame.get_var(var_1[0],var_1[1])
    else:
        x1=Variable(name=None,frame=None,value=instruction.arguments[1].value,type_of_var=instruction.arguments[1].type_of_arg)

    if(instruction.arguments[2].type_of_arg == 'var'):
        var_2=instruction.arguments[2].value.split("@")
        x2=frame.get_var(var_2[0],var_2[1])
    else:
        x2=Variable(name=None,frame=None,value=instruction.arguments[2].value,type_of_var=instruction.arguments[2].type_of_arg)

    if(x1.type_of_var != x2.type_of_var):
        if(x1.type_of_var == 'nil') or (x2.type_of_var == 'nil'):
            pass
        else:
            sys.exit(err_code.WRONG_OPERAND_TYPE)
    else:
        if(x1.type_of_var == 'int'):
            x1=int(x1.value)
            x2=int(x2.value)
        else:
            x1=x1.value
            x2=x2.value
        if(x1==x2):
            index=jump_fnc(instruction,label_list)
            return index

#instrukcia JUMPIFNEQ
def jumpif_N_eq_fnc(instruction,label_list):
    if(instruction.arguments[1].type_of_arg == 'var'):
        var_1=instruction.arguments[1].value.split("@")
        x1=frame.get_var(var_1[0],var_1[1])
    else:
        x1=Variable(name=None,frame=None,value=instruction.arguments[1].value,type_of_var=instruction.arguments[1].type_of_arg)

    if(instruction.arguments[2].type_of_arg == 'var'):
        var_2=instruction.arguments[2].value.split("@")
        x2=frame.get_var(var_2[0],var_2[1])
    else:
        x2=Variable(name=None,frame=None,value=instruction.arguments[2].value,type_of_var=instruction.arguments[2].type_of_arg)

    if(x1.type_of_var != x2.type_of_var):
        if(x1.type_of_var == 'nil') or (x2.type_of_var == 'nil'):
            index=jump_fnc(instruction,label_list)
            return index
        else:
            sys.exit(err_code.WRONG_OPERAND_TYPE)
    else:
        if(x1.type_of_var == 'int'):
            x1=int(x1.value)
            x2=int(x2.value)
        else:
            x1=x1.value
            x2=x2.value
        if(x1!=x2):
            index=jump_fnc(instruction,label_list)
            return index

#instrukcia JUMP
def jump_fnc(instruction,label_list):
    if(instruction.arguments[0].type_of_arg != 'label'):
        sys.exit(err_code.WRONG_OPERAND_TYPE)
    for label in label_list:
        if(instruction.arguments[0].value == label.name):
            return label.order
    sys.exit(err_code.SEMANTIC_ERROR)

#instrukcia EXIT
def exit_fnc(instruction):
    if(instruction.arguments[0].type_of_arg == 'var'):
        var_1=instruction.arguments[0].value.split("@")
        x1=frame.get_var(var_1[0],var_1[1])
    else:
        x1=Variable(name=None,frame=None,value=instruction.arguments[0].value,type_of_var=instruction.arguments[0].type_of_arg)
    if(x1.type_of_var != 'int'):
        sys.exit(err_code.WRONG_OPERAND_TYPE)
    try:
        x1=int(x1.value)
    except Exception:
        sys.exit(err_code.WRONG_OPERAND_VALUE)
    if(x1>=0) and (x1<=49):
        sys.exit(x1)
    else:
        sys.exit(err_code.WRONG_OPERAND_VALUE)

#RIADIACA CAST PROGRAMU
################################################################

xml_source,input_src = parse_args()
instruction_list, label_list = parse_xml(xml_source)
frame=Frame()
call_stack=[]
data_stack=[]
i=0 #riadiaca premenna predstavuje index vykonavanej instrukcie
while(i<len(instruction_list)):
    if(instruction_list[i].opcode=='CREATEFRAME'):
        frame.createframe()

    elif(instruction_list[i].opcode=='PUSHFRAME'):
        frame.pushframe()
    
    elif(instruction_list[i].opcode=='POPFRAME'):
        frame.popframe()
    
    elif(instruction_list[i].opcode=='DEFVAR'): #var[0] je frame var[1] je nazov premennej
        var=instruction_list[i].arguments[0].value.split('@')
        variable=Variable(var[1],var[0],None,None)
        frame.exists(variable.frame)
        frame.add_var(variable)
    
    elif(instruction_list[i].opcode=='MOVE'): 
        var_target=instruction_list[i].arguments[0].value.split('@')
        if(instruction_list[i].arguments[1].type_of_arg == 'var'):
            var_src=instruction_list[i].arguments[1].value.split('@')
            frame.exists(var_src[0])
            variable=frame.get_var(var_src[0],var_src[1])
            frame.update_var(var_target[1],var_target[0],variable)
        else:
            variable=Variable(var_target[1],var_target[0],instruction_list[i].arguments[1].type_of_arg,instruction_list[i].arguments[1].value)
            frame.exists(variable.frame)
            frame.update_var(variable.name,variable.frame,variable)
    
    elif(instruction_list[i].opcode=='LABEL'):
        pass
    
    elif(instruction_list[i].opcode=='CALL'):
        found=False
        for label in label_list:
            if(instruction_list[i].arguments[0].value == label.name):
                call_stack.append(i)
                i=label.order
                found=True
        if not(found):
            sys.exit(err_code.SEMANTIC_ERROR)
    
    elif(instruction_list[i].opcode=='RETURN'):
        if(len(call_stack)==0):
            sys.exit(err_code.MISSING_VALUE)
        else:
            i=call_stack.pop()+1
    
    elif(instruction_list[i].opcode=='JUMP'):
        i=jump_fnc(instruction_list[i],label_list)
    
    elif(instruction_list[i].opcode=='PUSHS'):
        if(instruction_list[i].arguments[0].type_of_arg == 'var'):
            var=instruction_list[i].arguments[0].value.split('@')
            frame.exists(var[0])
            variable_to_add=frame.get_var(var[0],var[1])
            if(variable_to_add.type_of_var == None):
                sys.exit(err_code.MISSING_VALUE)
            else:
                data_stack.append(variable_to_add)
        else:
            data_stack.append(Variable(name=None,frame=None,type_of_var=instruction_list[i].arguments[0].type_of_arg,value=instruction_list[i].arguments[0].value))
    
    elif(instruction_list[i].opcode=='POPS'):
        if(len(data_stack)!= 0):
            var_src=data_stack.pop()
            var_target=instruction_list[i].arguments[0].value.split('@')
            frame.exists(var_target[0])
            frame.update_var(var_target[1],var_target[0],var_src)
        else:
            sys.exit(err_code.MISSING_VALUE)
    
    elif(instruction_list[i].opcode in ['ADD','SUB','MUL','IDIV']):
        arithmetic_fnc(instruction_list[i])

    elif(instruction_list[i].opcode in ['LT','GT']):
        lt_gt_fnc(instruction_list[i])

    elif(instruction_list[i].opcode == 'EQ'):
        eq_fnc(instruction_list[i])
    
    elif(instruction_list[i].opcode in ['AND','OR']):
        logic_fnc(instruction_list[i])
    
    elif(instruction_list[i].opcode == 'NOT'):
        not_fnc(instruction_list[i])
    
    elif(instruction_list[i].opcode == 'INT2CHAR'):
        int2char_fnc(instruction_list[i])

    elif(instruction_list[i].opcode == 'STRI2INT'):
        stri2int_fnc(instruction_list[i])

    elif(instruction_list[i].opcode == 'CONCAT'):
        concat_fnc(instruction_list[i])

    elif(instruction_list[i].opcode == 'STRLEN'):
        strlen_fnc(instruction_list[i])
    
    elif(instruction_list[i].opcode == 'GETCHAR'):
        getchar_fnc(instruction_list[i])

    elif(instruction_list[i].opcode == 'SETCHAR'):
        setchar_fnc(instruction_list[i])

    elif(instruction_list[i].opcode == 'TYPE'):
        type_fnc(instruction_list[i])

    elif(instruction_list[i].opcode == 'JUMPIFEQ'):
        jump_index=jumpifeq_fnc(instruction_list[i],label_list)
        if(jump_index is not None):
            i=jump_index

    elif(instruction_list[i].opcode == 'JUMPIFNEQ'):
        jump_index=jumpif_N_eq_fnc(instruction_list[i],label_list)
        if(jump_index is not None):
            i=jump_index
    
    elif(instruction_list[i].opcode == 'EXIT'):
        exit_fnc(instruction_list[i])

    elif(instruction_list[i].opcode == 'WRITE'):
        write_fnc(instruction_list[i])

    elif(instruction_list[i].opcode =='READ'):
        read_fnc(instruction_list[i],input_src)
        
    elif(instruction_list[i].opcode == 'DPRINT'):
        print('VALUE OF SYMB :',file=sys.stderr)

    elif(instruction_list[i].opcode == 'BREAK'):
        print('STATE OF INTERPRETER :',file=sys.stderr)
    
    i+=1
    