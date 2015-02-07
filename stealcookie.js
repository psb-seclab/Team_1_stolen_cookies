function Run()
{
	// Run TestSetCookie
	TestSetCookie("person", "jeff", 1);
	// Run GetTestCookie
	GetTestCookie("person");
}

function Steal(cname)
{

}

function Transmit()
{

}

// This function creates a test cookie
// 1. Need a cookie name and value
// 2. (Optional) Add a time stamp for expiration
// 3. (Optional) Add a path for the cookie
function TestSetCookie(cookiename, cookievalue, cookieexp)
{
	document.cookie = cookiename + "=" + cookievalue + ";";
}

//
function GetTestCookie(cookiename)
{
	// A list of common cookie value names
	//var commonNames = ["username", "name", "login", "email"];

	var strings = document.cookie.split(";");
	document.getElementById("cookiedata").innerHTML = strings[1];
	console.log(strings.length);
}