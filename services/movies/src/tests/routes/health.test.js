const http = require("http");

describe("Health endpoint", () => {
  it("/health", async () => {
    const res = await http.get("http://localhost:3000/health", (resp) => {
      expect(resp.statusCode).toEqual(200);
    });
  });
});
