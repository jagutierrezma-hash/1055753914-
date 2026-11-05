const http = require("node:http");

const server = http.createServer((request, response) => {
  const url = new URL(request.url, `http://${request.headers.host}`);
  const match = url.pathname.match(/^\/par-impar\/(-?\d+)$/);

  response.writeHead(200, { "Content-Type": "application/json" });
  response.end(
    JSON.stringify({
      numero,
      mensaje: numero % 2 === 0 ? "el numero es par" : "el numero es impar",
    }),
  );
});

server.listen(3000, "0.0.0.0");