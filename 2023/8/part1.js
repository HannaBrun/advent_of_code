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

    let currentNode = 'AAA';
    let currentInstruction = 0;
    while (currentNode != 'ZZZ') {
        let targetNode = nodes.filter(node => node.name == currentNode)[0];
        if (instructions[currentInstruction % instructions.length] == 'L') {
            currentNode = targetNode.left;
        } else {
            currentNode = targetNode.right;
        }
        currentInstruction++;
    }

    console.log(currentInstruction);
});