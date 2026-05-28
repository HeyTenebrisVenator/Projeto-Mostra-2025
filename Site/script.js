async function send_URL() {
    try {
        const info = document.getElementById("inp").value;
        document.getElementById("h1style").textContent = "Processing...";
        document.getElementById("h1style").style = "color: rgb(203, 115, 0);";

        const response = await fetch("/send_url?data=" + encodeURIComponent(info));

        if (!response.ok) {
            document.getElementById("h1style").textContent = "ERROR";
            document.getElementById("h1style").style = "color: rgba(0, 0, 0, 1);";
            throw new Error("Request error: " + response.status);
        }

        const data = await response.text();
        document.getElementById("h1style").innerHTML = "<h1 id='h1style' style='color: rgb(0, 0, 0);'>" + data + "</h1>";
    } catch (error) {
        console.error("Error:", error);
    }
}

async function send_Title() {
    try {
        const info = document.getElementById("inp").value;
        document.getElementById("h1style").textContent = "Processing...";
        document.getElementById("h1style").style = "color: rgb(203, 115, 0);";

        const response = await fetch("/send_title?data=" + encodeURIComponent(info));

        if (!response.ok) {
            document.getElementById("h1style").textContent = "ERROR";
            document.getElementById("h1style").style = "color: rgb(255, 0, 0);";
            throw new Error("Request error: " + response.status);
        }

        const data = await response.text();
        document.getElementById("h1style").innerHTML = "<h1 id='h1style' style='color: rgb(0, 0, 0);'>" + data + "</h1>";
    } catch (error) {
        console.error("Error:", error);
    }
}
