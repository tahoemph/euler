var answer = function() {
    var rv = 0;
    for(x = 1; x < 1000; x++) {
        if (x % 3 == 0 || x % 5 == 0) {
            rv += x;
        }
    }
    return rv;
}

console.log(answer());

