function Run()
{
	// Run TestSetCookie
	TestSetCookie("person", "jeff", 1);
	// Run GetTestCookie
	GetTestCookie("person");
	Steal("mint");
}

function Steal(cname)
{
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if (c.indexOf(name) == 0) return c.substring(name.length, c.length);
    }
    return "";
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

function GetTestCookie(cookiename)
{
	var strings = document.cookie.split(";");
	document.getElementById("cookiedata").innerHTML = strings[0];
}