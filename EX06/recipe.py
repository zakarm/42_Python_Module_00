# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zmrabet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/04 16:49:04 by zmrabet           #+#    #+#              #
#    Updated: 2023/01/04 18:11:54 by zmrabet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys, os

coockbook = {
        'Sandwich' : 
        {
            'ingredients' : ["ham", "bread", "cheese", "tomatoes"],
            'meal' : "lunch",
            'prep_time' : 10,
        },
        
        'Cake' : 
        {
            'ingredients' : ["flour", "sugar", "eggs"],
            'meal' : "dessert",
            'prep_time' : 60,
        },
        
        'Salad' : 
        {
            'ingredients' : ["avocado", "arugula", "tomatoes", "spinach"],
            'meal' : "lunch",
            'prep_time' : 0,
        },
    }

# A function that print all recipe names. 
def print_all() :
    for i in coockbook :
        print(i)
        
# A function that takes a recipe name and print its details.
def print_recipe_details(recipe) :
    data = coockbook.get(recipe)
    print("Recipe for cake:")
    for key, value in data.items() :
        if (key == "ingredients"):
            print("\tIngredients list: " + str(value) + ".")
        elif (key == "meal"):
            print("\tTo be eaten for " + str(value) + ".")
        elif (key == "prep_time"):
            print("\tTakes " + str(value) + " minutes of cooking.")

# A function that takes a recipe name and delete it.
def delete_recipe(recipe) :
    del coockbook[recipe]

# A function that add a recipe from user input. You will need a name, a list of ingredient, a meal type and a preparation time.
def add_recipe() :
    rec = input("Enter a name:\n")
    ing = []
    print("Enter ingredients:")
    while (1) :
        tester = input()
        if (tester == ""):
            break
        ing.append(tester)
    meal = input("Enter a meal type:\n")
    prep = input("Enter a preparation time:\n")
    
    coockbook[rec] = {}
    coockbook[rec]['ingredients'] = ing
    coockbook[rec]['meal'] = meal
    coockbook[rec]['prep_time'] = prep

# main function
def main():
    
    #os.system('clear')
    print("Welcome to the Python Coockbook\nList of available option:\n", end='')
    print("\t1: Add a recipe")
    print("\t2: Delete a recipe")
    print("\t3: Print a recipe")
    print("\t4: Print the cookbook")
    print("\t5: Quit")
    
    while (1) :
        val = input("Please select an option:\n")
        if (val == '2' or val == '3') :
            recipe = input("Please enter a recipe name to get its details:\n")
        if (val == '1') :
            add_recipe()
        elif (val == '2') :
            delete_recipe(recipe)
        elif (val == '3') :
            print_recipe_details(recipe)
        elif (val == '4') :
            print_all()
        else :
            break;
        

    
if __name__ == "__main__" :
    main()