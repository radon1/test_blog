let john = {
    age: 10,
    rost: 5,
    name: "John",
    school: {
        math: 5,
        rus: 4,
    },
    friends : ["Petya", "Olya", "Vasya"],
    getName: function () {
        console.log(this.name)
    }
}

class Chaild {
    constructor() {
        this.rost = 5;
    }
}

class John extends Chaild {
    constructor() {
        super()
        this.age = 11;
        this.name = "John";
    }

    getName() {
        console.log(this.name)
    }
}

// let a = new John()
// console.log(a)

//console.log(john.getName())


let a = {
    news: [
        {
            title: "овет кота",
            text: "text 241534634",
            comments: [
                {
                    "user": "John",
                    "text": "test js",
                    "date": "2019-05-12"
                }
            ]
        },
        {
            title: "совет кота 2",
            text: "text 24",
            comments: [
                {
                    "user": "Ivan",
                    "text": "test js 2",
                    "date": "2019-05-11"
                }
            ]
        }
    ]
}