class BubbleBuilder {
    bubbleConfig = [
        // pink
        {
            color: "rgb(250, 228, 223)",
            size: "20px",
            top: "20%",
            left: "70%",
            // animation: "floating-bubble-up-down 15s infinite linear",
        },
        // blue
        {
            color: "rgb(226, 234, 234)",
            size: "100px",
            top: "20%",
            left: "40%",
            // animation: "floating-bubble-down-up 15s infinite linear",
        },
        // purple
        {
            color: "rgb(239, 226, 236)",
            size: "60px",
            top: "20%",
            left: "10%",
            // animation: "floating-bubble-up-down 15s infinite linear",
        },
        // green
        {
            color: "rgb(227, 244, 224)",
            size: "30px",
            top: "20%",
            left: "30%",
            // animation: "floating-bubble-down-up 15s infinite linear",
        },
    ]

    constructor() {

    }

    createBubbles(sectionNumber = 2) {
        let sections = document.querySelectorAll(".bubbles")
        sections.forEach((section, index) => {
            section.style.left = `${(75 / (sectionNumber - 1)) * (index % sectionNumber)}vw`
            section.style.top = `${index * 20}vh`
            Array(4).fill(0).forEach((_, index) => {
                let { color, size, top, left, animation } = this.bubbleConfig[index]

                let node = document.createElement("div")
                node.classList = ["bubble"]
                node.style.background = color
                node.style.width = size
                node.style.height = size
                node.style.top = top
                node.style.left = left
                node.style.animation = Math.random() > 0.5 ? "floating-bubble-down-up 15s infinite linear" : "floating-bubble-up-down 15s infinite linear"

                section.appendChild(node)
            })
        })
    }
}
