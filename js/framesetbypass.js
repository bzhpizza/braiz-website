document.onreadystatechange = function(){
	// change title
	let title = document.getElementsByTagName('title')[0];
	title.innerHTML = "Braiz'Pizza";

	// get head from title
	let head = title.parentNode;

	// change favicon
	let icon = document.createElement("link");
	icon.href = "https://bzhpizza.github.io/braizpizza.github.io/img/braiz_logo.png";
	icon.rel = "icon";
	icon.type = "image/png";
	head.appendChild(icon);
	console.log('done');
}
