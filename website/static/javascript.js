
const search_url = "http://api.tvmaze.com/singlesearch/shows?q="

document.getElementById("search-sec-2").style.display='none';


async function getShow(completeURL)
{

	const response = await fetch(completeURL);
	const data = await response.json();
	console.log(data.name);
	document.getElementById("show-picture").src = data.image.medium;
	document.getElementById("show-name").innerHTML = data.name;
	document.getElementById("show-premiere").innerHTML = "Premiered on " + data.premiered;
	document.getElementById("show-rating").innerHTML = "Rating: " + data.rating.average;
	document.getElementById("show-status").innerHTML = data.status;
	document.getElementById("show-channel").innerHTML = data.network.name;
	document.getElementById("show-runtime").innerHTML = data.runtime + " minutes";
	document.getElementById("show-summary").innerHTML = data.summary;

	

	// fetch(completeURL)
	// 	.then(response => {
	// 		return response.json();
	// 	})
	// 	.then(data => {
	// 		document.getElementById("show-picture").src = data.image.medium;
	// 		document.getElementById("show-name").innerHTML = data.name;
	// 		document.getElementById("show-premiere").innerHTML = "Premiered on " + data.premiered;
	// 		document.getElementById("show-rating").innerHTML = "Rating: " + data.rating.average;
	// 		document.getElementById("show-status").innerHTML = data.status;
	// 		document.getElementById("show-channel").innerHTML = data.network.name;
	// 		document.getElementById("show-runtime").innerHTML = data.runtime + " minutes";
	// 		document.getElementById("show-summary").innerHTML = data.summary;
	// 	})
	// 	.catch(error => {
	// 		console.log('error!');
	// 		console.error(error);
	// 	});
}

function submitButton() {
	var input = document.getElementById("searchbar");
		const completeURL = search_url+input.value;

		getShow(completeURL)
			.then(response => {
				console.log('Success');
			})
			.catch(error => {
				console.log('error!');
				console.error(error);
			});
		document.getElementById("search-sec-2").style.display='block';
	
}