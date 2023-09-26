const express = require("express");
const ejs = require("ejs"); //View Engine
const bodyParser = require("body-parser");
const path = require("path");
const TFIDF_matrix_generator = require("./helper/TFIDF_matrix_generate");
const {extractKeywords, findFrequency, readFileAsStr} = require('./helper/extractor');
const responseArrayGenerator = require("./helper/similarityAlgo");

const app = express();

const IDF = readFileAsStr('IDF.txt');
const uniquekeywords = readFileAsStr('keywords.txt');
const TFIDF = readFileAsStr('TFIDF.txt');
const magnitude = readFileAsStr('magnitude.txt');
const problem_titles = readFileAsStr(__dirname + "/helper/scraped_files/problem_titles.txt");
const problem_urls = readFileAsStr(__dirname + "/helper/scraped_files/problem_urls.txt");

let TFIDF_array = TFIDF_matrix_generator(TFIDF);


app.use(express.json());
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(path.join(__dirname, "/public")));

const PORT = process.env.PORT || 3000;



app.get("/",(req, res) => {
    res.render("index");
})

app.post("/search", (req, res) => {
    const query = req.body.question;
    const question = query.toLowerCase();
    let responseArray = responseArrayGenerator(question, uniquekeywords, IDF, TFIDF_array, magnitude, problem_titles, problem_urls);
    if(responseArray.length == 0){
        res.render("sorry");
    }else{
        res.render("searchResult", {
            resp: responseArray
        });
    }

});

app.get("/question/:documentNum", (req, res) => {

    const documentNum = req.params.documentNum;
    const idx = documentNum - 1;
    const probStatement = readFileAsStr(__dirname + "/helper/scraped_files/problems/problem_text_"+ (idx + 1) +".txt");

    res.render("questionDesc", {
        title: problem_titles[idx],
        url: problem_urls[idx],
        statement: probStatement
    });

    
});
  

app.listen(PORT, () => {
    console.log("Server is running on port " + PORT);
  });