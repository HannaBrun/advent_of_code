const fs = require('fs');

let nodes = [];
let instructions = [];

class Node {
    constructor(name, left, right) {
        this.name = name;
        this.left = left;
        this.right = right;
    }
}

fs.readFile('8/network.txt', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }

    data.split('\n').forEach(line => {
        if (line.endsWith(')')) {
            let name = line.substring(0, 3);
            let left = line.substring(7, 10);
            let right = line.substring(12, 15);
            nodes.push(new Node(name, left, right))
        } else if (line == '') {
            
        } else {
            for (let i = 0; i < line.length; i++) {
                instructions.push(line.charAt(i));
            }
        }
    });

    let currentNodes = nodes.filter(node => node.name.endsWith('A'));
    let iterationsRequired = [];
    let nbrOfTargetsLeft = currentNodes.length;
    let currentInstruction = 0;
    while (nbrOfTargetsLeft > 0) {
        if (instructions[currentInstruction % instructions.length] == 'L') {
            currentNodes = nodes.filter(node => currentNodes.map(el => el.left).includes(node.name));
        } else {
            currentNodes = nodes.filter(node => currentNodes.map(el => el.right).includes(node.name));
        }

        currentInstruction++;

        currentNodes = currentNodes.filter(node => !node.name.endsWith('Z'));
        if (currentNodes.length < nbrOfTargetsLeft) {
            iterationsRequired.push(currentInstruction);
            nbrOfTargetsLeft--;
        }
    }
    let prodSum = iterationsRequired.reduce((acc, val) => acc * val, 1);
    let longestTime = iterationsRequired[iterationsRequired.length-1];

    for (i = longestTime; i < prodSum; i += longestTime) {
        if (iterationsRequired.every(el => i % el == 0)) {
            console.log(i);
            break;
        }
    }
});