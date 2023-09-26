const keyword_extractor = require("keyword-extractor");
var fs = require("fs");

let extractKeywords = (query, removeDuplicate) => {
    let extraction_result =  keyword_extractor.extract(query,{
        language:"english",
        remove_digits: true,
        return_changed_case:true,
        remove_duplicates: removeDuplicate
    });
    return extraction_result;
}

let readFileAndExtract = (fileDir, removeDuplicate) =>{
    const data = fs.readFileSync(fileDir, "utf-8");

    let probStatement;
    probStatement = data.toString();
    return extractKeywords(probStatement, removeDuplicate);
}

let findFrequency = (distinctKeywordsArray, keywordsArray) => {
    let frequency = [];
    let cnt = 0;
    let j = 0;
    for(let i = 0; i < keywordsArray.length; i++){
        if(distinctKeywordsArray[j] === keywordsArray[i]){
            cnt++;
        }else{
            frequency.push(cnt);
            cnt = 0;
            j++;
            i--;
        }
    }
    frequency.push(cnt);

    return frequency;
}

let readFileAsStr = (filepath) =>{
    let data = fs.readFileSync(filepath).toString().split("\n");
    return data;
}

let writeOnAFile = (fileName, arrayTowrite) => {
    const writeStream = fs.createWriteStream(fileName);
    const pathName = writeStream.path;
    arrayTowrite.forEach(value => writeStream.write(`${value}\n`));

    writeStream.on('finish', () => {
        console.log(`wrote all the array data to file ${pathName}`);
    });
    writeStream.on('error', (err) => {
        console.error(`There is an error writing the file ${pathName} => ${err}`)
    });
    writeStream.end();
}
module.exports ={
    extractKeywords,
    readFileAndExtract,
    findFrequency,
    readFileAsStr,
    writeOnAFile
}