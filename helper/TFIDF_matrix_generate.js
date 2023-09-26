const N = 3285;

const generateTFIDFMatrix = (TFIDF) =>{
    let TFIDF_array = [];

    for(let j = 0; j < N + 1; j++){
        TFIDF_array[j] = [];
    }

    for(let j = 0; j < TFIDF.length; j++){
        if(TFIDF[j] != ""){
            let TFIDFval = TFIDF[j].split(" ");
            TFIDF_array[parseInt(TFIDFval[0])].push( [parseInt(TFIDFval[1]), parseFloat(TFIDFval[2])] );
        }
    }
    return TFIDF_array;
}

module.exports = generateTFIDFMatrix;