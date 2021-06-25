<?php
ini_set('display_errors', 'stderr');
define("PARAMETER_ERROR", 10);
define("INTERNAL_ERROR", 11);
define("ERR_OFILE_OUT", 12);
define("HEADER_ERROR", 21);
define("OPCODE_ERROR", 22);
define("LEX_SYN_ERROR", 23);

$header = '<?xml version="1.0" encoding="UTF-8"?><program></program>';
$xml = new SimpleXMLElement($header);
$xml->addAttribute('language', 'IPPcode21');

## Zoznam instrukcii

$instructions = [
    "MOVE" => [["var"], ["symb"]],
    "CREATEFRAME" => [],
    "PUSHFRAME" => [],
    "POPFRAME" => [],
    "DEFVAR" => [["var"]],
    "CALL" => [["label"]],
    "RETURN" => [],
    "PUSHS" => [["symb"]],
    "POPS" => [["var"]],
    "ADD" => [["var"], ["symb"], ["symb"]],
    "SUB" => [["var"], ["symb"], ["symb"]],
    "MUL" => [["var"], ["symb"], ["symb"]],
    "IDIV" => [["var"], ["symb"], ["symb"]],
    "LT" => [["var"], ["symb"], ["symb"]],
    "GT" => [["var"], ["symb"], ["symb"]],
    "EQ" => [["var"], ["symb"], ["symb"]],
    "AND" => [["var"], ["symb"], ["symb"]],
    "OR" => [["var"], ["symb"], ["symb"]],
    "NOT" => [["var"], ["symb"], ["symb"]],
    "INT2CHAR" => [["var"], ["symb"]],
    "STRI2INT" => [["var"], ["symb"], ["symb"]],
    "READ" => [["var"], ["type"]],
    "WRITE" => [["symb"]],
    "CONCAT" => [["var"], ["symb"], ["symb"]],
    "STRLEN" => [["var"], ["symb"]],
    "GETCHAR" => [["var"], ["symb"], ["symb"]],
    "SETCHAR" => [["var"], ["symb"], ["symb"]],
    "TYPE" => [["var"], ["symb"]],
    "LABEL" => [["label"]],
    "JUMP" => [["label"]],
    "JUMPIFEQ" => [["label"], ["symb"], ["symb"]],
    "JUMPIFNEQ" => [["label"], ["symb"], ["symb"]],
    "EXIT" => [["symb"]],
    "DPRINT" => [["symb"]],
    "BREAK" => []
];

#funkcia vypise napovedu
function print_help(){
	echo "Skript načte ze standardního vstupu zdrojový kód v IPP-code21, zkontroluje lexikální a syntaktickou správnost kódu a vypíše na standardní výstup XML reprezentaci programu dle specifikace v sekci\n";
}

#funkcia skontroluje validnost argumentu typu var a v pripade ze je validny tak to zapise do XML
#vracia 1 ak je argument validny, inak vracia 0
function check_var($opcode, $instruction, $arg_no){
    if(preg_match("/^(LF|GF|TF)@[_\-$&%*!?A-Ža-ž][_\-$&%*!?A-Ža-ž0-9]+$/", $instruction)) {
        $arg = $opcode->addChild('arg'.$arg_no, $instruction);
        $arg->addAttribute('type', 'var');
        return 1;
    }
    else{
        return 0;
    }
}

#funkcia skontroluje validnost argumentu typu symb a v pripade ze je validny tak to zapise do XML
#vracia 1 ak je argument validny, inak vracia 0
function check_symb($opcode, $instruction, $arg_no){
    if(preg_match("/^int@([+-]?\d*)$/", $instruction)){
        $arg = $opcode->addChild('arg'.$arg_no, substr($instruction, 4));
        $arg->addAttribute('type', 'int');
        return 1;
    }
    elseif(preg_match("/^string@(([^\s\#\\\\]|\\\\[0-9]{3})*$)/", $instruction)){
        $arg = $opcode->addChild('arg'.$arg_no, substr($instruction, 7));
        $arg->addAttribute('type', 'string');
        return 1;
    }
    elseif(preg_match("/^bool@(true|false)$/", $instruction)){
        $arg = $opcode->AddChild('arg'.$arg_no, substr($instruction, 5));
        $arg->addAttribute('type', 'bool');
        return 1;
    }
    elseif(preg_match("/^nil@nil$/", $instruction)){
        $arg = $opcode->addChild('arg'.$arg_no, 'nil');
        $arg->addAttribute('type', 'nil');
        return 1;
    }
    elseif(preg_match("/^(LF|GF|TF)@[_\-$&%*!?A-Ža-ž][_\-$&%*!?A-Ža-ž0-9]+$/", $instruction)) {
        $arg = $opcode->addChild('arg'.$arg_no, $instruction);
        $arg->addAttribute('type', 'var');
        return 1;
    }
    else{
        return 0;
    }
}

