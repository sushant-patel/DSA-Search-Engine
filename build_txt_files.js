var fs = require('fs');
const {readFileAndExtract, findFrequency, writeOnAFile} = require('./helper/extractor');


let keywordsArray = [];
let distinctKeywordsArray = [];
let IDF = [];

for(let i = 1; i < 3286; i++){
    let extraction_result = readFileAndExtract(__dirname + "/helper/scraped_files/problems/problem_text_"+i+".txt", true);
    
    keywordsArray = [...keywordsArray, ...extraction_result];
    let tmp = [...distinctKeywordsArray, ...extraction_result];

    distinctKeywordsArray = [... new Set(tmp)];
}

distinctKeywordsArray.sort();
keywordsArray.sort();

let frequency = findFrequency(distinctKeywordsArray, keywordsArray);


for(let i = 0; i < frequency.length; i++){
    IDF.push(Math.log10( 3285 / frequency[i]));
}

writeOnAFile('keywords.txt', distinctKeywordsArray);
writeOnAFile('IDF.txt', IDF);

// ----------------------------------------------------------------------
// Now calculating TFIDF values & magnitude values

let magnitude = new Array(3285);

for(let i = 0; i < 3285; ++i) magnitude[i] = 0;

for(let i = 1; i < 3286; i++){
    let extraction_result = readFileAndExtract(__dirname + "/helper/scraped_files/problems/problem_text_"+i+".txt", false);
    let distinctExtractedKeywords = [... new Set(extraction_result)];

    distinctExtractedKeywords.sort();
    extraction_result.sort();

    let freqOfKeywordsInExtractionResult = findFrequency(distinctExtractedKeywords, extraction_result);

    for(let m = 0; m < distinctExtractedKeywords.length; m++){
        if(freqOfKeywordsInExtractionResult[m] != 0){
            let KWindex = distinctKeywordsArray.indexOf(distinctExtractedKeywords[m]);
            let TFval = freqOfKeywordsInExtractionResult[m] / (extraction_result.length);

            let TFIDFval = TFval * IDF[KWindex];

            magnitude[i - 1] += (TFIDFval * TFIDFval);
            fs.appendFileSync("TFIDF.txt", `${i} ${KWindex} ${TFIDFval}\n`, "utf-8");
        }
    }
    magnitude[i - 1] = Math.sqrt(magnitude[i - 1]);
}

writeOnAFile("magnitude.txt", magnitude);