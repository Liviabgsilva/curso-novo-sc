import http from "http";

const app = http.createServer((req, res) => {
    res.writeHead(200, { "Content-Type": "text/plain" });
    res.end("Servidor criado...");
});

app.listen(3000, () => {
    console.log("Servidor criado...");
});

