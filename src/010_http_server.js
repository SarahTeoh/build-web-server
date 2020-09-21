var http = require('http'); 
var fs = require('fs');
var path = require('path');
var app = require('express')();
var http = require('http').createServer(app);
var io= require('server.io')(http);
var bodyParser = require('body-parser');
/*require() doesn't work like #include or import does in other languages.
require() returns a reference to the resolved module. That reference must be assigned to a variable.
*/

var folderPath = __dirname + '/../html';

app.use(express.static(folderPath))
app.use(bodyParser.json());  // Handle POST messages
app.use(bodyParser.urlencoded({ extended: false })) //provides middleware for automatically parse forms w content type of application/x-www-urlencoded and storing the result as a dictionary (object) in req.body

app.get('/test.html', function(req, res) {
	res.sendFile(path.join(__dirname + '/../html/test.html'));
});

app.get('/', function(req, res) {
	res.send('It Works!');
});

app.post('/post.html', function(req, res) {
	var reply = 'Your Name: ' + req.body.name + '<br>' + 'Your Student ID: ' + req.body.studentID
	res.send(reply);
	console.log('Name: ' + req.body.name); //req.body will return {<name of input>: '<data>', ....}
	console.log('Student ID: ' + req.body.studentID)

});


http.listen(11111, function(){
	console.log('connected');
});

io.on('connection', function(socket){
	console.log('a user connected');
	socket.on('disconnect', function(){
		console.log('user disconnected');
	});
});
/*
//404 request response
function send404Response(response){
	response.writeHead(404, {"Context-Type" : "text/plain"});
	response.write("Error 404: Page not found!");
	response.end();
}

//Non-persistent response, which the connection will end once the request is being responded to
//Handle a user request
function onRequest(request, response){
	//examine the request
	if ( request.method == 'GET' && request.url == '/'){
		response.writeHead(200, {'Context-Type': 'text/plain'});
		response.write("It works!");
		response.end();
	}else if( request.method == 'GET' && request.url == '/test.html'){
		filePath = './test.html';
		var extname = path.extname(filePath);
		console.log(__dirname);
		response.writeHead(200, {"Content-Type": "image/jpg"});
		response.write(fs.readFileSync('./test.html'));
		response.end()
		//fs.createReadStream("./test.html").pipe(response); //create readable stream from the html file and send it to user as 'response'
	}
	else{
		//if requested file not found
		send404Response(response)
	}
}

http.createServer(onRequest).listen(11111);
console.log('Server is running!');*/