#funkcia skontroluje validnost argumentu typu type a v pripade ze je validny tak to zapise do XML
#vracia 1 ak je argument validny, inak vracia 0
function check_type($opcode, $instruction, $arg_no){
    if(preg_match("/^int|string|bool$/", $instruction)) {
        $arg = $opcode->addChild('arg'.$arg_no, $instruction);
        $arg->addAttribute('type', 'type');
        return 1;
    }
    else{
        return 0;
    }
}

#funkcia skontroluje validnost argumentu typu symb a v pripade ze je validny tak to zapise do XML
#vracia 1 ak je argument validny, inak vracia 0
function check_label($opcode, $instruction, $arg_no){
    if(preg_match("/^([a-zA-Z0-9_\-\$&%\*!?]+)$/", $instruction)) {
        $arg = $opcode->addChild('arg'.$arg_no, $instruction);
        $arg->addAttribute('type', 'label');
        return 1;
    }
    else{
        return 0;
    }
}

## TELO PROGRAMU

#kontrola argumentu --help, ak argument neni validny vracia sa PATAMETER ERROR
if ($argc == 2){
    if ($argv[1] == "--help"){
        print_help();
        exit(0);
    }
    else {
        exit(PARAMETER_ERROR);
    }
}
elseif ($argc > 2){
    exit(PARAMETER_ERROR);
}

#kontrola hlavicky, ak hlavicka chyba alebo je nespravna vracia sa HEADER ERROR
$line=trim(fgets(STDIN));
if(!preg_match("/^\.ippcode21$/", strtolower($line))){
    exit(HEADER_ERROR);
}


$counter =1; #pomocna premenna na pocet instrukcii

#nacitavanie riadkov zo standardneho vstupu
while($line=fgets(STDIN)){
    #ignorovanie prazdnych riadkov
	if($line == "\n"){
		continue;
	}
    #odstranenie komentarov
	$line=preg_replace("/#.*/","",$line);

    #instrukciu a argumenty oddelene medzerou naplnime do pola
	$line=trim($line);
	$instruction=explode(' ', $line);

	if($instruction[0]==""){
        continue;
    }

    #kontrola validity instrukcie
	if(!array_key_exists(strtoupper($instruction[0]), $instructions)){
		exit(OPCODE_ERROR);
	}

    #kontrola poctu argumentov
	if(count($instruction)-1 != count($instructions[strtoupper($instruction[0])])){
		exit(LEX_SYN_ERROR);
	}

    #zapisanie instrukcie do XML dokumentu
    $opcode = $xml->addChild('instruction');
    $opcode->addAttribute('order', $GLOBALS["counter"]++);
    $opcode->addAttribute('opcode', strtoupper($instruction[0]));
    $arg = $instructions[strtoupper($instruction[0])];
    
    #kontrola validity argumentov
    if(count($instruction) - 1 >= 1) {
        for ($i = 1; $i < count($instruction); $i++) {
            $check = 0;
            foreach ($arg[$i-1] as $arg_item) {
                switch ($arg_item) {
                    case "var":
                        $check = check_var($opcode, $instruction[$i], $i);
                        break;
                    case "symb":
                        $check = check_symb($opcode, $instruction[$i], $i);
                        break;
                    case "type":
                        $check = check_type($opcode, $instruction[$i], $i);
                        break;
                    case "label":
                        $check = check_label($opcode, $instruction[$i], $i);
                        break;
                    default:
                        exit(LEX_SYN_ERROR);
                }
            }
        }
        if ($check == 0) {
            exit(LEX_SYN_ERROR);
        }
    }
}
#vypisanie XML na standardny vystu[]
echo $xml->asXML();
?>