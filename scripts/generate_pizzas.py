categories = {
    'BASE TOMATE' : [
        {
            "nom" : 'Marguerita',
            "ingredients" : [
                'Tomate',
                'mozzarella'
            ],
            "prix" : 7.00
        },
        {
            "nom" : 'Reine',
            "ingredients" : [
                'Champignon',
                'jambon',
                'mozzarella'
            ],
            "prix" : 8.80
        },
        {
            "nom" : 'Bacon',
            "ingredients" : [
                'Bacon',
                'oeuf',
                'mozzarella'
            ],
            "prix" : 8.80
        },
        {
            "nom" : 'Royale',
            "ingredients" : [
                'Champignon',
                'jambon',
                'oeuf',
                'mozzarella'
            ],
            "prix" : 9.00
        },
        {
            "nom" : 'Légumes',
            "ingredients" : [
                'Champignon',
                'oignon',
                'poivron',
                'chèvre',
                'mozarella'
            ],
            "prix" : 9.90
        },
        {
            "nom" : 'Lannionaise',
            "ingredients" : [
                'Poivron',
                'oignon',
                'thon',
                'chèvre',
                'mozzarella'
            ],
            "prix" : 9.90
        },
        {
            "nom" : 'Bolognaise',
            "ingredients" : [
                'Bolognaise maison',
                'mozzarella'
            ],
            "prix" : 9.90
        },
        {
            "nom" : 'Tartiflette',
            "ingredients" : [
                'Pomme de terre',
                'oignon',
                'lardons',
                'raclette',
                'mozzarella'
            ],
            "prix" : 9.90
        },
        {
            "nom" : 'Italienne',
            "ingredients" : [
                'Jambon de pays',
                'parmesan',
                'mozzarella'
            ],
            "prix" : 9.90
        },
        {
            "nom" : 'Créole',
            "ingredients" : [
                'Jambon ou poulet',
                'ananas',
                'mozzarella'
            ],
            "prix" : 9.90
        },
        {
            "nom" : 'Saumon',
            "ingredients" : [
                'Saumon fumé',
                'crème fraiche',
                'mozzarella'
            ],
            "prix" : 9.90
        },
        {
            "nom" : 'Bretonne',
            "ingredients" : [
                'Pomme de terre',
                'champignon',
                'andouille',
                'mozzarella'
            ],
            "prix" : 9.90
        },
        {
            "nom" : 'Sardinette',
            "ingredients" : [
                'Sardines',
                'oignons',
                'mozzarella'
            ],
            "prix" : 9.90
        },
        {
            "nom" : 'Plouber',
            "ingredients" : [
                'Lardons',
                'chèvre',
                'mozzarella'
            ],
            "prix" : 9.90
        },
        {
            "nom" : 'Basquaise',
            "ingredients" : [
                'Poulet',
                'oignon',
                'poivrons',
                'mozzarella'
            ],
            "prix" : 9.90
        },
        {
            "nom" : 'Poulet',
            "ingredients" : [
                'Pomme de terre',
                'oignon',
                'poulet',
                'mozzarella'
            ],
            "prix" : 9.90
        },
        {
            "nom" : 'Orientale',
            "ingredients" : [
                'Oignon',
                'poivron',
                'merguez',
                'chorizo',
                'oeuf',
                'mozzarella'
            ],
            "prix" : 9.90
        },
        {
            "nom" : 'Mexicaine',
            "ingredients" : [
                'Poivron',
                'haricots rouges',
                'viande hachée',
                'mozzarella'
            ],
            "prix" : 9.90
        },
        {
            "nom" : '3 Fromages',
            "ingredients" : [
                'Chèvre',
                'bleu',
                'brie',
                'raclette',
                'ou parmesan ...au choix'
            ],
            "prix" : 8.50
        },
        {
            "nom" : '4 Fromages',
            "ingredients" : [
                'Chèvre',
                'bleu',
                'brie',
                'raclette',
                'ou parmesan ...au choix'
            ],
            "prix" : 9.50
        }
    ],
    'BASE CRÈME' : [
        {
            "nom" : 'Dijonnaise',
            "ingredients" : [
                'Crème moutardée',
                'poulet',
                'champignon',
                'poivron',
                'origan',
                'mozarella'
            ],
            "prix" : 9.90
        },
        {
            "nom" : 'Braiz\'Pizza',
            "ingredients" : [
                'Pomme de terre',
                'poulet ou saumon',
                'raclette',
                'mozzarella'
            ],
            "prix" : 9.90
        },
        {
            "nom" : 'Braiz\'Curry',
            "ingredients" : [
                'Crème curry',
                'poivron',
                'champignon',
                'poulet',
                'mozzarella'
            ],
            "prix" : 9.90
        },
        {
            "nom" : 'Alsacienne',
            "ingredients" : [
                'Lardons fumés',
                'oignon',
                'mozzarella'
            ],
            "prix" : 9.90
        },
        {
            "nom" : 'Miel\'Pizza',
            "ingredients" : [
                'Chèvre',
                'miel',
                'jambon ou poulet',
                'mozzarella'
            ],
            "prix" : 9.90
        },
        {
            "nom" : 'Braiz\'Fines Herbes',
            "ingredients" : [
                'Thon',
                'oignons',
                'mozzarella',
                'fromage ail et fines herbes'
            ],
            "prix" : 9.90
        }
    ]
}

def generate_pizzas(outpath):
    string = ""
    for category, pizzas in categories.items():
        string += "<article>\n"
        string += "\t<h2>%s</h2>\n"%category
        string += '\t<table class="table table-pizza">\n'
        for pizza in pizzas:
            string += '\t\t<tr>\n'
            string += '\t\t\t<td pizza-name>%s</td>\n'%pizza['nom']
            string += '\t\t\t<td>%s</td>\n'%''.join(
                [ '<span class="ingr">%s</span>'%ingr for ingr in pizza['ingredients'] ]
            )
            string += '\t\t\t<td>%s€</td>\n'%("%.2f"% pizza['prix']).replace('.', ',')
            string += '\t\t\t<td><a onclick="addtocart(this)"><i class="fa fa-plus fa-sm"></i><i class="fa fa-clipboard-list"></i></a></td>'
            string += "\t\t</tr>\n"
        string += '\t</table>\n'
        string += "</article>\n"

    with open(outpath, 'w') as f:
        f.write(string)
