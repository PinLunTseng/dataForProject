// carousel
let carouselSelectedIndex = 0

let carouselTitles = document.querySelectorAll("#id_model div")

let carouselBtns = document.querySelectorAll(".carousel-btn")

let carouselTabs = document.querySelectorAll("#content-wrapper > div")

function toggleCarouselBtn() {
    carouselBtns[0].style.opacity = carouselSelectedIndex > 0 ? 1 : 0
    carouselBtns[1].style.opacity = carouselSelectedIndex < carouselTabs.length - 1 ? 1 : 0
}

function refreshCarouselTitle() {
    carouselTitles.forEach((title, index) => {
        title.style.display =
            index === carouselSelectedIndex ? "block" : "none"
    })
}

function refreshCarouselTab() {
    carouselTabs.forEach((tab, index) => {
        tab.style.display =
            index === carouselSelectedIndex ? "block" : "none"
    })
}

function assignHiddenInput() {
    document.querySelector("#id_model").setAttribute('value', carouselSelectedIndex + 1)
}

function refreshCarousel() {
    toggleCarouselBtn()
    refreshCarouselTitle()
    refreshCarouselTab()
    assignHiddenInput()
}

carouselBtns[0].addEventListener("click", () => {
    carouselSelectedIndex = Math.max(0, carouselSelectedIndex - 1)
    refreshCarousel()
})

carouselBtns[1].addEventListener("click", () => {
    carouselSelectedIndex = Math.min(carouselTabs.length - 1, carouselSelectedIndex + 1)
    refreshCarousel()
})

// init
refreshCarousel()


// init

let builder = new BubbleBuilder()
builder.createBubbles()