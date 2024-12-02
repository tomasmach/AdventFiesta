const fs = require("fs");

fs.open('test_input.txt', 'r', function (err, f) {
    console.log('Saved!');
    console.log(f);
});

const solve = () => {
    const result = 2 + 2; // Ukázkový příklad
    console.log(`Výsledek je: ${result}`);
};

solve();
