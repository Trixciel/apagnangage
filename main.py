
# Parser pour les options de bash (-o -i --HEEEEEELP ...)
import os
import argparse

# Lexer et parser APAGNAN
from antlr4 import *
from APAGNANGAGELexer import APAGNANGAGELexer as Lexer
from APAGNANGAGEParser import APAGNANGAGEParser as Parser

import visitor

# Des trucs utiles
import useful as uf


if __name__ == '__main__':
    #################################################
    # Parsing des arguments de la ligne de commande #
    #################################################
    argument_parser = argparse.ArgumentParser(
        prog="Interpréteur de l'APAGNANGAGE",
        description="Interpète l'APAGNANGAGE",
        epilog="POV TU FAIT UN APAGNAN DANS L'INTERPRÉTEUR DE L'APAGNANGAGE (APAGNAAAAAAAAAAA)",
    )
    argument_parser.add_argument("filename")
    args = argument_parser.parse_args()
    input_file_name = args.filename
    
    input_stream = uf.readfile(input_file_name)
    
    
    double_check = input("Chemin complet du fichier d'entrée : ")
    check = os.popen("pwd").read().strip() + "/" + input_file_name
    if double_check != check:
        print("Le nom du fichier d'entrée et l'input ne correspondent pas !!!!! 👿🤬")
        exit(1)

    #################################################
    # Parsing du/des fichiers d'entrée              #
    #################################################
    lexer = Lexer(InputStream(input_stream))
    parser = Parser(CommonTokenStream(lexer))
    parse_tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        vinterp = visitor.Visitor()
        vinterp.visit(parse_tree)
