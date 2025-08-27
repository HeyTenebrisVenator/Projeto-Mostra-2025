async function send_URL() {
    try {
        const info = document.getElementById("inp").value;
        const response = await fetch("http://fndetector.online/send_url?data=" + encodeURIComponent(info));
        document.getElementById("h1style").textContent ="Processando..."
        document.getElementById("h1style").style ="color: rgb(203, 115, 0);"
        
        if (!response.ok) {
            document.getElementById("h1style").textContent ="ERRO"
            document.getElementById("h1style").style ="color: rgba(0, 0, 0, 1);"
            throw new Error("Erro na requisição: " + response.status);
        }
        
        const data = await response.json();
        console.log("Resposta da API (URL):", data);
    } catch (error) {
        console.error("Erro:", error);
    }
}

async function send_Title() {
    try {
        const info = document.getElementById("inp").value;
        document.getElementById("h1style").textContent ="Processando..."
        document.getElementById("h1style").style ="color: rgb(203, 115, 0);"
        const response = await fetch("http://fndetector.online/send_title?data=" + encodeURIComponent(info));
        
        if (!response.ok) {
            document.getElementById("h1style").textContent ="ERRO"
            document.getElementById("h1style").style ="color: rgb(255, 0, 0);"
            throw new Error("Erro na requisição: " + response.status);
        }
        
        const data = await response.text();
            document.getElementById("h1style").innerHTML = "<h1 id='h1style' style='color: rgb(0, 0, 0);'>" + data + "</h1>"    } catch (error) {
        console.error("Erro:", error);
    }

}

