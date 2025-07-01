class Ninja{
    constructor(name, health){
        this.name=name;
        this.health=health;
        this.speed=3;
        this.strength=3;

    }
    sayName(){
        console.log(`hi my name is ${this.name}`)
    }
    showStats(){
        console.log(`Name: ${this.name}, Strength: ${this.strength}, Speed: ${this.speed}, Health: ${this.health}`)
    }
    drinkSake(){
        this.health+=10
        console.log(`Health: ${this.health}`)
    }

}
const peter= new Ninja("Peter",100);
peter.sayName()
peter.showStats()
peter.drinkSake()



