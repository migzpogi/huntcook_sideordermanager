class Recipes():
    def __init__(self):
        self.master_recipe = {
            'Rabbit Cider Soup': {
                'subrecipe': {'id': 1, 'value': 'Cider'},
                'time': 100
            },
            'Ayu Sushi': {
                'subrecipe': {'id': 0, 'value': ''},
                'time': 200
            }
        }

    def get_cooking_time(self, recipe):
        return self.master_recipe[recipe]['time']


class Orders():
    def get_recipes(self):
        recipes = [
            'Pheasant Ramen',
            'Raven Stew',
            'Raven Meat Pie',
            'Rabbit Cider Soup'
        ]
        return recipes

    def print_recipe_list(self):
        for idx, recipe in enumerate(self.get_recipes()):
            print idx+1, recipe

    def create_order(self):
        order = []
        recipe_count = int(raw_input('How many recipes in this order?: '))
        for x in range(0, recipe_count):
            print '-'*10
            self.print_recipe_list()
            choice = int(raw_input('Choose recipe: '))
            order.append(self.get_recipes()[choice-1])

        return order


if __name__ == '__main__':
    # x = Orders()
    # print x.create_order()
    x = Recipes()
    print x.get_cooking_time('Ayu Sushi')