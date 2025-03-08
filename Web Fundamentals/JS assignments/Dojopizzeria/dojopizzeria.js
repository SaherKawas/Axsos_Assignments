
var pizza = {
    crustType: "deepdish",
    sauceType: "traditional",
    cheese: ["Mozzarella"],
    toppings: ["pepperoni", "sausage"],
};
console.log (pizza)

function pizzaOven (crustType, sauceType, cheese, toppings) {
    var pizza = {};
    pizza.crustType= crustType;
    pizza.sauceType= sauceType;
    pizza.cheese= cheese;
    pizza.toppings= toppings;
    return pizza;
};
var pizza1 = pizzaOven ("deep dish", "traditional", ["Mozzarella"],["pepperoni", "sausage"]);
console.log (pizza1);

var pizza2 = pizzaOven ("hand tossed", "marinara", ["Mozzarella", "feta"],["mushroom", "olives","onions"]);
console.log (pizza2);

var pizza3 = pizzaOven ("crusty","four seasons", ["cheddar", "feta"],["pepper", "olives","onions"]);
console.log (pizza3);

var pizza4 = pizzaOven ("deep dish", "pesto", ["feta", "goat cheese"], ["olives","onions"]);
console.log (pizza4);
