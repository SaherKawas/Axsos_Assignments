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

class Sensei extends Ninja{
    constructor(name){
        super(name, 200)
        this.speed = 10;
        this.strength = 10;
        this.wisdom = 10;

    }
    speakWisdom(){
        this.drinkSake();
        console.log("What one programmer can do in one month, two programmers can do in two months.");
    }

}


const peter= new Ninja("Peter",100);
peter.sayName()
peter.showStats()
peter.drinkSake()

const superSensei= new Sensei("Master Splinter");
superSensei.speakWisdom()
superSensei.showStats(); 
