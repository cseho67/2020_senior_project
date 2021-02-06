var express = require('express');

let {PythonShell} = require('python-shell');

var router =express.Router();


router.get('/runpy', (req, res, next) => {
    
    console.log('실행')
      
    var options = {
     mode:'text',
     pythonPath: '',
     pythonOptions: ['-u'],
     scriptPath: './src',
     args : ['C:/Users/CHA/sserver/sungk/src/test1.jpg','C:/Users/CHA/sserver/sungk/src/test2.jpg','./src/out.jpg','./src/out2.jpg']
    }
    PythonShell.run('swap_hair.py',options, function (err, results){

        if (err ) {
            console.log("first_user_db error : world cup input eror");
            console.log('results: %j', results);
            res.status(500).send('Server Input Error');
            throw err;
        }
        else {
            console.log('results: %j', results);
            res.json({ message: 'success'});
        }
       
    });


});

router


module.exports = router;