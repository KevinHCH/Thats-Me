const getRandom = (max = 500) => Math.floor(Math.random() * Math.floor(max));

	const createImages = (maxImages = 5) => {
		const defaultUrl = "https://picsum.photos/id/404/700/800"
		for (let i = 0; i <= maxImages; i++) {

			let url = `https://picsum.photos/id/${getRandom()}/700/800`
			const figure = document.createElement("figure")
			figure.classList.add("col-md-4", "d-inline")
			fetch(url)
				.then(res => {
					if (res.status == 404) {
						url = defaultUrl
					}
					const img = document.createElement("img")
					img.setAttribute("src", url)
					img.setAttribute("loading", "lazy")
					img.setAttribute("alt", "picture")
					img.classList.add("img-fluid", "d-inline")

					figure.appendChild(img)
					document.getElementById("images").appendChild(figure)
				})
		}

	}//createImages
	
	// MAIN
	const totalRandom = getRandom(20)
	createImages(totalRandom)