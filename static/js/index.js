

window.onload = function() {
	
	var ico = document.querySelector(".ico");
	
	var label = document.querySelector(".upload");
	label.onmouseover = function() {
		ico.innerText = "";
	};
	
	label.onmouseout = function() {
		if(label.innerText == "请选择文件"){
			ico.innerText = "";
		}
	};
	
	var upFile = document.getElementById("upload");
	upFile.onchange = function() {
		var fileName;
		fileName = this.files[0] && this.files[0].name;
		if(fileName){
			label.innerText = fileName;
		}
	};
	
	
}



