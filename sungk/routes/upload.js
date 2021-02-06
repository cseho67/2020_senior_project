
var express = require('express');
var router =express.Router();
var fs =require('fs')

const multer = require('multer')

const storage = multer.diskStorage({
    destination:(req,file,callback) => {
        callback(null,'./src/');
    },
    filename:(req, file, callback) =>{
        callback(null,file.originalname);
    }
});

const upload = multer({storage:storage})

router.post('/upload',upload.single('img'),(req,res) => {
    res.json(req.file)
    console.log(req.file)
    console.log("이미지 받기 성공")
})

router.post('/result', function(req, res) {
 
    fs.readFile('./src/out.jpg', function(err, data) {
        res.writeHead(200, {"Content-Type": "image/png"});
        res.write(data);
        res.end();
    });
});


router.post('/', function(req, res, next) {
    res.send('test');
  });


module.exports = router;




